# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import person
import random
import matplotlib.pyplot as plt
totalPopulation = 1000
totalPeopleInfected = 0
totalPeopleImmune = 0
populationArray = list()
numberOfRounds = 365
lengthOfInfection = 20
lengthOfImmunity = 10
vaccineSuccessRate = 1
vaccineIntroductionRound = 50
vaccineDecrementValue = .00
vaccineAcceptanceRate = 1
Alpha = .01
Beta = .01
for x in range(totalPopulation):
    # change last parameter to static int to vaccinate all on one round... currently each person generates a random round they will get vaccinated on... you can also set a minimum round for the vaccine to appear
  populationArray.append(person.Person(0,0,0,0,random.random(),vaccineSuccessRate,random.randint(50,numberOfRounds - 1)))



plot_round = []
susceptible = []
infected = []
immune = []


populationArray[0].infectionStatus = 1
populationArray[0].turnsRemaining = lengthOfInfection
totalPeopleInfected += 1
for z in range(numberOfRounds):
    x = 0
    y = 0
    currentNumInfections = 0
    currentNumImmune = 0

    while x < totalPopulation :
        y = x + 1

        while y < totalPopulation:
            if (populationArray[x].turnsRemaining > 0 and populationArray[x].infectionStatus == 1) or (populationArray[y].turnsRemaining > 0 and populationArray[y].infectionStatus == 1):
                if random.random() <= Alpha:
                    if random.random() <= Beta:
                        if populationArray[y].infectionStatus == 0:
                            if z < populationArray[y].vaccineIntroductionRound or populationArray[y].vaccineStatus > vaccineAcceptanceRate or random.random() >= populationArray[y].vaccineSuccessRate:

                                populationArray[y].infectionStatus = 1
                                populationArray[y].turnsRemaining = -1
                                populationArray[x].infectionsCaused += 1
                                totalPeopleInfected +=1
                           #negative one turn remaining avoids the node infecting others until the next round
                            populationArray[y].turnsRemaining = -1
                        elif populationArray[x].infectionStatus == 0:
                            if z < populationArray[x].vaccineIntroductionRound or populationArray[x].vaccineStatus > vaccineAcceptanceRate or random.random() >= populationArray[x].vaccineSuccessRate:
                                populationArray[x].infectionStatus = 1
                                populationArray[x].turnsRemaining = -1
                                populationArray[y].infectionsCaused += 1
                                totalPeopleInfected +=1




            y += 1
        
        if populationArray[x].turnsRemaining == -1:
            populationArray[x].turnsRemaining = lengthOfInfection

        elif populationArray[x].turnsRemaining == 0:
            if populationArray[x].infectionStatus == 1:
                populationArray[x].infectionStatus = 2
                populationArray[x].immunityRemaining = lengthOfImmunity
        elif populationArray[x].turnsRemaining > 0:
            populationArray[x].turnsRemaining -= 1

        if populationArray[x].infectionStatus == 2:
            populationArray[x].immunityRemaining -= 1
            if populationArray[x].immunityRemaining <= 0:
                populationArray[x].infectionStatus = 0
                populationArray[x].turnsRemaining = -1
        if z > populationArray[x].vaccineIntroductionRound:
            populationArray[x].vaccineSuccessRate -= vaccineDecrementValue
        x += 1
    for k in range(totalPopulation):

        if populationArray[k].infectionStatus == 1:
            currentNumInfections += 1

        if populationArray[k].infectionStatus == 2:
            currentNumImmune += 1

    print("Round: "+str(z) +" currently infected: -->" +str(currentNumInfections) + "total infections: -->"+str(totalPeopleInfected))
    plot_round.append(z)
    susceptible.append(totalPopulation - (currentNumInfections + currentNumImmune))
    infected.append(currentNumInfections)
    immune.append(currentNumImmune)
sum = 0
avg = 0
for k in range(totalPopulation):
        sum += populationArray[k].infectionsCaused
        avg = sum/totalPopulation
        print("Person #"+str(k) +"caused "+str(populationArray[k].infectionsCaused)+" infections \n")
print("The average infections cause per person was: "+ str(avg))
plt.xlabel('Round')
plt.ylabel('Population')
plt.plot(plot_round, susceptible, label = "Susceptible", color = "blue")
plt.plot(plot_round, infected, label = "Infected", color = "red")
plt.plot(plot_round, immune, label = "Immune", color = "green")
plt.legend()
plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {populationArray[0].infectionStatus, populationArray[1].infectionStatus}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
