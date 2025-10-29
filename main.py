import pyxel

# All other functions

def load(file):
    pyxel.text(80, 100, "Loading...")
    pyxel.load(file)

# All Pyxel functions
class Title:
    def __init__(self):
        self.touchingPlay = False
        self.touchingQuit = False

    def update(self):
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y
        if self.mx > 42 and self.mx < 115 and self.my > 40 and self.my < 68:
            self.touchingPlay = True
        else:
            self.touchingPlay = False
        if self.mx > 42 and self.mx < 115 and self.my > 73 and self.my < 101 :
            self.touchingQuit = True
        else:
            self.touchingQuit = False
        if self.touchingPlay and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # put stuff here
            pass
        if self.touchingQuit and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()
        

    def draw(self):
        # pyxel.text(0, 0, "X: " + str(self.mx) + " Y: " + str(self.my), 2)
        pyxel.blt(60, 15, 0, 2, 0, 38, 8, None, None, 3)
        if self.touchingPlay:
            pyxel.blt(67, 50, 0, 24, 17, 24, 9, None, None, 3)
        else:    
            pyxel.blt(67, 50, 0, 0, 17, 24, 9, None, None, 3) # x is at 67 :D
        if self.touchingQuit:
            pyxel.blt(67, 83, 0, 24, 33, 24, 9, None, None, 3)
        else:
            pyxel.blt(67, 83, 0, 0, 33, 24, 9, None, None, 3)

class Game:
    def __init__(self):
        pyxel.init(160, 120, "chime", 60, pyxel.KEY_NONE)  
        # Load inital game assets
        pyxel.load("title.pyxres") 
        pyxel.colors[8] = 0x8B0000  # Dark red

        self.level = 0 # Initilize level
        self.title = Title() # Start title screen
        pyxel.mouse(True) # Show mouse cursor

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
            pass # Load file here
            
game = Game()
pyxel.run(game.update, game.draw)