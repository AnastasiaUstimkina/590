import math
# reading

queries = int(input())
sets = []
user_set = {}
prices = []

for query in range(0, queries):
    n = int(input())
    prices = input()
    prices = [int(price) for price in prices.split()]
    user_set = {'n': n, 'prices': prices}

    price = math.ceil(sum(user_set['prices']) / user_set['n'])

    print(price)







