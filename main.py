import pyxel

# All other functions

def setColors(file):
    if file == "title.pyxres":
        pyxel.colors[8] = 0x8B0000  # Dark red
    elif file == "story.pyxres":
        pyxel.colors[8] = 0x8B0000  # Dark red

# All Pyxel functions
class Title:
    def __init__(self, game):
        self.touchingPlay = False
        self.touchingQuit = False
        self.game = game

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
        if self.touchingQuit and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()
        if self.touchingPlay and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.game.level = 1
            
        

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

class Typewriter:
    def __init__(self, text, x, y, color, speed, wait_ms):
        self.full_text = text
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed  # frames per character
        self.counter = 0
        self.visible_chars = 0
        self.done_typing = False
        self.wait_frames = int((wait_ms / 1000) * 60)  # Convert ms to frames
        self.wait_counter = 0
        self.done = False  # True only after typing + wait

    def update(self):
        if not self.done_typing:
            self.counter += 1
            if self.counter % self.speed == 0:
                self.visible_chars += 1
                if self.visible_chars >= len(self.full_text):
                    self.visible_chars = len(self.full_text)
                    self.done_typing = True
        elif not self.done:
            self.wait_counter += 1
            if self.wait_counter >= self.wait_frames:
                self.done = True

    def draw(self):
        pyxel.text(self.x, self.y, self.full_text[:self.visible_chars], self.color)

class Story:
    def __init__(self, game):
        self.game = game
        self.scene = 0
        self.skip = False
    
    def update(self):
        if self.scene == 0:
            self.typewriter = Typewriter("Long ago, in an ancient land,\ncivilizations and kingdoms prospered.\nThere was peace in the land. Until,\nan ancient power of evil fell upon\nthe land, causing blight to appear\neverywhere. The blight consumed the\ncrops and vegetation, and rotted\nstructures, leaving many homeless and\nstarving.", 10, 10, 8, 4, 3000)
            self.scene = 1
        elif self.scene == 1:
            if pyxel.btnp(pyxel.KEY_SPACE) and not self.typewriter.done:
                self.typewriter.visible_chars = len(self.typewriter.full_text)
                self.typewriter.done_typing = True
                self.typewriter.wait_counter = 0
                self.typewriter.done = True
            self.typewriter.update()
            if self.typewriter.done:
                self.scene = 2
        elif self.scene == 2:
            self.typewriter = Typewriter("Life was difficult and food was near\nimpossible to find. One day, you\nleave your family at your crumbling\nhome and go searching for food. While\nhunting for deer, you fall into a\nsinkhole, and fall hundreds of\nfeet into the ground. You awake, in\nshallow water. You find that you're\nin a cave, with blight covering the\nwalls and consuming all living things.", 10, 10, 8, 4, 5000)
            self.scene = 3
        elif self.scene == 3:
            if pyxel.btnp(pyxel.KEY_SPACE) and not self.typewriter.done:
                self.typewriter.visible_chars = len(self.typewriter.full_text)
                self.typewriter.done_typing = True
                self.typewriter.wait_counter = 0
                self.typewriter.done = True
            self.typewriter.update()
            if self.typewriter.done:
                self.scene = 4
        elif self.scene == 4:
            self.game.level = 3


    def draw(self):
        if self.scene == 1:
            self.typewriter.draw()
            pyxel.text(43, 110, "Press space to skip", 8)
        if self.scene == 3:
            self.typewriter.draw()
            pyxel.text(43, 110, "Press space to skip", 8)




class Game:
    def __init__(self):
        pyxel.init(160, 120, "chime", 60, pyxel.KEY_NONE)  
        # Load inital game assets
        pyxel.load("title.pyxres") 
        setColors("title.pyxres")

        self.level = 0 # Initilize level
        self.title = Title(self) # Start title screen
        pyxel.mouse(True) # Show mouse cursor

    def update(self):
        if self.level == 0:
            self.title.update()
        elif self.level == 1:
            if hasattr(self, "title"):
                del self.title
            pyxel.load("story.pyxres")
            setColors("story.pyxres")
            self.story = Story(self)
            self.level = 2
        elif self.level == 2:
            self.story.update()
        elif self.level == 3:
            pass # start here
    
    def draw(self):
        pyxel.cls(0)
        if self.level == 0:
            self.title.draw()
        elif self.level == 1:
            pyxel.text(63, 55, "Loading...", 7)
        elif self.level == 2:
            self.story.draw()
        elif self.level == 3:
            pass # start here
            
game = Game()
pyxel.run(game.update, game.draw)