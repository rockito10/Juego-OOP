from abc import ABC, abstractclassmethod

class Weapon(ABC):
    def __init__(self):
        self.damage = self.base_damage()
        
    def damage_entity(self, entity):
        print(f"te wo matar con {self.damage}")
        entity.take_damage(self.damage)
        
    @abstractclassmethod
    def base_damage(self):
        pass
    
class WoodenMurasama(Weapon):
        
    def base_damage(self):
       return 25