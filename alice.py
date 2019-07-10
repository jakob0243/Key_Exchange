'''
Diffie-Hellman Key Exchange
Jakob Mckinney
17/01/2019
'''
import primes


class Alice:
    '''
    Class Alice that represents the information Alice has
    during the diffie-hellman key exchange
    '''
    
    def __init__(self, g, p):
        '''
        Initiliases the Alice class using the public keys 
        passed in as g and p, a is randomly generated and 
        A is calculated from g^a mod p
        '''
        self.g = g
        self.p = p
        self.a = primes.get_really_big_number(256)
        self.A = self.calc_biga()
        
        self.B = None
        self.key = None
        
        
    def calc_biga(self):
        '''
        Returns A = p^a mod p
        '''
        x = pow(self.g, self.a, self.p) 
        
        return x
    
    def calc_key(self):
        '''
        Calculates the shared key and assigns it to self.key
        '''
        self.key = pow(self.B, self.a, self.p)
        
        print("The key is: " + str(self.key))