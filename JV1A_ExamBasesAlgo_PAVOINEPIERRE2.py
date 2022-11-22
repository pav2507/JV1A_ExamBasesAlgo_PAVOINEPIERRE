## ci-dessous on retrouve chaque etape du programme## 

## ex1 : je créer 2 lignes verticales, et 2 lignes horizontales, pour créer 3 colonnes et 3 lignes formant 9 cases##
## ex2 : pour pouvoir placer le 'O' et le 'X' je les implante grace au input, et grace a la grille de jeu creee juste avant je peux desormais les placer comme dans un tableau ##
## ex3 : apres chaque tour, je demande a l'algorythme de verifer si le symbole 'O' ou 'X' est aligné avec 2 autres signes, si cest le cas la partie s'arrete, sinon elle continue ##
## ex3 suite : pour savoir si les signes sont alignés, je montre dans le programme les differentes possibilitées (horizontal, verticale, diagonale, les differentes positions, etc...)##
## ex4 : si la grillest est complete, cest a dire que les neuf cases sont remplies mais il n'y a pas de vainqueur, la partie s'arrete et une autre recommence. ##
## ex5 : 
## ex6 : si l'on souhaite jouer au puissance 5, le principe est le meme, il faudra malgrés tout faire quelques modifications, tout d'abord le principe de gravité, bon dans ce cas si ##
## ex6 suite : on ne va pas se compliquer la tache, il suffira simplement de verifier si il y a un signe en dessous, si oui, le signe posé s'arrete la, si non il continue de decendre, ##
## ex6 suite :  il faut egalement montrer les possibilités de victoires, ou de match nul comme dans le jeu précédent 
##



monjeu1 = [7,8,9]
monjeu2 = [4,5,6]
monjeu3 = [1,2,3]

player1 = 0
player2 = 0

## ex1 : je créer 2 lignes verticales, et 2 lignes horizontales, pour créer 3 colonnes et 3 lignes formant 9 cases##

print ("    |   |   ")
print ("____________")
print ("    |   |   ")
print ("____________")
print ("    |   |   ")

## ex2 : pour pouvoir placer le 'O' et le 'X' je les implante grace au input, et grace a la grille de jeu creee juste avant je peux desormais les placer comme dans un tableau ##
input ('X')
input ('O')

print(" player1 vous jouer les O vous commencez")
touche = input  # le jouer dois appuyer sur le pavé numérique pour placer son jetons##
if(touche == '1') : # ici j'ecris toute les possibilités possible
    print ("    |   |   ")
    print ("____________")
    print ("    |   |   ")
    print ("____________")
    print ("  O |   |   ")
    if(touche == '2') : 
        print ("    |   |   ")
        print ("____________")
        print ("    |   |   ")
        print ("____________")
        print ("    | O |   ")
        if(touche == '3') : 
            print ("    |   |   ")
            print ("____________")
            print ("    |   |   ")
            print ("____________")
            print ("    |   | O ")
            if(touche == '4') : 
                print ("    |   |   ")
                print ("____________")
                print ("  O |   |   ")
                print ("____________")
                print ("    |   |   ")
                if(touche == '5') : 
                    print ("    |   |   ")
                    print ("____________")
                    print ("    | O |   ")
                    print ("____________")
                    print ("    |   |   ")
                    if(touche == '6') : 
                        print ("    |   |   ")
                        print ("____________")
                        print ("    |   | O ")
                        print ("____________")
                        print ("    |   |   ")
                        if(touche == '7') : 
                            print ("  O |   |   ")
                            print ("____________")
                            print ("    |   |   ")
                            print ("____________")
                            print ("    |   |   ")
                            if(touche == '8') : 
                                print ("    | O |   ")
                                print ("____________")
                                print ("    |   |   ")
                                print ("____________")
                                print ("    |   |   ")
                                if(touche == '9') : 
                                    print ("    |   |  O ")
                                    print ("____________")
                                    print ("    |   |   ")
                                    print ("____________")
                                    print ("    |   |   ")








input()


    
## honnetement il y'avait peu de chance que cette technique marche, mais le pb, c'est que je ne comprends pas pq ça ne marche pas, il n'y a pas de messages d'erreur. ##



    


    

