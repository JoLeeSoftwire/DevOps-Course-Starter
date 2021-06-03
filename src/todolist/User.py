from flask_login import UserMixin
import enum

class Role(enum.Enum):
    Reader = 0
    Writer = 1


class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def role(self):
        return Role.Writer if (self.id == "57954007") else Role.Reader