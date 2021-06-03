from flask_login import AnonymousUserMixin
from todolist.User import Role

class AnonUser(AnonymousUserMixin):
    def role(self):
        return Role.Writer