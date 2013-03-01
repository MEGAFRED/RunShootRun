# Template pycap game v1.0
# Written by Farbs

appIni = {	"mCompanyName"		: "TBDCompany",
		"mFullCompanyName"	: "TBDCompany",
		"mProdName"		: "RunShootRun",
		"mProductVersion"	: "0.0.1",
		"mTitle"			: "RunShootRun Beta",
		"mRegKey"			: "RunShootRun",
		"mWidth"			: 800,
		"mHeight"			: 600,
		"mAutoEnable3D"	: 1,
		"mVSyncUpdates"	: 1 }

import Pycap as PC
PCR = None

# some temporary globals that refer to key data
KEYLEFT		= 37
KEYRIGHT	= 39
KEYUP		= 38
KEYDOWN		= 40

leftDown = 0
rightDown = 0
upDown = 0
downDown = 0

# player class
class Player:
        def __init__(self, x, y):
                # store variables x and y as initial location
                self.x = x
                self.y = y

        def update(self, delta):
                # change x and y positions based on whether keys are pressed
                dx = (rightDown - leftDown) * 2
                dy = (downDown - upDown) * 2

                self.x += dx * delta
                self.y += dy * delta

        def draw(self):
                PC.drawImageF(self.image, self.x - self.width * 0.5, self.y - self.height * 0.5)

def loadBase():
	import PycapRes
	global PCR
	PCR = PycapRes

	# load image for the player, and set the player's width and height
	Player.image = PCR.loadImage("Res\\BetaMan.png")
	Player.width = PCR.imageWidth(Player.image)
	Player.height = PCR.imageHeight(Player.image)

def init():
        # retrieve width and height values from appIni
        global screenWidth
        global screenHeight
        screenWidth = appIni["mWidth"]
        screenHeight = appIni["mHeight"]
        
        # initialize the player
	global player
	player = Player(100, 100)

def update( delta ):
	PC.markDirty()

	player.update(delta)

def draw():
        # make a white screen to initialize the framebuffer
        PC.setColour(255, 255, 255, 255)
        PC.fillRect(0, 0, screenWidth, screenHeight);

        #draw the player
        player.draw()

def keyDown(key):
        if key == KEYLEFT:
		global leftDown
		leftDown = 1
	elif key == KEYRIGHT:
		global rightDown
		rightDown = 1
	elif key == KEYUP:
		global upDown
		upDown = 1
	elif key == KEYDOWN:
		global downDown
		downDown = 1
	
	print key  

def keyUp(key):
        if key == KEYLEFT:
		global leftDown
		leftDown = 0
	elif key == KEYRIGHT:
		global rightDown
		rightDown = 0
	elif key == KEYUP:
		global upDown
		upDown = 0
	elif key == KEYDOWN:
		global downDown
		downDown = 0
