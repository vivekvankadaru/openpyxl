'''program to find hcf and lcm of numbers'''
def hcf(l):
    '''First step is to take factors'''
    d={}
    for i in l:
        d[i]=set()
        for j in range(1,i+1):
            if int(i%j)==0:
                d[i].add(j)
    print(d)
    d1={}
    keylist=list(d.keys())
    for i in d:
        if not d1:
            d1=d[i].intersection(d[keylist[keylist.index(i)+1]])
        else:
            if keylist.index(i)+1==len(keylist):
                pass
            else:
                d1=d1.intersection(d[keylist[keylist.index(i)+1]])
    print("The GCD of numbers given is " + str(max(d1)))
list1=[int(x) for x in input('Enter numbers sep by , ').split(',')]
hcf(list1)
#lcm(list1)