# in a room of n people what is the probability that at least 2 have the same birthdays?
import random
import matplotlib.pyplot as plt


def populate_room(people_count):
    people = {}
    for person in range(1,people_count+1):
        people[person] = random.randint(1,365)
    return people


# for simulation in range(10):
def check_matches(people):
    match = False
    for i in range(1, len(people)+1):
        for j in range (i+1, len(people)+1):
            #print (people[i], people[j], sep = ' - ')
            if people[i] == people[j] and match == False:
                match = True
                #print(i, j, people[i], match)
                same_birthday.append(1)
                #print(same_birthday)
                return same_birthday



# people = populate_room()
# print(people)
# match_lst = check_matches(people)
# print(match_lst)

number_ppl = 60
simulations = 1000
lst1 = [0,0] #x-axis data store (# of people in room)
lst2 = [0,0] #y-axis data store (% chance of samd Bday)

fig = plt.figure()
plt.title("Birthday problem after " + str(simulations) + " simulations per iteration")
plt.xlabel("# of people in room")
plt.ylabel("% chance of at least one same birthday")
plt.xlim([0, number_ppl])


for people_count in range(2,number_ppl+1):
    same_birthday = []

    for i in range(simulations):
        people = populate_room(people_count)
        check_matches(people)
        #print(people)

    total_matches = sum(same_birthday)
    percent_match = (total_matches/simulations)*100
    print('...')
    print("Number of people in room: " + str(people_count))
    print("Total Matches: " + str(total_matches))
    print("Percent Matching: "+ str(percent_match))
    print(str(int(people_count*(people_count-1)/2)) + " pairs compared")# (N*(N-1))/2
    lst1.append(people_count)
    lst2.append(percent_match)

    plt.plot(lst1,lst2)

plt.show()






