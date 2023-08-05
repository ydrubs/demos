# what is the odds of winning if you switch doors?
import random
import matplotlib.pyplot as plt

def create_doors():
    door = {}
    for i in range (3):
        door[i] = 0
    return door

def winning_door(door):
    win = random.randint(0,2)
    door[win] = 1
    # print(door)
    return door

def choose_door(door):
    choice = random.randint(0,2)
    return choice

def show_door(selection, chosen_door):
    del selection[chosen_door[0]]
    print("Doors left: "+ str(selection))


    chosen_door = random.choice(list(selection.items()))

    # print(str(chosen_index) + " this")

    if chosen_door[1] == 1:
        # print("reveal this")
        l = list(selection.values()).index(0) #get the index position of door that does not win (has value of 0 in key value pair)
        # print("reveal door: " +str(l))
        # print(list(selection.items())[l])
        return list(selection.items())[l], selection


    return chosen_door, selection


win_count = 0
win_percent = []
simulations = 100
wins = []
games_played = []

fig = plt.figure()
plt.title("Monte Hall Simulator after " + str(simulations) + " games")
plt.xlabel("# of games played")
plt.ylabel("Win Percent")
plt.xlim([0, simulations])
plt.ylim([0, 1])

for i in range (simulations):
    games_played.append(i)
    wins.append(win_count)
    win_percent.append(win_count/(i+1))
    selection = winning_door(create_doors())
    print("Doors shown: " + str(selection))


    chosen_door = list(selection.items())[choose_door(selection)]
    print("I choose door: " + str(chosen_door))

    door_revealed = show_door(selection, chosen_door) # stores value of: door revealed, doors left
    print("Door Revealed: " + str(door_revealed[0]))

    #get the index of door that does not have key of door revelaved
    switch_to = list(door_revealed[1].keys()).index(door_revealed[0][0])

    if switch_to == 0:
        switched_door = list(selection.items())[1]
        print("Switched to door: " + str(switched_door))
        if switched_door[1] == 1:
          print("you win!")
          win_count +=1



    elif switch_to == 1:
        switched_door = list(selection.items())[0]
        print("Switched to door: " + str(switched_door))
        if switched_door[1] == 1:
            print("you win!")
            win_count +=1


    plt.plot(games_played,win_percent)

print(win_percent)
print(len(win_percent))
print (win_count)
print(win_count/simulations)

graph_text = "win %: " + str(win_count/simulations)
plt.text(simulations/3, .25, graph_text, fontsize = 16)
plt.show()
