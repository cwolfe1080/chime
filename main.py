import pyxel

# Define the game class
class Title:
    def __init__(self):
        pass      

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        

    def draw(self):
        pyxel.text(50, 50, "chime", 9)

# Start the game
class Game:
    def __init__(self):
        pyxel.init(160, 120, "chime")  
        # Load inital game assets
        pyxel.load("title.pyxres") 

        self.level = 0 # Initilize level
        self.title = Title() # Start title screen

    def update(self):
        if self.level == 0:
            self.title.update()
        elif self.level == 1:
            if hasattr(self, "title"):
                del self.title
            # pyxel.load("next_level.pyxres")
    
    def draw(self):
        pyxel.cls(0)
        if self.level == 0:
            self.title.draw()
        elif self.level == 1:
            pyxel.text(80, 100, "Loading...")
            
game = Game()
pyxel.run(game.update, game.draw)