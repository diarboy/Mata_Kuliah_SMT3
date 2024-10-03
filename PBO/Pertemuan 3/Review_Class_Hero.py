class Hero:
    def __init__ (self, name, role, healthpoint, attackdamage, skill):
        self.nm = name
        self.rl = role
        self.hp = healthpoint
        self.ad = attackdamage
        self.sk = skill

    # Membuat Method Attack
    def attack(self, target):
        target.hp -= self.ad
        print(f"{self.nm} menyerang {target.nm}")
        print(f"{target.nm} kehilangan {self.ad} HP.")

    # Membuat Method Use Skill
    def useSkill(self, target):
        target.hp -= self.ad * 2.5
        print(f"{self.nm} Menggunakan Skill: {self.sk}! \n{target.nm} Kehilangan {int(self.ad * 2.5)} HP")

    # Membuat Method show Stats
    def showStats(self):
        print("===============")
        print(f"Status {self.nm} :")
        print("===============")
        print(f"Role    : {self.rl}")
        print(f"HP      : {int(self.hp)}")
        print(f"AD      : {self.ad}")
        print(f"Skill   : {self.sk}")
        print("===========================")
layla = Hero("Layla", "Marksman", 350, 50, "Destruction Rush")
layla.showStats()
tigreal = Hero("Tigreal", "Tank", 500, 40, "Sacred Hammer")
tigreal.showStats()

layla.attack(tigreal)
tigreal.useSkill(layla)
layla.showStats()
tigreal.showStats()