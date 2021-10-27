import copy
import os


class State:
    def __init__(self, newNumber, newTowers) -> None:
        self.number = newNumber
        self.towers = newTowers

    def __eq__(self, o: object) -> bool:
        if type(o) is State and self.towers == o.towers:
            return True
        else:
            return False

    def __str__(self) -> str:
        returnString = "State " + str(self.number) + "\n"
        for i in range(len(self.towers)):
            returnString += "Tower " + str(i) + ": "
            for number in self.towers[i]:
                returnString += str(number) + " "
            returnString += "\n"
        return returnString

    def NextStates(self):
        nextStates = []
        for i in range(len(self.towers)):
            for j in range(len(self.towers)):
                if i != j and len(self.towers[i]) > 0:
                    if len(self.towers[j]) < 1 or self.towers[i][0] < self.towers[j][0]:
                        newState = copy.deepcopy(self)
                        newState.towers[j] = [
                            newState.towers[i][0]] + newState.towers[j]
                        newState.towers[i].pop(0)
                        nextStates.append(newState)
        return nextStates


def NextWave(currentStates, statesToCheck):
    nextStates = []
    for stateToCheck in statesToCheck:
        nextStates += stateToCheck.NextStates()
    for nextState in nextStates:
        if nextState not in currentStates:
            nextState.number = len(currentStates)
            currentStates.append(nextState)
            currentStates = NextWave(currentStates, nextState.NextStates())
    return currentStates


initialNumbers = [[1, 2, 3], [], []]
initialState = State(0, initialNumbers)
global states
states = [initialState]

states = NextWave(copy.deepcopy(states), copy.deepcopy(states))

dotCode = "strict graph {\n"
dotCode += "\"123| | \"" + " [shape=doublecircle];\n"
dotCode += "\" | |123\"" + " [shape=Msquare];\n"
for state in states:
    label = ""
    for tower in state.towers:
        for number in tower:
            label += str(number)
        if tower == []:
            label += " "
        label += "|"
    label = label[:-1]
    for nextState in state.NextStates():
        nextLabel = ""
        for tower in nextState.towers:
            for number in tower:
                nextLabel += str(number)
            if tower == []:
                nextLabel += " "
            nextLabel += "|"

        nextLabel = nextLabel[:-1]
        dotCode += "\"" + str(label) + "\"" + " -- \"" + \
            str(nextLabel) + \
            "\";\n"
dotCode += "\n}"


with open('digraph.txt', 'w') as f:
    f.write(dotCode)

os.system("dot -Tpng digraph.txt > digraph.png")
