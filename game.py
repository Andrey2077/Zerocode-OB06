class Game:
    def __init__(self):
        self.human_player = None
        self.computer_player = None

    def start(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

        print("Игра началась. Погнали!")

        while True:
            self.human_player.attack(computer_player)
            self.computer_player.get_health()

            if not computer_player.is_alive():
                print(f"Герой по имени: {computer_player.name} погиб. Игра окончена. Победил: {human_player.name}")
                break

            self.computer_player.attack(human_player)
            self.human_player.get_health()
            if not human_player.is_alive():
                print(f"Герой по имени: {human_player.name} погиб. Игра окончена. Победил: {computer_player.name}")
                break

