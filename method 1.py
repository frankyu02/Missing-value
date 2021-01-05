#method 1: sort the inputted list and then go through each value in the list until there is a break in consistency amongs the elements
#output the valued that is not present
#for example: [2 1 3 4 6]-> [1 2 3 4 6]-> outputs 5

lst=[]
val=int(input("How many values in the list? ")) #take the initial list
for i in range(val):
    x=int(input())
    lst.append(x)

lst.sort() #sort the list in ascending order

if len(lst)+1!=lst[len(lst)-1]:
    print(len(lst)+1)
else:
    for i in range(val):
        if i+1!=lst[i]:
            print(i+1)
            break;





