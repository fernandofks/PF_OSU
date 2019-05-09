import pygame
from os import path

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), "snd")
fnt_dir = path.join(path.dirname(__file__), "font")

class Player(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the player, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(path.join(img_dir, "Pointer.png"))

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # Update the position of the player
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list, just like we'd fetch letters out
        # of a string.
        # NOTE: If you want to keep the mouse at the bottom of the screen, just
        # set y = 380, and not update it with the mouse position stored in
        # pos[1]
        x = pos[0]
        y = pos[1]

        # Set the attribute for the top left corner where this object is
        # located
        self.rect.x = x - 120
        self.rect.y = y - 120

pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #pygame.FULLSCREEN)

# Don't display the mouse pointer
pygame.mouse.set_visible(False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# This is a list of 'sprites.' Each sprite in the program (there is only 1) is
# added to this list. The list is managed by a class called 'Group.'
all_sprites_list = pygame.sprite.Group()

# This represents the ball controlled by the player
player = Player()
#screen.fill(BLACK)
# Add the ball to the list of player-controlled objects
all_sprites_list.add(player)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic
    all_sprites_list.update()

    #limpa a tela depois desenha
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(144)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
