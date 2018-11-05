from rolepermissions.permissions import register_object_checker
from mysite.roles import Verauth

@register_object_checker()
def seeall(role, user, cci):
    if role ==Verauth:
        return True

    if user.cci == cci:
        return True

    return False