'''program to perform insertion sort'''

list1=[int(i) for i in input('Enter the array sep by ,:').split(',')]
#print(list1)
list_sorted=[]
#list_unsorted=[]
list_unsorted=list1
#print(list_unsorted)
for i in range(len(list_unsorted)):
    if len(list_sorted)==0:
        list_sorted.append(list_unsorted[0])
    else:
        for j in range(len(list_sorted)):
            if list_unsorted[i]>list_sorted[j]:
                if j==len(list_sorted)-1:
                    list_sorted.append(list_unsorted[i])
                else:
                    if list_unsorted[i]<list_sorted[j+1]:
                        list_sorted.insert(j+1,list_unsorted[i])
                    else:
                        pass
            else:
                if j==0:
                    list_sorted.insert(j,list_unsorted[i])            
print(list_sorted)