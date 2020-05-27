

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
    self.name = name
    self.__dict__.update(kwargs)
    if hasattr(self, 'value'):
        self.value = 0
    Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        if isinstance(origin, int):
            src_id = origin
            src_name = None
        elif isinstance(origin, str):
            src_name = origin
            src_id = None
        else:
            return False
        if isinstance(dest, int):
            dest_id = dest
            dest_name = None
        elif isinstance(dest, str):
            dest_name = dest
            dest_id = None
        else:
            return False
        if isinstance(amount, float)n and amount >= 0:
            pass
        else:
            return False

        # right object
        if dest_id:
            if self.account[dest_id] in self.account:
                pass
            else:
                return False
        else:
            if self.account.dest_name in self.account: # do a fct ?
                pass
            else:
                return False
        if src_id:
            if self.account[src_id] in self.account:
                # check is has enoght money
                if self.account[src_id].amount < amount:
                    return False
            else:
                return False
        else:
            if self.account.src_name in self.account: # do a fct ?
                # check is has enoght money
                pass
            else:
                return False
        

        # do to check if is corrupted

        return True

    def fix_account(self, account):
        if isinstance(account, int):
            src_id = account
        elif isinstance(account, str):
            src_name = account
        else:
            return False
        return True
    """
    fix the corrupted account
    """