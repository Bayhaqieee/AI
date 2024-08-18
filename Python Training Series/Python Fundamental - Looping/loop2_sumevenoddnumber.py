# Sum of all evens and odds from 0 to 100
sum_of_evens = 0
sum_of_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_of_evens += i
    else:
        sum_of_odds += i

print("The sum of all evens is", sum_of_evens)
print("The sum of all odds is", sum_of_odds)
