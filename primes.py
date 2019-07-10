'''
Diffie-Hellman Key Exchange
Jakob Mckinney
17/01/2019
'''
from random import getrandbits
from random import randint
from math import sqrt


def get_really_big_number(size=8):
    '''
    Randomly generate a really big number,
    size is the number of bits to be in the number
    '''
    
    return getrandbits(size)


def test_prime(n, k):
    '''
    fermat prime test,
    Loops through k times each time generating a random number, a, between
    0 and n-2, if a^(n-1) mod n != 1 then n is not prime by fermats little
    theorem and so False is returned. If it passes this k times then n is
    most likely prime and so True is returned
    '''
    for i in range(1, k+1):
        a = randint(0, n-2) 
        if (pow(a, n-1, n)) != 1:
            return False
        
    return True
        

def big_primes(size=16, k=10):
    '''
    Makes a real big prime number by generating big numbers 
    until one that is prime is generated
    '''
    probably_prime = False
    while not probably_prime: # Loops until a prime is found
        big_num = get_really_big_number(size) # Generates a number of given size
        if int(str(big_num)[-1]) % 2 == 0: # Checks if the number is even, if it is it trys again
            pass
        else:
            probably_prime = test_prime(big_num, k) # Calls test_prime func which will return True if big_num is prime
            
    return big_num 


if __name__ == "__main__":
    print('Probably prime: ' + str(big_primes(64, 1)))