class GameCharacter:
    def __init__(self, Char_name, char_health, char_power):
        self.name = Char_name
        self.health = char_health
        self.power = char_power

c1 = GameCharacter("Ajay", 100, "Jump")
c2 = GameCharacter("Vijay", 200, "Fire")

print(f'''\n
Character 1 ->
            Name    -> {c1.name}
            Health  -> {c1.health}
            Power   -> {c1.power}\n''')
print(f'''
Character 2 ->
            Name    -> {c2.name}
            Health  -> {c2.health}
            Power   -> {c2.power}\n''')