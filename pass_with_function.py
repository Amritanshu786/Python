def consonant(u):
    v = "aeiouAEIOU"
    s = ""
    for i in u:
        if i in v:
            pass
        else:
            s+=i
    return s;

u = "India is a country"
consonant = consonant(u)
print("consonant: ",consonant)
