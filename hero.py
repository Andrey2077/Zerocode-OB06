class Hero:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f"Герой по имени {self.name} атакует другого героя по имени: {other.name} и наносит урон в размере: {self.attack_power}")
        other.set_health(self.attack_power)

    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        print(f"У героя по имени: {self.name} осталось здоровья: {self.health}")

    def set_health(self, damage):
        self.health = self.health - damage