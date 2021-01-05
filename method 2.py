#Since it is known that all values from 1 to n must be present in the list,
#the total sum of the list must be equal to the summation of 1 to the length of the list +1

lst=[]
val=int(input("How many values in the list? ")) #take the initial list
for i in range(val):
    x=int(input())
    lst.append(x)

total=sum(lst) #take the total sum of all elements present in the array

#to find expected total value from 1 to n, use to formula:
#total= n/2(2a+(n-1)d) where n is the number of elements in the arraym, a is the first value in the the sequence, d is the common difference
#Since the sequence is always from 1 to n, a=1 and since each value from 1 to n is present in the array, this also sets d=1
#subbing those constants gives us: n/2(2+n-1) -> (n*(n+1))/2

n=len(lst) #set n to be equal to the length of the list+1 since there is an element missing
expected_value=(n*(n+1))/2
print(expected_value-total)
