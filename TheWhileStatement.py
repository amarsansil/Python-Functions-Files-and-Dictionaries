# Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.

n = 0
eve_nums = []
while (n <=15):
    if(n % 2 == 0):
        eve_nums.append(n)
    n += 1



# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.

accum = 0
list1 = [8, 3, 4, 5, 6, 7, 9]
n = 0
while (n < len(list1)):
    accum += list1[n]
    n += 1
