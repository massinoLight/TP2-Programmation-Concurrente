#################################
#                               #
#    TP2 Amassin NACERDDINE     #
#                               #
#################################



#########################  Exercie 1  ###############################################################
#fonction qui renvoie le nombre de mots que contient cette chaîne.

#ici on priorise l'utilisation de la fonction prédéfinie splite() pour simplifier mais on aurait tres bien pu
#réaliser ça a l'aide de boucles et de conditions...

import time

def compte_mots(phrase):

     return len(phrase.split())


#########################  Exercie 2  ###############################################################
#
def remplace_multiple(chaine1,chaine2,position):
    p = int(position)
    temp = ''
    a = 0

    for i in range( 0 , len(chaine1)):

        if i == p :
            temp=temp+chaine2[a]
            p = p*2
            a = a+1

        else:
            temp = temp+chaine1[i]

    if len(chaine1) <= len(chaine2):
        for j in range( a , len(chaine2)):
            temp=temp+chaine2[j]

    print(temp)

#########################  Exercie 3 a ###############################################################
#fonction recursive qui calcule la suite Un
def termeU(n):
    if n == 0 :
        return 1
    else:
        return termeU(n-1)*pow(2,n)+n

#########################  Exercie 3 b ###############################################################
#fonction recursive por calculer la série S(p)
def serie(p):
   if p == 0 :
       return termeU(0)
   else:
       return termeU(p-1)+termeU(p)



#########################  Exercie 3 e  ###############################################################
#calcule du temps d'execution du prog
def temp_passe(p):
    depart = time.process_time()
    serie(p)
    arrivee = time.process_time()
    print("temps passe en secondes: ", arrivee - depart)

#########################  Exercie 4   ###############################################################
#fonction qui calcule la factorielle
def factorielle(n):
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)


if __name__ == '__main__':


   compte_mots("")
   compte_mots("il ingurgite impunément un iguane.")
   compte_mots("coursdeprogrammation")
   compte_mots(" Attention aux espaces consécutifs ou terminaux ")
   remplace_multiple('botjaurLaMonde', 'noe', 2)  # bonjourLeMonde
   remplace_multiple('abacus', 'oiseau', 2)  # ’abocisseau’
   remplace_multiple('hirondelles', 'nid', 3)  # ’hirnndillds’ici le e ne doit pas passer en d car 2n=12 et non pas 9
   remplace_multiple('', '', 2)  #

   print(termeU(0))
   print(termeU(1))
   print(termeU(5))
   print(termeU(10))

   print(serie(0))
   print(serie(1))
   print(serie(5))
   print(serie(10))
   temp_passe(100)
   print(factorielle(1))
   print(factorielle(2))
   print(factorielle(3))
   print(factorielle(4))
   print(factorielle(5))
