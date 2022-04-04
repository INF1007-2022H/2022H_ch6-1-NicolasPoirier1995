  
mot1, mot2 = input("Entrez deux mots : ").split()

if sorted(mot1) == sorted(mot2):
    print(mot1 + " et " + mot2 + " sont des anagrames")
else:
    print(mot1 + " et " + mot2 + " ne sont pas des anagrames") 