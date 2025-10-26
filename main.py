import pyxel

# Define the game class
class App:
    def __init__(self):
        # 1. Initialize the screen (160x120 pixels)
        pyxel.init(160, 120, "Smiley Game")

        # 2. Load your assets file
        # 🟢 CORRECTED LINE: Pass the filename string as the first argument
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
        pyxel.cls(0) # Clear the screen to color 0 (black)
        
        # Draw a sprite: 
        # (x-pos, y-pos, Image Bank 0, u-coord, v-coord, width, height)
        # u=0, v=0 means the top-left 8x8 pixels in the Image Bank 0
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8) 

# Start the game
App()