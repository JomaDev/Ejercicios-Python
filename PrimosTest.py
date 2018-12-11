import math

def isPrime(number):
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    ###Your isPrime2 code here.
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))+1):  
        if (number%check) == 0:  
            return False
    return True
    pass

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(9) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    assert isPrime(27) == False 
#    print ("1 es primo? ", isPrime(1)) 
#    print ("2 es primo? ", isPrime(2))
#    print ("3 es primo? ", isPrime(3)) 
#    print ("4 es primo? ", isPrime(4))
#    print ("5 es primo? ", isPrime(5))
#    print ("9 es primo? ", isPrime(9))
#    print ("20 es primo? ", isPrime(20))
#    print ("21 es primo? ", isPrime(21))
#    print ("22 es primo? ", isPrime(22))
#    print ("23 es primo? ", isPrime(23))
#    print ("24 es primo? ", isPrime(24))
#    print ("27 es primo? ", isPrime(27))
    print("Prueba exitosa")
    pass
def test2():
    ###Your test code here.
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(20) == False
    assert isPrime2(21) == False
    assert isPrime2(22) == False
    assert isPrime2(23) == True
    assert isPrime2(24) == False
    assert isPrime2(9) == False 
#    print ("1 es primo? ", isPrime2(1)) 
#    print ("2 es primo? ", isPrime2(2))
#    print ("3 es primo? ", isPrime2(3))
#    print ("4 es primo? ", isPrime2(4))
#    print ("5 es primo? ", isPrime2(5))
#    print ("9 es primo? ", isPrime2(9))
#    print ("20 es primo? ", isPrime2(20))
#    print ("21 es primo? ", isPrime2(21))
#    print ("22 es primo? ", isPrime2(22))
#    print ("23 es primo? ", isPrime2(23))
#    print ("24 es primo? ", isPrime2(24))
#    print ("27 es primo? ", isPrime2(27))
    print("Prueba 2 exitosa")
    pass

#test()
test2()
