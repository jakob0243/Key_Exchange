'''
Diffie-Hellman Key Exchange
Jakob Mckinney
17/01/2019
'''
from alice import Alice
from bob import Bob
from primes import big_primes
from math import gcd as bltin_gcd
import time

def egcd(a, b):
    '''
    Uses euclidean algorithm to recursively calculate 
    gcd of a and b
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y) #g is the gcd


def get_public_keys_egcd():
    '''
    Calculates p and n which are the public keys used
    p and n must be relativley prime for it to work securely
    p is almost always 2 and n is a randomly generated large
    prime, they are then put through the euclidean algorithm
    to see if they are relativley prime.
    '''
    are_coprime = False
    
    while not are_coprime:
        p = 2
        n = big_primes()
        
        a, _, _ = egcd(p, n) # a is the gcd(p, n)
        
        # Checks if p and n are co-prime
        if a == 1:
            are_coprime = True
        else:
            p += 1 # If p and n aren't co-prime then p+1 and n will always be co-prime
    
    # p and n must be co-prime
    return p, n


def get_public_keys_bltin():
    '''
    Same as above but uses builtin gcd method instead of 
    euclidean algorithm, bit more effecient
    '''
    p = 2
    while True:
        n = big_primes()
        
        gcd_pn = bltin_gcd(p, n)
        if gcd_pn == 1:
            return p, n
        else:
            p += 1
    

def main():
    '''
    Performs the Key Exchange between and instance of class Alice and 
    an instance of class Bob, it prints the private keys, A and B, of
    Alice and Bob and also the shared Public key twice, once for the 
    instance of Alice and once for the instance of Bob
    '''
    start1 = time.time()
    #g, p = get_public_keys_egcd()
    #end1 = time.time()
    #print("p: {}, n: {}, time taken: {}".format(str(p1), str(n1), str(end1-start1)))
    
    #start = time.time()
    g, p = get_public_keys_bltin()
    #end = time.time()
    #print("g: {}, p: {}, time taken: {}".format(str(g), str(p), str(end1-start1)))
    #print("p: {}, n: {}, time taken: {}".format(str(g1), str(p1), str(end-start))) '''
    
    alice = Alice(g, p) #g, p
    bob = Bob(g, p)
    
    public_alice = alice.A
    public_bob = bob.B
    print("A = " + str(public_alice))
    print("B = " + str(public_bob))
    
    alice.B = public_bob
    bob.A = public_alice
    
    alice.calc_key()
    bob.calc_key()
    
    end = time.time()
    print("Time taken: {}".format(end-start1))
    
    
    # Time taken with normal exponentiation: 0.001996278762817383 (8-bit number)
    # Time taken with pow() exponentiation: 0.003019094467163086 (256-bit number)
    # Time taken with pow() and more effecient prime test and get_public_keys_egcd(): 0.001024484634399414 (256-bit number)
    # Time taken with pow() and more effecient prime test and get_public_keys_bltin(): 0.0 (256-bit number) - negligible time i guess
    

if __name__ == "__main__":
    main()