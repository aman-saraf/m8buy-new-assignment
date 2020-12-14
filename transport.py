from flask import (Flask, request)
from exceptions.DuplicateLineException import DuplicateLineException
from repository.LineRepository import LineRepository
from pymodm import connect
from service.SecretService import SecretService

app = Flask(__name__)
secretService = SecretService()
connect(secretService.getSecretValue('MONGODB_CONNECTION_STRING'))
lineRepository = LineRepository()


@app.route('/metro/line', methods=['POST'])
def create_metro_line():
    lineCode = request.json['code']
    lineName = request.json['name']
    try:
        lineCount = lineRepository.getLineByCode(lineCode).count()
        if (lineCount >= 1):
            raise DuplicateLineException()
        line = lineRepository.saveLine(lineCode, lineName)
    except DuplicateLineException as error:
        return {"success": False, "error": error.to_dict()}
    except Exception as error:
        return {"success": False, "error": {"msg": str(error)}}
    return {"success": True, "data": line}


if __name__ == '__main__':
    app.run(debug=True)
