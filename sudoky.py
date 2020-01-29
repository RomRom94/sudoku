# SUDOKU ROMAIN FERJULE

# On construit le sudoku ligne par ligne donc la on affiche la premiere ligne avec toutes les colonnes avec les valeurs du tableau grid + un espaces pour revenir a la ligne
def afficher_grille(grille): 
    for numeroLigne in range(9): 
        for numeroColonne in range(9): 
            print (grille[numeroLigne][numeroColonne]), 
        print ('') 
  
          
# Fonction permettant de trouver l'entree dans la grille qui n'est pas encore utilisee 
# Cherche dans la grille pour trouver une entree qui n'est pas encore attribuee. Si elle est trouvee, la ligne des parametres de reference, col sera definie comme l'emplacement qui n'est pas assigne, et true est renvoye. S'il ne reste aucune entree non assignee, false est renvoye. 
# 'l' est une variable de liste qui a ete passee par la fonction resoudreLeSudoku pour suivre l'incrementation des lignes et des colonnes

#On cherche les emplacements vides, c est a dire ceux avec une valeur de 0
def trouverEmplacementVide(grille,l): 
    for ligne in range(9): 
        for colonne in range(9): 
            if(grille[ligne][colonne]==0): 
                l[0]=ligne 
                l[1]=colonne 
                return True
    return False

#explication
#Pour chaque ligne je check, si ca retourne true je check a la ligne d'apres
#exemple : pour la ligne 0 de 0 a 8, pour chaque colonne de 0 a 8, si a la ligne 0 colonne 0 il y a un 0 je recupere la position l[0,0] et je recommence pour la ligne 0 , pour la colonne 1, si a la ligne 0 colonne 1 il y a un 0 je recupere la position l[0,1]
#si ca retourne false ca veut dire qu il n y a pas de trou donc tout est complete
  
# Renvoie un booleen qui indique si une entree attribuee dans la ligne specifiee correspond au numero donne.
# Si trouve ==> true est renvoye sinon false

def existeDansLaLigne(grille,ligne,numero): 
    for i in range(9): 
        if(grille[ligne][i] == numero): 
            return True
    return False
  
# Renvoie un booleen qui indique si une entree attribuee dans la colonne specifiee correspond au numero donne.
# Si trouve ==> true est renvoye sinon false
def existeDansLaColonne(grille,colonne,numero): 
    for i in range(9): 
        if(grille[colonne][i] == numero): 
            return True
    return False
  
#Renvoie un booleen qui indique si une entree attribuee dans une boite de 3 cases sur 3 correspond au nombre donne 
def existeDansLaBoite(grille,ligne,colonne,numero): 
    for i in range(3): 
        for j in range(3): 
            if(grille[i+ligne][j+colonne] == numero): 
                return True
    return False
  
#Verifie s'il sera possible d'attribuer un numero a la ligne donnee, col 
#Renvoie un booleen qui indique s'il sera legal d'attribuer un numero a la ligne donnee, col emplacement. 
def verifierSiNumeroDejaPresent(grille,ligne,colonne,numero): 
      
    #Verifiez si le numero n'est pas deja place dans la ligne, la colonne et la boite actuelle
    #Si not existeDansLaLigne veut dire que cela retourne true donc l element n est pas dans la ligne
    #Si not existeDansLaColonne veut dire que cela retourne true donc l element n est pas dans la colonne
    #Si not existeDansLaBoite veut dire que cela retourne true donc l element n est pas dans la boite
    return not existeDansLaLigne(grille,ligne,numero) and not existeDansLaColonne(grille,ligne,numero) and not existeDansLaBoite(grille,ligne - ligne%3,colonne - colonne%3,numero) 
  
def resoudreLeSudoku(grille): 
      
    # 'l' est une variable de liste qui conserve la position de row et col dans la fonction trouverEmplacementVide     
    l=[0,0] 
      
    # Si il n'y a pas d'emplacement vide c est fini tout est rempli  
    if(not trouverEmplacementVide(grille,l)): 
        return True
      
    # La premiere valeur du tableau est la ligne et l autre la colonne
    ligne=l[0] 
    colonne=l[1] 
      
    # On essaye avec les numeros de 1 a 9
    for numero in range(1,10): 
          
        # Si le numero n est pas present 
        if(verifierSiNumeroDejaPresent(grille,ligne,colonne,numero)): 
              
            # on essaye avec un chiffre
            grille[ligne][colonne]=numero 
  
            # Si la grille est resolu on envoi true et c est fini
            if(resoudreLeSudoku(grille)): 
                return True
  
            # Sinon on remet 0 et on recommence avec un autre chiffre
            grille[ligne][colonne] = 0
              
    return False 
    
# Tableau de ligne qui represente le sudoku
grille=[[5,0,0,6,0,0,2,7,0], 
        [6,0,0,7,4,0,1,0,8], 
        [0,0,0,0,2,5,6,4,0], 
        [4,0,9,0,0,2,3,1,0], 
        [0,0,7,0,0,0,4,0,0], 
        [0,3,1,5,0,0,8,0,6], 
        [0,4,2,9,5,0,0,0,0], 
        [1,0,5,0,3,7,0,0,2], 
        [0,9,6,0,0,8,0,0,4]] 
    
resoudreLeSudoku(grille)
afficher_grille(grille) 
 