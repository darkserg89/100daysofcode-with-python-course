


BATTLE_TABLE = {'rock':{'rock':'draw','scissors':'win','paper':'lose'},
'paper':{'rock':'win','scissors':'lose','paper':'draw'},
'scissors':{'rock':'lose','scissors':'draw','paper':'win'}}

class Player:
    def __init__(self,name):
        self.name = name
        self.count = 0
        
    def get_name():
        return self.name
        
class Roll:
    def __init__(self,roll_type):
        self.roll_type = roll_type.lower()
    
    
    def get_type():
        return self.roll_type
    
    
    def can_defeat(self,p2_roll):
        return BATTLE_TABLE[self.roll_type][p2_roll.roll_type]
    
