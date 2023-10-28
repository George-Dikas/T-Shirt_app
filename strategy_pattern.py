import abc

""" STRATEGY PATTERN """

#Create an interface for the strategy
#abstract class
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def payment_method(self):
        pass


#Create concrete strategy classes
#Class for Credit/Debit Cards
class CreditDebitCard(Strategy):
     def payment_method(self):
         return "Credit/Debit Card"


#Class for Money/Bank Transfer
class MoneyBank(Strategy):
     def payment_method(self):
         return "Money/Bank Transfer"


#Class for Cash
class Cash(Strategy):
     def payment_method(self):
         return "Cash"


#class for the Contex
class Context:
    def __init__(self,strategy):
        self.strategy=strategy

    def execute_strategy(self):
        return self.strategy.payment_method()
