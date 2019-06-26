'''program to find hcf and lcm of numbers'''
def hcf(l):
    '''First step is to take factors'''
    d={}
    for i in l:
        d[i]=set()
        for j in range(1,i):
            if int(i%j)==0:
                d[i].add(j)
    
list1=[int(x) for x in input('Enter numbers sep by , ').split(',')]
hcf(list1)
lcm(list1)
