from pydantic import BaseModel, Field
import random
import json

class Character(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    level: int = Field(gt=0)
    strenght: int = Field(gt=0)
    intelligence: int = Field(gt=0)
    health: int
    stamina: int = Field(gt=0)
    magicka: int = Field(gt=0)

    def physical_attack(self):
        if self.stamina <= 0:
            return 0
        toss = random.randint(0, 4)
        if toss == 0:
            self.stamina -= 200 / self.strenght
            return 0
        damage = self.strenght * random.randint(1, 6) * self.stamina / 100
        self.stamina -= 200 / self.strenght
        return round(damage, 2)

    def magical_attack(self):
        if self.magicka <= 0:
            return 0
        toss = random.randint(0, 5)
        if toss == 0:
            self.magicka -= 200 / self.intelligence
            return 0
        damage = self.intelligence * random.randint(1, 6) * self.magicka / 100
        self.magicka -= 200 / self.intelligence
        return round(damage, 2)


mage = Character(
    name='Merlino',
    level=1,
    strenght=1,
    intelligence=6,
    health=100,
    stamina=50,
    magicka=200
)

warrior = Character(
    name='Arthur',
    level=1,
    strenght=6,
    intelligence=1,
    health=150,
    stamina=150,
    magicka=50
)

# --- Qui salvo lo storico ---
battle_log = []

turno = 1
while True:
    turno_data = {"turno": turno, "azioni": []}
    toss = random.randint(1, 2)

    if toss == 1:
        # Mage attacca per primo
        damage_m = mage.magical_attack()
        warrior.health -= damage_m
        turno_data["azioni"].append({
            "attaccante": mage.name,
            "tipo": "magia",
            "danno": damage_m,
            "magicka_rimanente": mage.magicka,
            "health_warrior": warrior.health
        })
        if warrior.health <= 0:
            turno_data["winner"] = mage.name
            battle_log.append(turno_data)
            break

        damage_w = warrior.physical_attack()
        mage.health -= damage_w
        turno_data["azioni"].append({
            "attaccante": warrior.name,
            "tipo": "fisico",
            "danno": damage_w,
            "stamina_rimanente": warrior.stamina,
            "health_mage": mage.health
        })
        if mage.health <= 0:
            turno_data["winner"] = warrior.name
            battle_log.append(turno_data)
            break
    else:
        # Warrior attacca per primo
        damage_w = warrior.physical_attack()
        mage.health -= damage_w
        turno_data["azioni"].append({
            "attaccante": warrior.name,
            "tipo": "fisico",
            "danno": damage_w,
            "stamina_rimanente": warrior.stamina,
            "health_mage": mage.health
        })
        if mage.health <= 0:
            turno_data["winner"] = warrior.name
            battle_log.append(turno_data)
            break

        damage_m = mage.magical_attack()
        warrior.health -= damage_m
        turno_data["azioni"].append({
            "attaccante": mage.name,
            "tipo": "magia",
            "danno": damage_m,
            "magicka_rimanente": mage.magicka,
            "health_warrior": warrior.health
        })
        if warrior.health <= 0:
            turno_data["winner"] = mage.name
            battle_log.append(turno_data)
            break

    # Recupero energia
    warrior.stamina += warrior.strenght * 2
    mage.magicka += mage.intelligence * 2

    turno_data["recupero"] = {
        warrior.name: {"stamina": warrior.stamina},
        mage.name: {"magicka": mage.magicka}
    }

    battle_log.append(turno_data)
    turno += 1

# Stampa JSON finale
print(json.dumps(battle_log, indent=4, ensure_ascii=False))
