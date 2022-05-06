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


def miller_rabin_test(prime):
                for s in range(prime-1, 0, -1):
                      if((prime-1)%(2**s) == 0): break # max 2^r divisor for "prime"-1
                d = (prime-1)/(2**s)
                print("d = ", d, " s = ", s)
                for a in range(2, prime - 2):
                        print("\nbase: ", a)

                        if(pow(a, int(d), prime) == 1):
                                print(prime, " is most likely a prime number")
                                break
                        else:
                                r_i = 0 # r_i = {0, 1, ..., s-1}
                                num = 0
                                while(num != prime-1 and r_i < s):
                                        num = pow(a, int((pow(2, r_i, prime))*d), prime)
                                        #print("a^(2^(r)*d) : ", num)
                                        r_i = r_i + 1

                                if(r_i >= s): print(prime, " is not a prime number")
                                else: 
                                        print(prime, " is most likely a prime number")
                                        break


miller_rabin_test(prime)