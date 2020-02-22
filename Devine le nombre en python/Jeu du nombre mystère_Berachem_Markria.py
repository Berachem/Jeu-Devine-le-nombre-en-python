from random import randint

cmpt = 1
nombre = randint(1,1000)
joueur = input("Entrez votre pseudo :")
print("====================================================================================")
print("Bienvenue à vous,", joueur," et bonne chance ! :)")
print("====================================================================================")
essai = int(input("Entrez un nombre :"))


while True:
    cmpt += 1 

    if essai > nombre:
        print("Moins ↓")
    elif essai < nombre:
        print("Plus ↑")
    else:
        print("====================================================================================")
        print("Bingo,", joueur,"tu as trouvé le nombre en", cmpt, "essai(s)")
        print("====================================================================================")
        break

    essai = int(input("Entrez un nombre :"))