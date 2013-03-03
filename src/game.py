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
import math
PCR = None

# various key codes and key state variables
# key names refer to direction, not actual key
KEYLEFT		= 65
KEYRIGHT	= 68
KEYUP		= 87
KEYDOWN		= 83

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
			# set modifiers for relative x and y location
			ds = (rightDown - leftDown) * 2
			df = (downDown - upDown) * 2
			
			mdx = (mouseX - self.x)
			mdy = (mouseY - self.y)
			
			if(mdx > 0):
				self.angle = math.atan(mdy / mdx) * -1
			elif(mdx < 0):
				self.angle = math.atan(mdy*-1 / mdx) + math.pi
			else:
				if(mdy < 0):
					self.angle = math.pi / 2
				elif(mdy > 0):
					self.angle = math.pi * 1.5
			
			# change actual x and y locations based on relative position modifiers
			# and angle
			self.x += math.cos(self.angle)*df
			self.y += math.sin(self.angle)*df
			
        def draw(self):
			PC.drawImageRotF(self.image, self.x - self.width * 0.5, self.y - self.height * 0.5,self.angle - math.pi / 2)

def loadBase():
	import PycapRes
	global PCR
	PCR = PycapRes

	# load image for the player, and set the player's width and height
	Player.image = PCR.loadImage("Res\\BetaMan.png")
	Player.width = PCR.imageWidth(Player.image)
	Player.height = PCR.imageHeight(Player.image)
	
	# load the game font
	global gameFont
	gameFont = PCR.loadFont("Res\\Fonts\\LCDSolid20.txt")
	
def init():
	# retrieve width and height values from appIni
	global screenWidth
	global screenHeight
	screenWidth = appIni["mWidth"]
	screenHeight = appIni["mHeight"]
		
	# initialize mouse position by calling mouseMove
	mouseMove(0, 100)
		
	# initialize the player
	global player
	player = Player(100, 100) 
	
	

def update( delta ):
	PC.markDirty()

	player.update(delta)

def draw():
	# set the game font
	PC.setFont(gameFont)
	
	# make a white screen to initialize the framebuffer
	PC.setColour(255, 255, 255, 255)
	PC.fillRect(0, 0, screenWidth, screenHeight);

	# draw the player
	player.draw()
	
	# display the player's angle for debugging purposes
	PC.setColour(0, 0, 0, 255)
	PC.drawString(str(player.angle), 5, 25)

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
		
def mouseMove(x, y):
	global mouseX
	global mouseY
	mouseX = x
	mouseY = y
