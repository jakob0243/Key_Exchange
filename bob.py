'''
Diffie-Hellman Key Exchange
Jakob Mckinney
17/01/2019
'''
import primes


class Bob:
    '''
    Class Bob that represents the information Bob has
    during the diffie-hellman key exchange
    '''
    
    def __init__(self, g, p):
        '''
        Initiliases the Bob class using the public keys 
        passed in as g and p, b is randomly generated and 
        B is calculated from g^b mod p
        '''
        self.g = g
        self.p = p
        self.b = primes.get_really_big_number(256) # Generates a 256 bit prime number randomly
        self.B = self.calc_bigb() # Calculate g^b mod p
        
        self.A = None
        self.key = None
    
    
    def calc_bigb(self):
        '''
        Returns B = p^a mod p
        '''
        b = pow(self.g, self.b, self.p)
        
        return b
    
    
    def calc_key(self):
        '''
        Calculates the shared key and assigns it to self.key
        '''
        self.key = pow(self.A, self.b, self.p) # Calculates A^b mod p
        
        print("The key is: " + str(self.key))    