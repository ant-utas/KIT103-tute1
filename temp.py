# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this is a comment

d = 13/4 # normal division
q = 13//4 # floor division
r = 13%4 # modulo


t = (1, 2, 3, 1) #t is a tuple of four elements (tuple) - ordered
u = 1, 2, 3, 1   #u is also a tuple (and is equal to t) - unordered
l = [1, 2, 3, 1] #l is a list of four elements; l != t but l == list(t) [list]
s = {1, 2, 3, 1} #s is a set of three elements {set}



l = [1, 2, 3, 4, 5]
s = {1, 2, 3, 4, 5}

l = ['kangaroo','wallaby','chicken','cow','salmon']
s = {'kangaroo','wallaby','chicken','cow','salmon'}


s = set() #creates an empty set
for i in range(1, 11):
    s.add( i**2 )
    
    
fours = set()
for i in range(1, 31):
    fours.add( 4 * i )
    
evens = set()
for k in range(0, 11):
    evens.add( 2 * k )

odds = set()
for k in range(0, 11):
    odds.add( 2 * k + 1 )

powers3 = set()
for i in range(0, 4):
    powers3.add( 3**i )
    powers3.add( -1 * 3**i )

powers3_alt = set()
for i in range(-4, 5):
    if i != 0:
        powers3_alt.add( i//abs(i) * 3**(abs(i)-1) )
        # first part gets sign, next one generates the value 27, 9, 3 or 1
        
        
