import copy


class Player:
    '''
    name
    place
    items
    '''

    def __init__(self, newName, newPlace, newItems) -> None:
        self.name = newName
        self.place = newPlace
        self.items = newItems

    def __str__(self) -> str:
        return str(self.name)


class Item:
    '''
    name
    '''

    def __init__(self, newName) -> None:
        self.name = newName

    def __str__(self) -> str:
        return str(self.name)


class Place:
    '''
    name
    obstacles
    '''

    def __init__(self, newName, newObstacles) -> None:
        self.name = newName
        self.obstacles = newObstacles

    def __str__(self) -> str:
        return str(self.name)


class Altar:
    '''
    name
    active
    acceptedItems
    usedItems
    inputMode  # AND, OR
    place
    '''

    def __init__(self, newName, newActive, newAcceptedItems, newUsedItems, newPlace) -> None:
        self.name = newName
        self.active = newActive
        self.acceptedItems = newAcceptedItems
        self.usedItems = newUsedItems
        self.place = newPlace

    def __str__(self) -> str:
        return str(self.name)


class Obstacle:
    '''
    name
    opened
    altars
    inputMode  # AND, OR
    places
    '''

    def __init__(self, newName, newOpened, newAltars,  newPlaces) -> None:
        self.name = newName
        self.opened = newOpened
        self.altars = newAltars
        self.places = newPlaces

    def __str__(self) -> str:
        return str(self.name)

############################


class State:
    '''
    number
    player
    items
    places
    obstacles
    altars
    '''

    def __init__(self, newNumber, newPlayer, newItems: list,  newPlaces, newObstacles, newAltars) -> None:
        self.number = newNumber
        self.player = newPlayer
        self.items = newItems
        self.places = newPlaces
        self.obstacles = newObstacles
        self.altars = newAltars

    def __str__(self) -> str:
        returnString = "Number: " + str(self.number) + "\n"
        returnString += "Player: " + str(self.player) + "\n"
        for item in self.items:
            returnString += "Items: " + str(item) + "\n"
        for place in self.places:
            returnString += "Places: " + str(place) + "\n"
        for obstacle in self.obstacles:
            returnString += "Obstacles: " + str(obstacle) + "\n"
        for altar in self.altars:
            returnString += "Altars: " + str(altar) + "\n"
        return returnString

    def NextState(self):
        for item in self.player.items:
            for altar in self.altars:
                if item in altar.acceptedItems:
                    stateCopy = copy.deepcopy(self)
                    stateCopy.player.items.remove(item)
                    stateCopy.altars.usedItems.append(item)
                    return stateCopy


items = [Item("Companion cube")]
places = [Place("Button room", [items[0]]), Place("Final room", [])]
altars = [Altar("Ground button", False, items, [], places[0])]
obstacles = [Obstacle("Final door", False, altars, places)]
player = Player("Chell", places[0], [])


initialState = State(1, player, items, places, obstacles, altars)

print(initialState)

print(altars)
print(str(initialState.NextState()))
