from rolepermissions.roles import AbstractUserRole
class Verauth(AbstractUserRole):
    available_permissions = {
        'read_all': True,
    }

class cciperson(AbstractUserRole):
    available_permissions = {
        'write_all': True,
        'read_his': True
    }