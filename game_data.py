class Game_data():
    def __init__(self):
        self.gold = 50
        self.upgrades = {
            'damage': {
                'lvl': 1,
                'cost': 5,
                'improv': 2
            },
            'attack speed': {
                'lvl': 1,
                'cost': 5,
                'improv': 0.02
            },
            'hp': {
                'lvl': 1,
                'cost': 5,
                'improv': 10
            },
            'regeneration': {
                'lvl': 1,
                'cost': 5,
                'improv': 0.02
            }
        }

    def add_gold(self, amount):
        self.gold += amount

    def sub_gold(self, amount):
        self.gold -= amount

    def upgrade(self, upgradable):
        if self.gold - self.upgrades[upgradable]['cost'] >= 0:
            self.sub_gold(self.upgrades[upgradable]['cost'])
            self.upgrades[upgradable]['lvl'] += 1
            self.upgrades[upgradable]['cost'] = int(
                self.upgrades[upgradable]['cost'] + (self.upgrades[upgradable]['lvl'] / 2)
            )
        else:
            print('cant afford it!, upgrade_menu, 123')

