import pickle
import os

class Balance:
    _balance = '0'
    dir = os.getcwd()
    filename = 'db_balance.bin'
    balance_path = os.path.abspath(os.path.join(dir, filename))
    # if os.getcwd().endswith('db'):
    #     balance_path = os.path.join(dir, filename)
    # elif os.getcwd().endswith('hotdog'):
    #     dir += '/db/'
    #     balance_path = os.path.join(dir, filename)
    # else:
    #     dir = os.path.split(dir)[0] + '/db/'
    #     balance_path = os.path.join(dir, filename)


    @classmethod
    def read(cls):
        with open(cls.balance_path, 'rb') as file:
            cls._balance = pickle.load(file)
        return cls._balance

    @classmethod
    def write(cls, value: str):
        with open(cls.balance_path, 'wb') as file:
            pickle.dump(value, file)
        cls._balance = value


