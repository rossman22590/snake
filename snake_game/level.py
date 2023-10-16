class Level:
    def __init__(self):
        self.difficulty: int = 1

    def set_difficulty(self, difficulty: int = 1) -> None:
        """
        Set the difficulty level of the game.

        Args:
            difficulty (int): The difficulty level of the game. Default is 1.
        """
        self.difficulty = difficulty
