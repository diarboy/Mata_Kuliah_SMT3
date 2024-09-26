class Hero:
    listhero = 0
    def __init__(self, name, role, hp, atk_dmg, skills):
        self.namahero = name
        self.rolehero = role
        self.healthpoint = hp
        self.attackdamage = atk_dmg
        self.skillhero = skills
        Hero.listhero += 1
    def __str__(self):
        return f"{self.namahero}, {self.rolehero}, {self.healthpoint}, {self.attackdamage}, {self.skillhero}"

    def launch_atk(self, opponent):
        damage = self.attackdamage
        opponent.healthpoint -= damage
        print(f"{self.namahero} menyerang {opponent.namahero} dengan {self.skillhero}, memberikan {damage} damage.")
        if opponent.healthpoint <= 0:
            print(f"{opponent.namahero} telah dikalahkan oleh {self.namahero}!")
            opponent.healthpoint = 0
        else:
            print(f"HP {opponent.namahero} tersisa {opponent.healthpoint}.")
    
    def status(self):
        return f"Hero: {self.namahero} | Role: {self.rolehero} | HP: {self.healthpoint} | ATK: {self.attackdamage} | Skill: {self.skillhero}"

H1 = Hero("Hayabusa", "Assassin", 500, 200, "Shadow Kill")
print(H1)
print("listhero: ", Hero.listhero)

H2 = Hero("Tigreal", "Tank", 1000, 100, "Implosion")
print(H2)
print("listhero: ", Hero.listhero)

H3 = Hero("Ixia", "Marksman", 500, 300, "Full Barrage")
print(H3)
print("listhero: ", Hero.listhero)

def battle(hero1, hero2):
    turn = 1
    while H1.healthpoint > 0 and H3.healthpoint > 0:
        print(f"\n--- Babak {turn} ---")
        
        if turn % 2 != 0:
            H1.launch_atk(H2)
        else:
            H2.launch_atk(H1)
        
        turn += 1

    if H1.healthpoint > 0:
        print(f"\nPemenangnya adalah {H1.namahero}!")
    else:
        print(f"\nPemenangnya adalah {H2.namahero}!")

    print("\n=== Show Stats ===")
    print(H1.status())
    print(H2.status())

print("=== Pertarungan Dimulai! ===")
battle(H1, H2)