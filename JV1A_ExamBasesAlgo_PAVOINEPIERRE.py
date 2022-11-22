## tri a bulles ##

mytable = [12,4,26,45,9]

print(mytable)

sauvegarde = 0


## ex1 : je permutte plusieurs valleurs ##
## ex2 : chaques valeurs permuttent en fonction de la valeur suivante et s'arrete l'orsque la prochaine lui ai superieur ##
## ex3 : le programme fonctionne peu import le nombre de valeur rajoutee ou enlevee ##


for n in range(len(mytable)-1): 
    for i in range(len(mytable)-1): 
        if(mytable[i] > mytable[i+1]): 
            sauvegarde = mytable[i]
            mytable[i] = mytable[i+1]
            mytable[i+1] = sauvegarde

print (mytable)        

###    reponse a la 4e question : le tri a bulle est considere comme lent car il calcul fonction de la valeur qui suivra, c'est a dire,#
# valeur par valeur, il ne calcul pas tout en une seule fois, lorsqu'il a finit de faire monter une valeur il passe a la prochaine.     ###
