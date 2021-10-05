import stdiomask
from string import *
from csv import*
import random

# Fonction de calcul
# ###################################################################################################################
def calcul():
    argent = ("$5000", "$10 000", "$20 000")
    print("Men kantite kòb nou ap ka ba ou yo.\n")
    for i in argent:
        print(i)

    for i in range(5):
        montant_des = int(input("\nMete kantite kòb ou vle a:\n"))
        if montant_des == 5000:
            taux = int(input("Mete valè pousantaj ou vle peye chak ane a, ki dwe: '20%' ou '40%'\n"))

            # Valeur 1
            if taux == 20:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 1000:
                    interet2 = ((montant_des + 2000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet2,"an.")
                    break
            elif taux == 40:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 2000:
                    interet3 = ((montant_des + 1000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet3,"an.")
                    break
            # Valeur 2

        if montant_des == 10000:
            taux = int(input("Mete valè pousantaj ou vle peye chak ane a, ki dwe: '20%' ou '40%'\n"))
            if taux == 20:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 2000:
                    interet2 = ((montant_des + 4000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet2,"an.")
                    break
            elif taux == 40:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 4000:
                    interet3 = ((montant_des + 3000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet3,"an.")
                    break

                # Valeur 3
        if montant_des == 20000:
            taux = int(input("Mete valè pousantaj ou vle peye chak ane a, ki dwe: '20%' ou '40%'\n"))
            if taux == 20:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 4000:
                    interet2 = ((montant_des + 4000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet2,"an.")
                    break
            elif taux == 40:
                interet = (montant_des * taux // 100)
                print(interet)
                if interet == 8000:
                    interet3 = ((montant_des + 4000) * 1) // interet
                    print("Wap peye",interet,"dola chak ane pandan ",interet3,"an.")
                    break

            else:
                if taux != 20 or taux != 40:
                    print("Ou fè erè..")
        else:
            if montant_des != 5000:
                print("Ou fè erè..")


# ###################################################################################################################
# ###################################################################################################################

# creation du mot-de-passe:
def mot_de_passe():
    password = stdiomask.getpass(prompt="Kreye yon kòd de sekirite:\n", mask = '.')
    confirm =stdiomask.getpass(prompt="Re mete kòd de sekirite'w la ankò:\n", mask = '.')




# ###################################################################################################################
# ###################################################################################################################

# regeneration du mot de passe.
def generer_mot_de_passe():
    lettre = ascii_letters.upper()
    digits = "0123456789"
    symbols = "!@#$&=?/"
    get_nom = lettre.lower()

    upper, lower, nums, syms = True, True, True, True

    all1 = ""

    if upper:
        all1 += lettre
    if lower:
        all1 += get_nom
    if nums:
        all1 += digits
    if syms:
        all1 += symbols

    length = 6
    amount = 1
    for x in range(amount):
        password1 = "".join(random.sample(all1, length))
        for i in range(3):
            print("Mete kòd sa pou ka fini:",password1)
            validation = stdiomask.getpass(mask = '.')
            if password1 == validation:
                print("Byenvini ankò nan pwogram nou an.\n")
                break

            else:
                print("Ou fè érè, eseye ankò:")




# ###################################################################################################################
# ###################################################################################################################
def intro():
    print("\n!!!! Byenvini nan pwogram finansman an. !!!!\n")

# ###################################################################################################################
# ###################################################################################################################
# Inscription si oui
def login_si_oui():
    nom = input("\nMete non itilizatè'w la:\n")
    user_password = stdiomask.getpass(prompt="Mete kòd de sekirite'w la:\n", mask = '.')
    generer_mot_de_passe()
    ques = int(input("\nKisa ou vle fè? peze '1', '2'ou '3'\n1) Peye nan kòb ou dwe a\n2) Prete Kòb si ou pa dwe\n3) Ou bezwen plis enfòmasyon...\n"))
    if ques == 1:
        print("Pase nan lokal program finansman pou fè sa souple.. Mèsi.")
    elif ques == 2:
        calcul()
        print("Mèsi paske ou fè nou konfyans...")
    elif ques == 3:
        print("Fòk ou pase nan lokal la pou fè yon kanè bank avan.... \nMèsi..")
    else:
        print("Mèsi...")
    quit()


# ###################################################################################################################
# ###################################################################################################################
# Inscription si non
def inscription_si_oui():
        print("SVP ranpli fòm sa pou ka enskri nan pwogram nan:\n")

        count = 0
        nombre_de_pers = int(input("Mete kantite moun ki fè pati de projè a:\n"))
        for x in range(nombre_de_pers):
            count += 1
            print("\n#", count)
            file = open ("Constant.csv","a")

            nom_de_chaque_pers = input("Mete siyati'w svp:\n")
            prenom_de_chaque_pers = input("Mete Non 'w svp:\n")
            nif_de_chaque_pers = input("Mete nif ou svp:\n")
            e_mail = input("Mete e-mail ou:\n")

            information = nom_de_chaque_pers + "," + prenom_de_chaque_pers + "," + nif_de_chaque_pers + "," + e_mail + "\n"
            file.write(str(information))
            file.close()

        mot_de_passe()
        generer_mot_de_passe()
        print("Kounya nou pral pase nan lòt etap ki pi enpòtan an.\n")

# ###################################################################################################################
# ###################################################################################################################

# etape superieure de l'inscription:
def sup_inscription():
    nom_bus = input("Mete non Biznis la:\n")
    start = input("Eske Biznis la gentan kòmanse?\n""repon'n pa: 'wi' ou 'non'\n")
    adresse = input("Mete adrès biznis la ou byen kote ou pral fèl la:\n")
    if start == "wi":
        année = input("Nan ki ane Biznis la kòmanse?:\n")
        age = input("Konbyen tan li genyen: ")
        objectif1 = input("Eske Biznis sa a but Likratif ou non-Likratif?\n""repon'n: 'Likratif' ou non Likratif\n")
        if objectif1 == "likratif".lower():
            raison1 = input("Pou kisa se likratif ou fè biznis la?\n")
        else:
            raison2 = input("Pou kisa ou vle fè Biznis la non Likratif\n")


    else:
        vision_B = input("Pou kisa ou vle fè Biznis sa?\n")
        objectif2 = input("Eske Biznis sa a bi Likratif ou non Likratif?\n""repon'n: 'Likratif' ou non Likratif\n")

        if objectif2 == 'likratif':
            raison = input("Pouki rezon wap fèl Likratif?\n")

        else:
            raison2 = input("Pou kisa ou vle fè Biznis la non Likratif\n")
    print()
    print("Men lis Biznis nou ap finansye yo:")
    liste_bus = ("Restaurant", "Store", "Mall", "Garade machine", "Projet de l'agriculture")
    for i in liste_bus:
        print(i)

    def condition_list_bus():
        while True:
            reponse_user = input("\nMete tip Biznis lan svp:\n")
            if reponse_user == "restaurant".lower():
                calcul()
                break


            elif  reponse_user == "store".lower():

                calcul()
                print("Mèsi paske ou chwazi èd nou nan pwojè Strore ou a, e nou swete'w bon siksè...!!")
                break
            elif reponse_user == "mall".lower():
                calcul()
                print("Mèsi paske ou chwazi èd nou nan pwojè Mall ou a, e nou diw yon lòt fwa ankò bon siksè...!!")
                break
            elif reponse_user == "garage machine".lower():
                calcul()
                print("Mèsi paske ou chwazi èd nou nan pwojè garaj ou a, e nou swete'w bon siksè...!!")
                break

            elif reponse_user == "projet de l'agriculture".lower():
                calcul()
                print("Mèsi dèske wap ede pwodiksyon natyonal la avanse e bon siksè avèk pwojè'w la.!!")
                break
    condition_list_bus()

# ###################################################################################################################

def si_non_merci():
    print("Mèsi dèske ou te vizite nou..")
    quit()




# ###################################################################################################################
# ###################################################################################################################

def condition():
    intro()
    compte = input("Èske ou gen yon kont deja sou pwogram nan?\nReponn 'wi' oubyen 'non'\n")
    if compte == 'wi'.lower():
        login_si_oui()
    elif compte == 'non'.lower():
        choix = input("Èske ou vle enskri nan pwogram nan?\nReponn 'wi' ou 'non'\n")
        if choix == "wi".lower():
            inscription_si_oui()
        elif choix == "non".lower():
            si_non_merci()
    else:
        print("Ou fe ere...")
    sup_inscription()

    print("\nMèsi pou repons ou yo.\nPase nan lokal la aprè 2 jou pou ka siyen\nYon lòt fwa ankò mèsi.....")

condition()


# ###################################################################################################################
# ###################################################################################################################
