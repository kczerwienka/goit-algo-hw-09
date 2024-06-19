
class Item:
    def __init__(self, amount, value):
        self.amount = amount
        self.value = value


def find_coins_greedy(change: list[Item], amount: int)-> dict:
    change.sort(key=lambda x: x.amount, reverse=True)
    return_change = {1 : 0, 2 : 0, 5 : 0, 10 : 0, 25 : 0, 50 : 0}        
    
    i=0
    while amount > 0:
        print(change[i].value, change[i].amount)
        if change[i].amount > 0:
            if amount >= change[i].value:
                amount -= change[i].value
                return_change[change[i].value] += 1
                change[i].amount -= 1
                change.sort(key=lambda x: x.amount, reverse=True)
            else:
                if i < 5:
                    i +=1
                else:
                    i = 0
    return return_change


def find_min_coins(value, count, amount) -> dict:
    return_change = {1 : 0, 2 : 0, 5 : 0, 10 : 0, 25 : 0, 50 : 0} 
    
    i = 5

    while amount > 0:

        if amount >= value[i] and count[i] > 0:
        
            amount -= value[i]
            return_change[value[i]] += 1
        
        else:
            i -= 1

    return return_change

value = [1, 2, 5, 10, 25, 50]
count = [10, 20, 30, 40, 50, 600]

total = 0


change = list()
for i in range(0,len(value)):
    change.append(Item(count[i], value[i]))

amount = 5634


print(find_coins_greedy(change, amount)) 

print(find_min_coins(value, count, amount))