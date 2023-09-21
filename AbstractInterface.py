from abc import ABC, abstractmethod

class Interface(ABC):
    
    @abstractmethod
    def get_data(self):
        raise NotImplementedError('You did something wrong')
    
class User(Interface):
    def __init__(self, name):
        self.name = name
                
    def get_data(self) -> str:
        super().get_data()
        return f'name: {self.name}'
    
class Phone(Interface):
    def __init__(self, phones, user: User):
        self.phones = phones
        self.user = user
        
    def get_data(self) -> str:
        super().get_data()
        return f'name: {self.user.get_data()}, phone: {self.phone}'
    
class Notes(Interface):
    def __init__(self, notes):
        self.notes = notes
        
    def get_data(self) -> str:
        super().get_data()
        return self.notes
    
class ListCommands(Interface):
    def __init__(self):
        self.commands = list()
        
    def get_data(self):
        super().get_data()
        return self.commands
    

