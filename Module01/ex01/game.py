class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        if type(first_name) != str:
            print("The first name should be a string.")
            raise ValueError()
        self.first_name = first_name
        if type(is_alive) != bool:
            print("The second parameter is either 'True' or 'False'.")
            raise ValueError
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        super().__init__(first_name = self.first_name, is_alive = False)
        
        
        