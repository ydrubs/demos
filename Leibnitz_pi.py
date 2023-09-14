#1/1 - 1/3 + 1/5 - 1/7 + 1/9 -.....
iterations = int(input("How many iterations: "))
total = 0

for i in range(1, iterations+1):
    denominator = 2*i-1
    # print(denominator)
    if i%2 == 0:
        denominator = -denominator
    total+=1/denominator

print(total)

#Break it down into smaller problems
# Problem 1: How can you loop through (and get the sum of) the odd numbers a given amount of iterations (for example for 3 iterations, take the sum of 1+3+5)?
# Problem 2: How can you loop through (and get the sum of) the odd unit fractions a given amount of iterations?
# Problem 3: How can you alternate between adding and subtracting consecutive terms (preferably within ONE loop)?
            #How can you get 1-3+5-7?


#Strategy #2
subt_part = 0
add_part = 0

#addition loop (1/1 + 1/5 + 1/9 + ....)
for i in range(1,2*(iterations),4):
    print(i)
    add_part +=1/i

#subtraction loop (-1/3 - 1/7 - 1/11 - ....)
for i in range(3,2*(iterations),4):
    print(i)
    subt_part -=1/i


print(add_part+subt_part)
