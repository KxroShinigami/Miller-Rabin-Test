#--> Miller-Rabin-Test
#-> The Miller-Rabin-Test is a more exact prime number test then Fermat´s Little Theorem Test

# Input:
try: # prime
        print("\nPlease enter a valid Integer: ")
        prime = int(input("a: "))
except Exception as e:
        print("\nError: ", e)
