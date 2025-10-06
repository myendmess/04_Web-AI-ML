class Character:
    def __init__(self, name, level, strength, agility, intelligence, stamina):
        self.name = name
        self.level = level
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stamina = stamina
    
    def stats(self):
        stats = {
            'name': self.name,
            'level': self.level,
            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
            'stamina': self.stamina
        }
        return f'Stats: {stats}'
    
    
    
    def level_up(self):
        self.level += 1
        return self.level
    def strengthen(self, amount):
        self.strength += amount
        return self.strength
    def agilitize(self, amount):
        self.agility += amount
        return self.agility
    def intellectualize(self, amount):
        self.intelligence += amount
        return self.intelligence
    def staminize(self, amount):
        self.stamina += amount
        return self.stamina


Shiro = Character("Shiro", 1, 1, 1, 1, 1)
print(Shiro.level_up())
print(Shiro.strengthen(1))
print(Shiro.agilitize(1))
print(Shiro.intellectualize(1))
print(Shiro.staminize(1))
print(Shiro.stats())
