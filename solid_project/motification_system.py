from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def message(self):
        pass


class EmailNotifier(Notifier):

    def message(self):
        print("email")

class SMSNotifier(Notifier):

    def message(self):
        print('sms')


class PushNotifier(Notifier):

    def message(self):
        print("push")



