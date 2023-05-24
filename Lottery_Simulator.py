#1) What are the expected winnings from buying n lottery tickets at m dollars with the given odds of winning for a single person?
#2) What are the expected winnings from buying n lottery tickets at d dollars with the given odds of winning for a group of h people?
#3) WHat is the minimum number of tickets that should be bought at d dollars with given odds to make it worth buying?


import random
import matplotlib.pyplot as plt
# plt.use('module://backend_interagg')
import pandas as pd


path = pd.read_excel(r"C:\Users\ydrub\Downloads\lottery_data.xlsx")
lottery_data = path.to_dict()

# print(From[0], To[0])
# print(lottery_data.get('Winnings'))
# print(len(lottery_data.get('Winnings')))

#Inputs
tickets_Purchased = 20
num_simulations = 100
ticket_cost = 5
net_gain = []

""""
odds:
Nothing: 573/1000
$1: 1/4 -> 250/1000 -> 823/1000
$5: 1/8 125/1000 948/1000
$10: 1/20 50/1000
$1000: 1/500 2/1000

"""
# create amount of lottery tickets
#'play' the lottery ticket by removing element in tickets purchased array
# Return result of ticket (win/lose)
# Create a dictionary of ticket number/values

def create_lottery_tickets():
    tickets_Purchased = {}
    From = lottery_data.get('From') #From what lottery ticket in the roll can you win that amount
    To = lottery_data.get('To') #To what lottery ticket in the roll can you win that amount
    Winnings = lottery_data.get('Winnings') #How

    for award in range(len(Winnings)):
        for i in range(From[award], To[award]+1):
            tickets_Purchased[i] = Winnings[award]

    return (tickets_Purchased)


def menu(tickets_drawn,net_gain):
    print("What data do you want to see?")
    print("1:Tickets Drawn", "2:Net Gain Each Simulation", "3:Average winnings over all simulation", sep="\n")
    choice = int(input("Make your selection: "))
    if choice == 1:
        print(tickets_drawn)
    elif choice == 2:
        print(net_gain)
    elif choice == 3:
        average_winning = sum(net_gain)/num_simulations
        print("Average winning after " + str(num_simulations)+ " simulations is $" +str(average_winning))


fig = plt.figure()
plt.title("Lottery winning from buying [" +str(tickets_Purchased)+ "] tickets over [" + str(num_simulations) + "] simulations")
plt.xlabel("# of tickets purchased")
plt.ylabel("Winnings")
plt.xlim([0, tickets_Purchased])
#print(random.choice(list(roll.items())))

for simulations in range(num_simulations):
    roll = create_lottery_tickets()
    tickets_drawn = []
    ticket_count = [0]
    win = 0
    balance = [0]

    for i in range(tickets_Purchased):

        select_ticket = random.choice(list(roll.items()))
        # print(select_ticket, select_ticket[0], sep = '**')
        ticket_index = select_ticket[0]
        # print(ticket_index)
        tickets_drawn.append(select_ticket)
        del roll [ticket_index]
        win += tickets_drawn[i][1]-ticket_cost
        balance.append(win)
        ticket_count.append(i+1)

        if i == tickets_Purchased -1:
            net_gain.append(balance[-1])


    plt.plot(ticket_count,balance)

# print(tickets_drawn)
# print(balance)
# print(net_gain)

plt.show()
show_data = True
while (show_data == True):
    choice = input("See Data? (Y/N): ")
    if (choice == 'Y'.casefold()):
        menu(tickets_drawn, net_gain)
    if (choice != 'Y'.casefold()):
        show_data == False
        break


