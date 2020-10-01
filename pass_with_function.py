# Defining a function named consonant
def consonant(u):
    '''
    This function helps to find consonats in the string..
    '''
    v = "aeiouAEIOU"
    s = ""
    for i in u:
        if i in v:
            pass
        else:
            s+=i
    return s
# Input
u = str(input("Enter something :"))
consonant = consonant(u)
print("consonant: ",consonant)
