class GameStats():
    
    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        
        with open('stats\high_score.txt') as f:
            self.high_score = int(f.readline())

        self.resetStats()
    

    def resetStats(self):
        self.player_left = 3
        self.score = 0
        self.level = 1
