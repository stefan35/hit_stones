class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (75, 210, 80)
        
        self.stones_drop_speed = 10
        
        self.rectangle_width = 3
        self.rectangle_height = 15
        self.rectangle_color = 60, 60, 60
        self.rectangles_allowed = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.stone_points = 50

        self.initializeDynamiSettings()


    def initializeDynamiSettings(self):
         self.player_speed = 1
         self.rectangle_speed = 0.75
         self.stone_speed = 0.1
         self.stones_direction = 1 # 1 right, -1 left
         #self.stone_points = int(self.stone_points  * self.score_scale)
    

    def increaseSpeed(self):
        self.player_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale
        self.stone_speed *= self.speedup_scale