from abc import ABC, abstractmethod, abstractproperty


class AbstractBuilder(ABC):

    @abstractmethod
    def create_id(self, id):
        pass

    @abstractmethod
    def create_balance(self, balance):
        pass

    @abstractmethod
    def create_rate(self, rate):
        pass


class BankAccount():

    def __init__(self):
        self.attributes = {}

    def add(self, key, value):
        self.attributes[key] = value

    def describe(self):
        print(self.attributes)


class BankAccountBuilder(AbstractBuilder):

    def __init__(self):
        self.bank_account = BankAccount()

    def create_id(self, id):
        self.bank_account.add('id', id)

    def create_balance(self, balance):
        self.bank_account.add('balance', balance)

    def create_rate(self, rate):
        self.bank_account.add('rate', rate)


builder = BankAccountBuilder()
builder.create_id(12345)
builder.create_balance(1000000.0)
builder.create_rate(3.6)
builder.bank_account.describe()

builder = BankAccountBuilder()
builder.create_id('qwerty')
builder.create_balance(2500000.0)
builder.bank_account.describe()
