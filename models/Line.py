from pymodm import MongoModel, fields, connect

class Line(MongoModel):
    code = fields.CharField()
    name = fields.CharField()

    class Meta:
        final = True
