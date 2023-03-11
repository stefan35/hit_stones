class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (75, 210, 80)
        
        self.stones_drop_speed = 10
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.speedup_scale = 1.1
        self.stone_points = 50

        self.initializeDynamiSettings()


    def initializeDynamiSettings(self):
         self.player_speed = 1
         self.bullet_speed = 0.75
         self.stone_speed = 0.1
         self.stones_direction = 1 # 1 right, -1 left
    

    def increaseSpeed(self):
        self.player_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.stone_speed *= self.speedup_scale