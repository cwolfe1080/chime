import pyxel

# Define the game class
class App:
    def __init__(self):
        # 1. Initialize
        pyxel.init(160, 120, "Chime")

        # Load assets
        pyxel.load("assets.pyxres") 
        
        # Initialize a position variable for the sprite
        self.x = 10
        self.y = 10
        
        # 3. Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Handle game logic (e.g., movement)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        # Simple movement: move the sprite to the right
        self.x = (self.x + 1) % 160 

    def draw(self):
        # This function handles all rendering
        pyxel.cls(0)
        pyxel.text(50, 50, "chime", 9)

# Start the game
App()