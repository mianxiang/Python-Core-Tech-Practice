import yaml
from yaml.loader import Loader

class Monster(yaml.YAMLObject):
    yaml_tag = '!Monster'
    def __init__(self, name, hp, ac, attacks):
        super().__init__()
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks
    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % ( self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)
    def print(self):
        print("hello, i am {}".format(self.__class__.__name__))

testObject = yaml.load("""
--- !Monster
name: Cave spider
hp: [2, 6]
ac: 16
attacks: [BITE, HURT]
""", Loader)

print(type(testObject))
testObject.print()

testobject2 = Monster(name="hz", hp=[100, 99], ac=29, attacks=['Bear', 'dog'])
print(yaml.dump(testobject2))