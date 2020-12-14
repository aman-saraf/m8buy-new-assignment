from models.Line import Line

class LineRepository:

    def getLineByCode(self, code):
        return Line.objects.raw({'code':  code})

    def saveLine(self, code, name):
        metroLine = Line(code, name)
        savedMetroLine = metroLine.save().to_son().to_dict()
        savedMetroLine['_id'] = str(savedMetroLine['_id'])
        return savedMetroLine
