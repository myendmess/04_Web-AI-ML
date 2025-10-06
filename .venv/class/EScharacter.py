import random
import time
from pydantic import BaseModel, Field


class Character(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    level: int = Field(gt=0)
    strength: int = Field(gt=0)
    intelligence: int = Field(gt=0)
    health: int = Field(gt=0)
    stamina: int = Field(gt=0)
    magicka: int = Field(gt=0)

    def physical_attack(self):
        if self.stamina <= 0:
            print(f"{self.name} is too exhausted to perform a physical attack!")
            return 0
        self.stamina -= int(20 / self.strength)
        return self.strength * random.randint(1, 6)

    def magical_attack(self):
        if self.magicka <= 0:
            print(f"{self.name} is out of magicka!")
            return 0
        self.magicka -= int(20 / self.magicka)
        return self.intelligence * random.randint(1, 6)

    def is_alive(self):
        return self.health > 0

    def __repr__(self):
        return f"<Character name={self.name}, level={self.level}, hp={self.health}, sta={self.stamina:.1f, int=0}, mag={self.magicka:.1f}>"


# Define characters
mage = Character(
    name='Merlin',
    level=1,
    strength=20,
    intelligence=110,
    health=1000,
    stamina=80,
    magicka=200
)

knight = Character(
    name='Pendragon',
    level=1,
    strength=90,
    intelligence=70,
    health=1500,
    stamina=150,
    magicka=1
)

# Fight simulation
print("⚔️ Battle starts between Mage and Knight!\n")
while mage.is_alive() and knight.is_alive():
    toss = random.randint(1, 2)

    if toss == 1:
        # Mage turn
        if random.choice(["magic", "physical"]) == "magic":
            damage = mage.magical_attack()
            knight.health -= damage
            print(f"⚡ {mage.name} casts a spell! Deals {damage} damage. {knight.name} HP = {knight.health}")
        else:
            damage = mage.physical_attack()
            knight.health -= damage
            print(f"🗡️ {mage.name} strikes physically! Deals {damage} damage. {knight.name} HP = {knight.health}")
    else:
        # Knight turn
        if random.choice(["magic", "physical"]) == "physical":
            damage = knight.physical_attack()
            mage.health -= damage
            print(f"🗡️ {knight.name} strikes physically! Deals {damage} damage. {mage.name} HP = {mage.health}")
        else:
            damage = knight.magical_attack()
            mage.health -= damage
            print(f"⚡ {knight.name} casts a spell! Deals {damage} damage. {mage.name} HP = {mage.health}")

    time.sleep(1)

# Winner
print("\n🏆 The winner is:")
if mage.is_alive():
    print(mage)
else:
    print(knight)
