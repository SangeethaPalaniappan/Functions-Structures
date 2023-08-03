#floor is the function which returns the same whole value even if it has decimal greater than 5
def floor(key):
    print(int(key))


#ceil returns the next whole value of the given value
def ceil(key):
    key=(int(key))+1
    print(key)

floor(10.5)
floor(13.2)
ceil(12.3)
ceil(33.7)
d=12//11
print(d)