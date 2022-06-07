# list_of_items = [1, 3, 5, 6, 7]
# print(sum(list_of_items))

def list_sum(x):
    total = 0
    for val in x:
        total = total + val
        return total


list_of_items = [1, 3, 5, 6, 7]
print(list_sum(list_of_items))
