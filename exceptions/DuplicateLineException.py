import json


class DuplicateLineException(Exception):
    def __init__(self, message="Line already present"):
        self.message = message
        super().__init__(self.message)

    def to_dict(self):
        return {
            "msg": self.message
        }
