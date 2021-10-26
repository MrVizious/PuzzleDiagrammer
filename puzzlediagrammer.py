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

    def __eq__(self, o: object) -> bool:
        if type(o) is Player and o.name == self.name and o.place == self.place and self.items.sort() == o.items.sort():
            return True
        else:
            return False


class Item:
    '''
    name
    '''

    def __init__(self, newName) -> None:
        self.name = newName

    def __str__(self) -> str:
        return str(self.name)

    def __eq__(self, o: object) -> bool:
        if type(o) is Item and self.name == o.name:
            return True
        else:
            return False


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

    def __eq__(self, o: object) -> bool:
        if type(o) is Place and self.name == o.name and self.opened == o.opened and self.altars.sort() == o.altars.sort() and self.places.sort() == o.places.sort():
            return True
        else:
            return False


class Altar:
    '''
    name
    active
    acceptedItems
    usedItems
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

    def __eq__(self, o: object) -> bool:
        if type(o) is Altar and o.name == self.name:
            return True
        else:
            return False


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

    def __eq__(self, o: object) -> bool:
        if type(o) is Obstacle and self.name == o.name and self.opened == o.opened and self.altars.sort() == o.altars.sort() and self.places.sort() == o.places.sort():
            return True
        else:
            return False


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

    def __init__(self, newNumber, newPlayer, newPlaces, newObstacles, newAltars) -> None:
        self.number = newNumber
        self.player = newPlayer
        self.places = newPlaces
        self.obstacles = newObstacles
        self.altars = newAltars

    def __str__(self) -> str:
        returnString = "Number: " + str(self.number) + "\n"
        returnString += "Player: " + str(self.player) + "\n"
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
                    if item in stateCopy.player.items:
                        stateCopy.player.items.remove(item)
                        altar_in_copy = next(
                            (x for x in stateCopy.altars if altar == x), None)
                        if altar_in_copy is not None:
                            altar_in_copy.usedItems.append(item)
                    return stateCopy


items = [Item("Companion cube")]
places = [Place("Button room", [items[0]]), Place("Final room", [])]
altars = [Altar("Ground button", False, items, [], places[0])]
obstacles = [Obstacle("Final door", False, altars, places)]
player = Player("Chell", places[0], items)

initialState = State(1, player, places, obstacles, altars)

next_state = initialState.NextState()

print(initialState.altars[0].usedItems)
print(next_state.altars[0].usedItems)
