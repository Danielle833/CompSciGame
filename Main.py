import pygame, random
pygame.init()

displayDimensions = [1200, 650]
display = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption("Danielle's Diner")
clock = pygame.time.Clock()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
darkBrown = (71, 44, 0)
red = (112, 35, 35)
green = (35, 112, 55)


# Getting random positions for the bread
breadPosOne = [random.randint(800, 875), random.randint(240, 300)]
breadPosTwo = [random.randint(800, 875), random.randint(240, 300)]
if breadPosTwo[0] == breadPosOne[0]:
    breadPosTwo[0] = random.randint(800, 875)
if breadPosTwo[1] == breadPosOne[1]:
    breadPosTwo[1] = random.randint(240, 300)

# Making random orders
def makeOrder():
    menuItems = ["pancakes", "eggs", "bacon", "waffles", "juice", "toast"]

    order = []
    orderAmount = random.randint(1, 5)
    for x in range(orderAmount):
        order.append(menuItems[random.randint(0, (len(menuItems) - 1))])

    finalOrder = {}

    for item in range(len(order)):

        if order[item] == "pancakes":
            possiblePancakeToppings = ["blueberries", "strawberries", "banana", "chocolate-chips", "whipped-cream", "syrup"]
            pancakeToppings = []
            b = random.randint(1, len(possiblePancakeToppings))

            for i in range(b):
                currentTopping = random.randint(0, (len(possiblePancakeToppings)-1))
                pancakeToppings.append(possiblePancakeToppings[currentTopping])
                possiblePancakeToppings.pop(currentTopping)
            finalOrder["pancake"] = pancakeToppings

        elif order[item] == "eggs":
            possibleEggStyles = ["sunny-side-up", "scrambled", "omelette"]
            eggStyle = possibleEggStyles[random.randint(0, (len(possibleEggStyles)-1))]
            finalOrder["egg"] = eggStyle

        elif order[item] == "bacon":
            baconAmount = random.randint(1, 4)
            finalOrder["bacon"] = baconAmount

        elif order[item] == "waffles":
            waffleToppings = []
            possibleWaffleToppings = ["blueberries", "strawberries", "banana", "chocolate-chips", "whipped-cream", "syrup"]
            b = random.randint(1, len(possibleWaffleToppings))

            for i in range(b):
                currentTopping = random.randint(0, (len(possibleWaffleToppings)-1))
                waffleToppings.append(possibleWaffleToppings[currentTopping])
                possibleWaffleToppings.pop(currentTopping)
            finalOrder["waffle"] = waffleToppings

        elif order[item] == "juice":
            possibleJuiceTypes = ["apple-juice", "orange-juice", "cranberry-juice", "lemonade"]
            juiceType = possibleJuiceTypes[random.randint(0, (len(possibleJuiceTypes)-1))]
            finalOrder["juice"] = juiceType

        elif order[item] == "toast":
            possibleToastToppings = ["avocado", "butter", "jam", "peanut-butter"]
            possibleToastStrengths = ["light", "medium", "dark", "burnt"]
            toastStrength = possibleToastStrengths[random.randint(0, (len(possibleToastStrengths)-1))]
            toastTopping = possibleToastToppings[random.randint(0, (len(possibleToastToppings)-1))]
            finalOrder["toast"] = [toastTopping, toastStrength]

    return finalOrder


# Food item classes
class Pancakes:
    def __init__(self, toppings):
        self.toppings = toppings
        self.price = 13.50

class Eggs:
    def __init__(self, style):
        self.style = style
        self.price = 9.25

class Bacon:
    def __init__(self):
        self.cookedLevel = "raw"
        self.beingMoved = True
        self.displayImage = rawBacon
        self.displayPos = pos
        self.onPlate = False
        self.locked = False
        self.time = 0
        self.rect = self.displayImage.get_rect(topleft=self.displayPos)

    def move(self):
        if self.locked is False:
            self.displayPos = (pos[0]-10, pos[1]-10)
            self.rect.topleft = self.displayPos

    def getCooked(self):
        if self.time < 30:
            self.time += 0.07
        if 20 > self.time > 10:
            self.displayImage = halfCookedBacon
            self.cookedLevel = "half"
        elif 30 > self.time >= 20:
            self.displayImage = cookedBacon
            self.cookedLevel = "cooked"
        elif self.time >= 30:
            self.displayImage = burntBacon
            self.cookedLevel = "burnt"

    def updateDisplay(self):
        display.blit(self.displayImage, self.displayPos)

class Pan:
    def __init__(self, position, dimensions):
        self.rect = pygame.Rect(position, dimensions)
        self.slot1 = False
        self.slot2 = False
        self.slot3 = False
        self.slot4 = False


    def fillSlot(self):
        if self.slot1 is False:
            self.slot1 = True
            return 630, 394
        elif self.slot2 is False:
            self.slot2 = True
            return 658, 396
        elif self.slot3 is False:
            self.slot3 = True
            return 680, 403
        elif self.slot4 is False:
            self.slot4 = True
            return 704, 402

class Waffles:
    def __init__(self, toppings):
        self.toppings = toppings

# this class creates an empty glass that the player can interact with. It has the ability to be filled by one of the four sections of the juice machine through the "fillGlass" method, which checks the position of the glass and fills it with a specific juice based on the position. It can also be moved, and if it is found to be in a position it can't be (for example on the wall) it is returned to the correct position through the "changePosition" method.
class Juice:
    def __init__(self):
        self.type = "empty"
        self.filledLevel = "empty"
        self.emptyGlass = pygame.image.load("Images//Empty_Glass.png").convert_alpha()
        self.glassPos = [900, 225]
        self.glassRect = self.emptyGlass.get_rect(topleft=self.glassPos)
        self.displayImage = self.emptyGlass
        self.displayPosition = self.glassPos
        self.displayStart = False
        self.juiceTimer = 0
        self.imageNum = 0
        self.juiceType = []
        self.colourOne = (0, 0, 0)
        self.colourTwo = (0, 0, 0)
        self.juicePosOne = (0, 0)
        self.juicePosTwo = (0, 0)

    def fillGlass(self):
        if self.displayStart is False:
            if self.type == "apple juice":
                self.juiceType = appleImages
                self.juiceType.append(appleFull)
                self.colourOne = (241, 155, 32)
                self.colourTwo = (206, 179, 124)
                self.juicePosOne = [145.5, 278]
                self.juicePosTwo = [145.5, 339]
            elif self.type == "orange juice":
                self.juiceType = orangeImages
                self.juiceType.append(orangeFull)
                self.colourOne = (253, 181, 37)
                self.colourTwo = (210, 190, 130)
                self.juicePosOne = [305, 278]
                self.juicePosTwo = [305, 339]
            elif self.type == "lemonade":
                self.juiceType = lemonImages
                self.juiceType.append(lemonFull)
                self.colourOne = (255, 237, 104)
                self.colourTwo = (215, 224, 164)
                self.juicePosOne = [465, 278]
                self.juicePosTwo = [465, 339]
            else:
                self.juiceType = cranberryImages
                self.juiceType.append(cranberryFull)
                self.colourOne = (201, 55, 64)
                self.colourTwo = (181, 135, 149)
                self.juicePosOne = [623.85, 278]
                self.juicePosTwo = [623.85, 339]

            self.juiceTimer = pygame.time.get_ticks()
            self.displayStart = True

        if pygame.time.get_ticks() - self.juiceTimer > 450 and self.imageNum < 23:
            self.imageNum += 1
            self.juiceTimer = pygame.time.get_ticks()

        self.displayImage = self.juiceType[self.imageNum]

        if 0 <= self.imageNum <= 22:
            self.filledLevel = "filling"
        elif self.imageNum == 23:
            self.filledLevel = "full"

    def changePosition(self, position):
        self.displayPosition = position
        self.glassRect.topleft = position

    def moveGlass(self):
        self.glassRect.topleft = (pos[0]-60, pos[1]-60)
        self.displayPosition = self.glassRect.topleft

    def updateDisplay(self):
        display.blit(self.displayImage, self.displayPosition)

# This is the class that creates a piece of toast for the toaster section of my game. Each piece of toast can be moved by the player through the "moveBread" method. If placed in the toaster it can be toasted through the "getToasted" method, which changes the toast's sprite based on how long it's placed in the toaster. Toast also must be given a topping through the "haveTopping" method, which uses the topping that the player chooses to add a topping spread image to the toast sprite.
class Toast:
    def __init__(self, breadPos):
        self.cookedLevel = "none"
        self.breadPos = breadPos
        # Bread variables for functions
        self.breadClick = False
        self.progressLength = 0
        self.breadImage = pygame.image.load("Images//Bread.png").convert_alpha()
        self.breadRect = self.breadImage.get_rect()
        self.breadRect.topleft = self.breadPos
        self.position = None
        self.displayBar = False
        self.toasterPlaced = False
        self.gettingToasted = False
        self.doneToasting = False
        self.toppingStatus = "plain"
        self.toppingImage = None
        # Bread images
        self.halfBreadImage = pygame.image.load("Images//Half_Bread.png").convert_alpha()
        self.halfToastLight = pygame.image.load("Images//Half_Toast_Light.png").convert_alpha()
        self.halfToastMedium = pygame.image.load("Images//Half_Toast_Medium.png").convert_alpha()
        self.halfToastDark = pygame.image.load("Images//Half_Toast_Dark.png").convert_alpha()
        self.halfToastBurnt = pygame.image.load("Images//Half_Toast_Burnt.png").convert_alpha()

        # display positions
        self.displayImage = self.breadImage
        self.displayPosition = self.breadPos

    def moveBread(self):
        self.breadClick = True
        self.breadRect.topleft = (pos[0]-60, pos[1]-60)

    def getToasted(self, position):
        if self.displayBar:
            pygame.draw.rect(display, white, pygame.Rect(175.5, 312.999999999999971578290569595992565156, self.progressLength, 9.999999999999999111821702))

        if toasterLever == "down":
            self.displayBar = True
            if self.progressLength < 312:
                self.progressLength += 0.45

        if 78 <= self.progressLength < 154:
            self.cookedLevel = "light"
            return self.halfToastLight, position
        elif 154 <= self.progressLength < 236:
            self.cookedLevel = "medium"
            return self.halfToastMedium, position
        elif 236 <= self.progressLength < 311:
            self.cookedLevel = "dark"
            return self.halfToastDark, position
        elif 311 <= self.progressLength:
            self.cookedLevel = "burnt"
            return self.halfToastBurnt, position
        else:
            self.cookedLevel = "None"
            return self.halfBreadImage, position

    def haveTopping(self, topping):
        self.toppingStatus = topping
        self.toppingImage = toastToppingImages[topping]
        self.displayImage.blit(self.toppingImage, (25, 16))

    def updateDisplay(self):
        display.blit(self.displayImage, self.displayPosition)

# This is the class that makes the customer's order using the "makeOrder" function (which is not part of the class, it is at the beginning of the file). When displaying the order in the kitchen the "cleanOrder" method is used initially to put the order in the correct format for displaying, and then the "displayOrder" method is used to actually put it on the screen. When the player is submitting the order, the "evaluateOrder" method is used to both putting the text into the right formatting, displaying the order items on the screen, and scoring the items that the player made.
class CustomerOrder:
    def __init__(self):
        self.items = makeOrder()
        self.madeFood = []
        self.newMadeFood = []
        self.foodTypes = ["toast:", "egg:", "waffle:", "pancake:", "juice:", "bacon:"]
        self.colour = black
        self.text = pygame.font.Font("Retro Gaming.ttf", 23)
        self.scoreText = pygame.font.Font("Retro Gaming.ttf", 30)
        self.isSplit = False
        self.timer = 0
        self.displayingList = []
        self.listDone = False
        self.score = 0
        self.hasScored = []
        self.doneDisplaying = False

    def cleanOrder(self):
        orderItems = self.items
        orderItemsList = list(orderItems.items())
        formList = []

        for thing in orderItemsList:
            ingList = []
            for x in range(len(thing)):
                ingList.append(str(thing[x]))
            ingList.pop(0)
            if len(ingList) > 0:
                formList.append(f"{thing[0]}: {",".join(ingList)}")
            else:
                formList.append(f"{thing[0]}")

        charsToRemove = ["[", "]", "'", '"']

        for t in range(len(formList)):
            for x in range(len(charsToRemove)):
                formList[t] = formList[t].replace(charsToRemove[x], "")
            formList[t] = formList[t].replace("-", " ")
            formList[t] = formList[t].replace("n, ", "n")

        formList.insert(0, "ORDER:")
        self.items = formList
        return formList

    def displayOrder(self):
        yPos = 500
        maxLength = 0
        for f in range(len(self.items)):
            currentLength = len(self.items[f])
            if currentLength >= maxLength:
                maxLength = currentLength

        orderDisplay = pygame.Surface((((maxLength + 1.255) * 12.4), 26.25 * len(self.items) + 10), pygame.SRCALPHA)
        orderDisplay.fill((255, 255, 255, 200))
        display.blit(orderDisplay, (25, 495))

        for f in range(len(self.items)):
            orderSurface = orderFont.render(str(self.items[f]), False, black)
            orderRect = orderSurface.get_rect(topleft=(35, yPos))
            display.blit(orderSurface, orderRect)
            yPos += 25

    def evaluateOrder(self):
        # Adjusting the text formatting
        if self.isSplit is False:
            if self.items[0] == "ORDER:":
                del self.items[0]

            for num in range(len(self.items)):
                if ":" in self.items[num]:
                    self.items[num] = self.items[num].replace(":", ":,")
                    self.items[num] = self.items[num].split(", ")
                    self.isSplit = True

        if self.listDone is False:
            for num in range(len(self.items)):
                for item in range(len(self.items[num])):
                    self.displayingList.append(self.items[num][item])

            for x in range(len(self.madeFood)):
                for i in range(len(self.madeFood[x])):
                    self.newMadeFood.append(self.madeFood[x][i])

            self.listDone = True

        posX = 250
        posY = 130


        while len(self.hasScored) < len(self.displayingList):
            self.hasScored.append(False)

        for num in range(len(self.displayingList)):
            # displaying the food item/topping:
            if self.displayingList[num] in self.foodTypes and posX != 250 and posX != 650:
                posX -= 25
            elif posX != 275 and posX != 675 and ":" not in self.displayingList[num]:
                posX += 25

            if self.displayingList[num] in self.newMadeFood:
                self.colour = green
            else:
                self.colour = red


            if posY >= 475:
                posX += 400
                posY = 130

            evaluateSurface = self.text.render(self.displayingList[num], False, self.colour)
            evaluateRect = evaluateSurface.get_rect(topleft=(posX, posY))
            if num <= self.timer:
                display.blit(evaluateSurface, evaluateRect)

            posY += 35


            # Updating the score:
            if self.colour == green and self.hasScored[num] is False:
                if ":" in self.displayingList[num]:
                    self.score += 50
                else:
                    self.score += 100
                self.hasScored[num] = True

            scoreSurface = self.scoreText.render(f"SCORE: {str(self.score)}", False, darkBrown)
            scoreRect = scoreSurface.get_rect(topleft=(750, 493))
            display.blit(scoreSurface, scoreRect)

            self.timer += 0.0095

        if self.timer > (len(self.displayingList) + 2.5):
            self.doneDisplaying = True

# The topping parent class is used for all topping types, but is never used on its own.
class Topping:
    def __init__(self, image, position):
        self.image = image
        self.position = position

    def updateDisplay(self):
        display.blit(self.image, self.position)

# The Jar class is used for all the toast-related toppings like butter, peanut butter, etc. The unique feature of jars is that they can be used up, so after a certain amount of clicks they will change their image (become darker), and be unable to be used.
class Jar(Topping):
    def __init__(self, image, position, imageTwo):
        super().__init__(image, position)
        self.imageTwo = imageTwo
        self.rect = self.image.get_rect(topleft=position)
        self.clickCounter = 0

    def usedUp(self):
        self.clickCounter += 1
        if self.clickCounter >= 2:
            self.image = self.imageTwo

class Bottle(Topping):
    def __init__(self, image, position, drizzle):
        super().__init__(image, position)
        self.drizzle = drizzle
        self.imageUpsidedown = pygame.transform.rotate(self.image, 180)

# The knife class creates a utensil that is used during the toast topping section. It can be interacted with through being moved, and can be given a "status", and the "updateImage" method will change its sprite based on the status. This will show which topping it has on it. The knife is used to apply toppings to toast objects.
class Knife:
    def __init__(self):
        self.status = "plain"
        self.image = knifeImages[self.status]
        self.startingPoint = (570, 260)
        self.position = self.startingPoint
        self.rect = self.image.get_rect(topleft=self.position)
        self.starting = True
        self.onMouse = False

    def updatePosition(self):
        self.position = (pos[0] - 15, pos[1] - 15)

    def updateImage(self):
        self.image = knifeImages[self.status]

    def updateDisplay(self):
        display.blit(self.image, self.position)

# The button class creates button that the player can interact with to take them between screens. The main buttons that are created are arrows, but it is also a parent class for text buttons.
class Button:
    def __init__(self, image, position):
        self.image = image.copy()
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def checkClick(self):
        if secondClick and self.rect.collidepoint(pos):
            return True
        else:
            return False

    def updateDisplay(self):
        display.blit(self.image, self.position)

# This class is a child class of Button. Its only difference is that in takes in a text attribute that will be displayed centered on the button image. These buttons are used when the player is submitting their order to be evaluated.
class TextButton(Button):
    def __init__(self, image, position, text):
        super().__init__(image, position)
        self.text = text
        self.textFont = pygame.font.Font("Retro Gaming.ttf", 30)
        self.textSurface = self.textFont.render(self.text, False, darkBrown)
        self.textRect = self.textSurface.get_rect(center=(192.5, 55.5))
        self.rect = self.image.get_rect(topleft=self.position)
        self.image.blit(self.textSurface, self.textRect)



# Images & variables
mainBackground = pygame.image.load("Images//Main_Background.png").convert_alpha()
toppingsBackground = pygame.image.load("Images//Toppings_Background.png").convert_alpha()
menuBackground = pygame.image.load("Images//Menu_Background.png").convert_alpha()

# toaster images
toasterBackground = pygame.image.load("Images//Toaster_Background.png").convert_alpha()
toasterLeverImage = pygame.image.load("Images//Toaster_Lever.png").convert_alpha()

toasterLeverX = 561.999999999
toasterLeverY = 264
toasterLeverRect = toasterLeverImage.get_rect(topleft=(toasterLeverX, toasterLeverY))

# topping images
avocadoOneFull = pygame.image.load("Images//Avocado_One_Full.png").convert_alpha()
avocadoOneEmpty = pygame.image.load("Images//Avocado_One_Empty.png").convert_alpha()
avocadoTwoFull = pygame.image.load("Images//Avocado_Two_Full.png").convert_alpha()
avocadoTwoEmpty = pygame.image.load("Images//Avocado_Two_Empty.png").convert_alpha()

peanutButterJarFull = pygame.image.load("Images//Peanutbutter_Full.png").convert_alpha()
peanutButterJarEmpty = pygame.image.load("Images//Peanutbutter_Empty.png").convert_alpha()

jamJarFull = pygame.image.load("Images//Jam_Full.png").convert_alpha()
jamJarEmpty = pygame.image.load("Images//Jam_Empty.png").convert_alpha()

butterJarFull = pygame.image.load("Images//Butter_Full.png").convert_alpha()
butterJarEmpty = pygame.image.load("Images//Butter_Empty.png").convert_alpha()

toastToppingImages = {
    "avocado": pygame.image.load("Images//Avocado_Spread.png").convert_alpha(),
    "peanut butter": pygame.image.load("Images//Peanut_Butter_Spread.png").convert_alpha(),
    "jam": pygame.image.load("Images//Jam_Spread.png").convert_alpha(),
    "butter": pygame.image.load("Images//Butter_Spread.png").convert_alpha()
}


# Drink Machine Images
drinkMachineBackground = pygame.image.load("Images//Drink_Machine_Background.png").convert_alpha()

appleImages = [pygame.image.load(f"Images//Apple_Juice//Apple_{i}.png").convert_alpha() for i in range(1, 24)]
appleFull = pygame.image.load("Images//Apple_Juice//Apple_Full.png").convert_alpha()
orangeImages = [pygame.image.load(f"Images//Orange_Juice//Orange_{i}.png").convert_alpha() for i in range(1, 24)]
orangeFull = pygame.image.load("Images//Orange_Juice//Orange_Full.png").convert_alpha()
lemonImages = [pygame.image.load(f"Images//Lemonade//Lemon_{i}.png").convert_alpha() for i in range(1, 24)]
lemonFull = pygame.image.load("Images//Lemonade//Lemon_Full.png").convert_alpha()
cranberryImages = [pygame.image.load(f"Images//Cranberry_Juice//Cranberry_{i}.png").convert_alpha() for i in range(1, 24)]
cranberryFull = pygame.image.load("Images//Cranberry_Juice//Cranberry_Full.png").convert_alpha()

# Stove Images
stoveBackground = pygame.image.load("Images//Stove_Background.png").convert_alpha()
eggs = pygame.image.load("Images//Egg.png").convert_alpha()
baconTray = pygame.image.load("Images//Raw_Bacon.png").convert_alpha()
baconTrayRect = baconTray.get_rect(topleft=(850, 260))
rawBacon = pygame.image.load("Images//Raw_Bacon_Piece.png").convert_alpha()
cookedBacon = pygame.image.load("Images//Cooked_Bacon.png").convert_alpha()
halfCookedBacon = pygame.image.load("Images//Half_Bacon.png").convert_alpha()
burntBacon = pygame.image.load("Images//Burnt_Bacon.png").convert_alpha()
plate = pygame.image.load("Images//Plate.png").convert_alpha()
plateRect = plate.get_rect(topleft=(870, 170))


# other
backArrow = pygame.image.load("Images//Arrow.png").convert_alpha()
forwardArrow = pygame.transform.rotate(pygame.image.load("Images//Arrow.png").convert_alpha(), 180)
menuButton = pygame.image.load("Images//Button_Background.png").convert_alpha()

goBackwardsArrow = Button(backArrow, (20, 20))
goForwardsArrow = Button(forwardArrow, (1105, 20))
proceedButton = TextButton(menuButton, (407.5, 280), "Continue")
goBackButton = TextButton(menuButton, (407.5, 405), "Return")
newGameButton = TextButton(menuButton, (407.5, 190), "New Game")
quitButton = TextButton(menuButton, (407.5, 345), "Quit")
baconArrow = Button(forwardArrow, (1120, 285))


# Font
orderFont = pygame.font.Font("Retro Gaming.ttf", 18)


# Random variables
stoveRectangle = pygame.Rect(305, 365, 400, 275)
toasterRectangle = pygame.Rect(770, 315, 115, 75)
drinksRectangle = pygame.Rect(46, 228, 222, 165)
waffleRectangle = pygame.Rect(993, 258, 107, 133)



click = False
secondClick = False
mainMenu = True
order = False
orderNum = 1
myOrder = None

toaster = False
drinkMachine = False
stove = False
waffleIron = False
sendingOrder = False

# toasting variables:
toastCookingStation = True
toastToppingStation = False
toastOne = Toast(breadPosOne)
toastTwo = Toast(breadPosTwo)
toastList = [toastOne, toastTwo]
toasterSlotTwo = (258, 159)
toasterSlotOne = (258, 194)

toastOneCookedImages = {
    "none": pygame.image.load("images\\Bread.png").copy(),
    "light": pygame.image.load("Images\\Light_Toast.png").copy(),
    "medium": pygame.image.load("Images\\Medium_Toast.png").copy(),
    "dark": pygame.image.load("Images\\Dark_Toast.png").copy(),
    "burnt": pygame.image.load("Images\\Burnt_Toast.png").copy()
}
toastTwoCookedImages = {
    "none": pygame.image.load("images\\Bread.png").copy(),
    "light": pygame.image.load("Images\\Light_Toast.png").copy(),
    "medium": pygame.image.load("Images\\Medium_Toast.png").copy(),
    "dark": pygame.image.load("Images\\Dark_Toast.png").copy(),
    "burnt": pygame.image.load("Images\\Burnt_Toast.png").copy()
}

toastCookedHalfImages = {
    "none": pygame.image.load("Images\\Half_Bread.png"),
    "light": pygame.image.load("Images\\Half_Toast_Light.png"),
    "medium": pygame.image.load("Images\\Half_Toast_Medium.png"),
    "dark": pygame.image.load("Images\\Half_Toast_Dark.png"),
    "burnt": pygame.image.load("Images\\Half_Toast_Burnt.png")
}

toasterSlotCounter = 1
toasterLever = "up"
bothDoneToasting = False

# toast topping variables:
avocadoOne = Jar(avocadoOneFull, (490, 270), avocadoOneEmpty)
avocadoTwo = Jar(avocadoTwoFull, (415, 270), avocadoTwoEmpty)
peanutButter = Jar(peanutButterJarFull, (320, 260), peanutButterJarEmpty)
jam = Jar(jamJarFull, (220, 260), jamJarEmpty)
butter = Jar(butterJarFull, (120, 260), butterJarEmpty)
toastToppingList = [avocadoOne.rect, avocadoTwo.rect, peanutButter.rect, jam.rect, butter.rect]

knifeImages = {
    "plain": pygame.image.load("Images//Plain_Knife.png").convert_alpha(),
    "avocado": pygame.image.load("Images//Avocado_Knife.png").convert_alpha(),
    "peanut butter": pygame.image.load("Images//Peanut_Butter_Knife.png").convert_alpha(),
    "jam": pygame.image.load("Images//Jam_Knife.png").convert_alpha(),
    "butter": pygame.image.load("Images//Butter_Knife.png").convert_alpha()
}
toastKnife = Knife()


# drink machine variables
drink = Juice()
appleButton = pygame.Rect((145, 229), (20, 20))
orangeButton = pygame.Rect((305, 229), (20, 20))
lemonButton = pygame.Rect((465, 229), (20, 20))
cranberryButton = pygame.Rect((625, 229), (20, 20))


# Stove variables
baconTrayCheck = False
eggCheck = False
baconMouse = False
panOneRect = pygame.Rect(622, 395, 130, 75)
panOne = Pan((622, 395), (130, 75))
baconList = []
baconArrowCheck = False
onPlate = False


# sending order variables
questioningSendingOrder = True
actuallySendingOrder = False
questioningText = pygame.font.Font("Retro Gaming.ttf", 32)
questioningSurface = questioningText.render("Do you want to submit the order?", False, darkBrown)
questioningRect = questioningSurface.get_rect(center=(600, 200))


# Game Loop
run = True

while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            secondClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    # Getting this game's random order
    if order is False:
        myOrder = CustomerOrder()
        myOrder.cleanOrder()
        order = True


    # Main menu
    elif mainMenu:
        display.blit(mainBackground, (0, 0))

        # Toaster section
        if toasterRectangle.collidepoint(pos) and click:
            mainMenu = False
            toaster = True

        # Stove section
        elif stoveRectangle.collidepoint(pos) and click:
            mainMenu = False
            stove = True

        # Drinks section
        elif drinksRectangle.collidepoint(pos) and click:
            mainMenu = False
            drinkMachine = True

        # Waffle section
        elif waffleRectangle.collidepoint(pos) and click:
            mainMenu = False
            waffleIron = True


    # Toaster section
    if toaster:

        if toastCookingStation:
            display.blit(toasterBackground, (0, 0))
            display.blit(toasterLeverImage, (toasterLeverX, toasterLeverY))

            # This checks if the bread is being selected, and if so it calls the move function
            if toastOne.breadRect.collidepoint(pos) and click and toastOne.gettingToasted is False:
                toastOne.moveBread()
                toastOne.displayImage = toastOneCookedImages[toastOne.cookedLevel]
                toastOne.displayPosition = toastOne.breadRect
                if toastOne.toasterPlaced is True:
                    toasterSlotCounter -= 1
                toastOne.toasterPlaced = False
            elif toastTwo.breadRect.collidepoint(pos) and click and toastTwo.breadRect.collidepoint(pos) != toastOne.breadRect.collidepoint(pos) and toastTwo.gettingToasted is False:
                toastTwo.moveBread()
                toastTwo.displayImage = toastTwoCookedImages[toastTwo.cookedLevel]
                toastTwo.displayPosition = toastTwo.breadRect
                if toastTwo.toasterPlaced is True:
                    toasterSlotCounter -= 1
                toastTwo.toasterPlaced = False


            # This for loop checks if each piece has been moved and where the position is, so it knows whether to move the toast back to the plate or if it's in the toaster
            for piece in toastList:
                if click is False and piece.breadRect[0] < 127 or piece.breadRect[0] > 527:
                    if piece.breadRect[1] < 180 or piece.breadRect[1] > 260:
                        piece.breadClick = False
                        piece.breadRect.topleft = piece.breadPos
                        piece.displayPosition = piece.breadPos
                        if piece.toasterPlaced is True:
                            toasterSlotCounter -= 1
                            piece.toasterPlaced = False

                elif click is False and 127 <= piece.breadRect[0] <= 527:
                    piece.breadClick = False
                    if toasterSlotCounter == 1 and piece.toasterPlaced is False:
                        piece.toasterPlaced = True
                        toasterSlotCounter += 1
                        piece.position = toasterSlotTwo
                        piece.breadRect.topleft = toasterSlotTwo
                        piece.displayPosition = toasterSlotTwo

                    elif toasterSlotCounter == 2 and piece.toasterPlaced is False:
                        piece.position = toasterSlotOne
                        piece.toasterPlaced = True
                        toasterSlotCounter += 1
                        piece.breadRect.topleft = toasterSlotOne
                        piece.displayPosition = toasterSlotOne

                if piece.toasterPlaced is True:
                    piece.breadClick = False
                    piece.displayImage = toastCookedHalfImages[piece.cookedLevel.lower()]

            # Checking the position of the toaster lever
            if toasterLeverRect.collidepoint((pos[0], pos[1])) and click:
                if 264 <= pos[1] <= 315:
                    toasterLeverY = pos[1]
                    toasterLever = "middle"
                elif pos[1] < 260:
                    toasterLever = "up"
                elif pos[1] > 315:
                    toasterLeverY = 315
                    toasterLever = "down"

            # Actually toasting the toast
            if toasterSlotCounter == 3:
                a = toastTwo.getToasted(toasterSlotTwo)
                c = toastOne.getToasted(toasterSlotOne)
                toastTwo.displayImage = a[0]
                toastOne.displayImage = c[0]

                if toasterLever == "down":
                    toastOne.gettingToasted = True
                    toastTwo.gettingToasted = True
                    toastTwo.displayPosition = a[1]
                    toastOne.displayPosition = c[1]
                else:
                    toastOne.gettingToasted = False
                    toastTwo.gettingToasted = False

                for piece in toastList:
                    if piece.breadRect.collidepoint(pos) and click and toasterLever != "down":
                        piece.gettingToasted = False
                        if piece == toastOne:
                            piece.displayImage = toastOneCookedImages[piece.cookedLevel]
                        if piece == toastTwo:
                            piece.displayImage = toastTwoCookedImages[piece.cookedLevel]

            for piece in toastList:
                if piece.cookedLevel != "none" and 750 <= piece.breadRect[0] <= 1065 and 220 <= piece.breadRect[1] <= 460:
                    piece.doneToasting = True


            if toastOne.doneToasting and toastTwo.doneToasting:
                goForwardsArrow.updateDisplay()
                if goForwardsArrow.checkClick():
                    toastToppingStation = True
                    display.blit(toppingsBackground, (0, 0))
                    toastCookingStation = False


            # Displaying the toaster cooked level bar:
            if toastOne.progressLength >= 20:
                pygame.draw.rect(display, white, pygame.Rect(175.5, 312.999999999999971578290569595992565156, toastOne.progressLength, 9.999999999999999111821702))

        elif toastToppingStation:
            display.blit(toppingsBackground, (0, 0))
            avocadoOne.updateDisplay()
            avocadoTwo.updateDisplay()
            peanutButter.updateDisplay()
            jam.updateDisplay()
            butter.updateDisplay()

            # For moving the toast
            if toastOne.breadRect.collidepoint(pos) and click and toastKnife.onMouse is False:
                toastOne.moveBread()
                toastOne.displayImage = toastOneCookedImages[toastOne.cookedLevel]
                toastOne.displayPosition = toastOne.breadRect
            elif toastTwo.breadRect.collidepoint(pos) and click and toastTwo.breadRect.collidepoint(pos) != toastOne.breadRect.collidepoint(pos) and toastKnife.onMouse is False:
                toastTwo.moveBread()
                toastTwo.displayImage = toastTwoCookedImages[toastTwo.cookedLevel]
                toastTwo.displayPosition = toastTwo.breadRect

            # Checking the position of the toast to ensure it stays on the plate
            for piece in toastList:
                if click is False and piece.breadRect[0] < 127 or piece.breadRect[0] > 527:
                    if piece.breadRect[1] < 180 or piece.breadRect[1] > 260:
                        piece.breadClick = False
                        piece.breadRect.topleft = piece.breadPos
                        piece.displayPosition = piece.breadPos

            # Picking up the knife
            if toastKnife.rect.collidepoint(pos) and click:
                for thing in toastToppingList:
                    if thing.collidepoint(pos) is False:
                        toastKnife.onMouse = not toastKnife.onMouse

            # Updating the position of the knife to be on the mouse, and changing the knife image to have a topping if the player clicks on one of the jars or the avocado
            if toastKnife.onMouse:
                toastKnife.updatePosition()
                if secondClick:
                    if avocadoOne.rect.collidepoint(pos) and avocadoOne.clickCounter <= 1:
                        toastKnife.status = "avocado"
                        avocadoOne.usedUp()
                    elif avocadoTwo.rect.collidepoint(pos) and avocadoTwo.clickCounter <= 1:
                        toastKnife.status = "avocado"
                        avocadoTwo.usedUp()
                    elif peanutButter.rect.collidepoint(pos) and peanutButter.clickCounter < 2:
                        toastKnife.status = "peanut butter"
                        peanutButter.usedUp()
                    elif jam.rect.collidepoint(pos) and jam.clickCounter < 2:
                        toastKnife.status = "jam"
                        jam.usedUp()
                    elif butter.rect.collidepoint(pos) and butter.clickCounter < 2:
                        toastKnife.status = "butter"
                        butter.usedUp()

                    toastKnife.updateImage()

            # Putting toppings on the toast if the knife has a topping on it and clicks on the toast
            if toastOne.breadRect.collidepoint(pos) and click and toastKnife.status != "plain" and toastKnife.onMouse:
                toastOne.haveTopping(toastKnife.status)
                toastKnife.status = "plain"
                toastKnife.image = knifeImages["plain"]
            elif toastTwo.breadRect.collidepoint(pos) and toastOne.breadRect.collidepoint(pos) is False and click and toastKnife.status != "plain" and toastKnife.onMouse:
                toastTwo.haveTopping(toastKnife.status)
                toastKnife.status = "plain"
                toastKnife.image = knifeImages["plain"]

            # Displaying the 'go forward' arrow only if both pieces of toast have toppings
            if toastOne.toppingStatus != "plain" and toastTwo.toppingStatus != "plain":
                goForwardsArrow.updateDisplay()
                if goForwardsArrow.checkClick() and toastKnife.onMouse is False:
                    myOrder.madeFood.append(["toast:", toastOne.toppingStatus, toastOne.cookedLevel])
                    mainMenu = True
                    toaster = False


        # displaying the two pieces of toast
        if toastTwo.displayPosition == toasterSlotOne:
            toastOne.updateDisplay()
            toastTwo.updateDisplay()
        else:
            toastTwo.updateDisplay()
            toastOne.updateDisplay()

        # Displaying the knife (it's done down here so that it's displayed above the pieces of toast)
        if toastToppingStation:
            toastKnife.updateDisplay()


    # Stove section
    elif stove:
        display.blit(stoveBackground, (0, 0))
        display.blit(backArrow, (20, 20))
        if baconTrayCheck is False:
            display.blit(baconTray, (850, 260))
        elif baconTrayCheck:
            display.blit(plate, (870, 170))
        if eggCheck is False:
            display.blit(eggs, (0, 0))

        if baconTrayRect.collidepoint(pos) and secondClick and baconMouse is False and len(baconList) <= 3 and baconTrayCheck is False:
            baconList.append(Bacon())
            baconMouse = True

        for piece in baconList:
            if baconMouse is True:
                if secondClick and panOne.rect.collidepoint(pos) and piece.locked is False:
                    piece.displayPos = panOne.fillSlot()
                    piece.rect.topleft = piece.displayPos
                    piece.locked = True
                    baconMouse = False
                else:
                    piece.move()
            elif baconMouse is False:
                if piece.cookedLevel == "cooked" or piece.cookedLevel == "burnt":
                    if click and piece.rect.collidepoint(pos) and baconMouse is False:
                        piece.locked = False
                        baconMouse = True
                        piece.move()

            if piece.locked is True and piece.onPlate is False:
                piece.getCooked()

        for piece in baconList:
            if piece.cookedLevel == "cooked" or piece.cookedLevel == "burnt":
                if click and baconMouse and plateRect.collidepoint(pos):
                    piece.onPlate = True
                    piece.locked = True
                    onPlate = True
                    baconMouse = False

            piece.updateDisplay()


        if panOne.slot1 is True:
            if baconArrowCheck is False:
                baconArrow.updateDisplay()
            if baconArrow.checkClick():
                baconArrowCheck = True
                baconTrayCheck = True

        if onPlate is True:
            goForwardsArrow.updateDisplay()
            if goForwardsArrow.checkClick():
                print(len(baconList))
                myOrder.madeFood.append(["bacon:", str(len(baconList))])
                mainMenu = True
                stove = False


    # Drinks section
    elif drinkMachine:
        display.blit(drinkMachineBackground, (0, 0))
        display.blit(backArrow, (20, 20))

        if click and drink.glassRect.collidepoint(pos):
            drink.moveGlass()


        # Checking the position of the glass and moving it either back to the starting point if it's placed in an incorrect spot, or into one of the four slots on the machine
        if drink.glassRect.topleft[1] < 256 and 77 < drink.glassRect.topleft[0] < 714 and click is False:
            drink.changePosition([900, 225])
            if drink.filledLevel == "empty":
                drink.type = "empty"
        elif drink.glassRect.topleft[1] < 10 and click is False:
            drink.changePosition([900, 225])
            if drink.filledLevel == "empty":
                drink.type = "empty"
        elif 275 < drink.glassRect.topleft[1] < 356 and click is False:
            if 84 < drink.glassRect.topleft[0] < 178:
                if drink.filledLevel == "empty":
                    drink.type = "apple juice"
                drink.changePosition([93.5, 283])
            elif 245 < drink.glassRect.topleft[0] < 347:
                if drink.filledLevel == "empty":
                    drink.type = "orange juice"
                drink.changePosition([252, 283])
            elif 405 < drink.glassRect.topleft[0] < 508:
                if drink.filledLevel == "empty":
                    drink.type = "lemonade"
                drink.changePosition([413, 283])
            elif 570 < drink.glassRect.topleft[0] < 660:
                if drink.filledLevel == "empty":
                    drink.type = "cranberry juice"
                drink.changePosition([572, 283])
            else:
                drink.changePosition([900, 225])
                if drink.filledLevel == "empty":
                    drink.type = "empty"

        # Filling the glass with the right kind of juice (based on the glass' position)
        if drink.type == "apple juice" and appleButton.collidepoint(pos) and click and drink.filledLevel != "full":
            drink.fillGlass()
        elif drink.type == "orange juice" and orangeButton.collidepoint(pos) and click and drink.filledLevel != "full":
            drink.fillGlass()
        elif drink.type == "lemonade" and lemonButton.collidepoint(pos) and click and drink.filledLevel != "full":
            drink.fillGlass()
        elif drink.type == "cranberry juice" and cranberryButton.collidepoint(pos) and click and drink.filledLevel != "full":
            drink.fillGlass()

        drink.updateDisplay()

        # Displaying the rectangles that show the glass is filling
        if drink.filledLevel == "filling" and click:
            if appleButton.collidepoint(pos) or orangeButton.collidepoint(pos) or lemonButton.collidepoint(pos) or cranberryButton.collidepoint(pos):
                pygame.draw.rect(display, drink.colourOne, pygame.Rect(drink.juicePosOne, (23, 46)))
                pygame.draw.rect(display, drink.colourTwo, pygame.Rect(drink.juicePosTwo, (23, 109)))

        # Displaying the arrow
        elif drink.filledLevel == "full":
            goForwardsArrow.updateDisplay()
            if goForwardsArrow.checkClick():
                myOrder.madeFood.append(["juice:", drink.type])
                mainMenu = True
                drinkMachine = False


    # Waffle section
    elif waffleIron:
        display.fill(black)
        display.blit(backArrow, (20, 20))

    # Displaying the arrow
    if len(myOrder.madeFood) != 0 and mainMenu:
        goForwardsArrow.updateDisplay()
        if goForwardsArrow.checkClick():
            sendingOrder = True
            mainMenu = False

    if sendingOrder is False:
        myOrder.displayOrder()

    # Sending the player's order to the customer
    if sendingOrder:
        display.blit(menuBackground, (0, 0))
        if questioningSendingOrder:
            display.blit(questioningSurface, questioningRect)
            proceedButton.updateDisplay()
            goBackButton.updateDisplay()

            if proceedButton.checkClick():
                actuallySendingOrder = True
                questioningSendingOrder = False
            elif goBackButton.checkClick():
                mainMenu = True
                sendingOrder = False

        elif actuallySendingOrder:
            myOrder.evaluateOrder()

            if myOrder.doneDisplaying:
                newGameButton.updateDisplay()
                quitButton.updateDisplay()

                if newGameButton.checkClick():
                    del myOrder
                    order = False
                    mainMenu = True
                    sendingOrder = False
                elif quitButton.checkClick():
                    pygame.quit()


    if mainMenu is False and sendingOrder is False:
        goBackwardsArrow.updateDisplay()
        if goBackwardsArrow.checkClick():
            mainMenu = True
            toaster = False
            stove = False
            drinkMachine = False
            waffleIron = False


    secondClick = False
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
