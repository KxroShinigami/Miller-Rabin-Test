#--> Miller-Rabin-Test
#-> The Miller-Rabin-Test is a more exact prime number test then Fermat´s Little Theorem Test.
#-> Input: a uneven number "prime" to test if its a prime number and "a" {2, 3, ..., prime-2} thats an integer relatively prime to "prime"


prime = 0
# Input:
while(prime%2 != 1):
        try: # prime
                print("\nPlease enter a valid uneven Integer: ")
                prime = int(input("prime: "))
        except Exception as e:
                print("\nError: ", e)

try: # a
        print("\nPlease enter a valid relatively prime integer to *prime* {2, 3, ..., prime-2}: ")
        a = int(input("a: "))
except Exception as e:
        print("\nError: ", e)


def miller_rabin_test(prime, a):
                s = len(format(prime, "b"))
                d = (prime-1)/(2**s)
                if((a**d) % prime == 1):
                        print(prime, " is a prime number")
                else:
                        r = 0 # r = {0, 1, ..., s-1}
                        while((a**((2**r)*d))%prime != -1 and r <= s):
                                r = r +1

                        if(r >= s): print(prime, " is a prime number")
                        else: print(prime, " is a prime number")





miller_rabin_test(prime, a)