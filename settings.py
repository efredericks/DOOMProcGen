import math

# screen info
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

# player info
PLAYER_POS = 1.5, 5 #mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
# PLAYER_SPEED = 0.002
# PLAYER_ROT_SPEED = 0.001
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

# map info
FLOOR_COLOR = (30,30,30)
NUM_ROWS = 100
NUM_COLS = 100
NOISE_ZOOM = 0.1

# raycasting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# drawing
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# textures
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

# utility functions
def p5Map(n, start1, stop1, start2, stop2):
  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2