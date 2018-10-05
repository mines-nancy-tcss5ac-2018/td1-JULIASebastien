def valeur_lettre(x):
    #retourne la valeur d'une lettre de l'alphabet
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, len(alphabet)) :
        if x == alphabet[i]:
            valeur = i + 1
    return valeur

def alphabetical_value(mot):
    # retourne la valeur d'un mot entré par l'utilisateur, selon les critères de l'exercice
    valeur_mot = 0
    
    for i in range(1, len(mot)-1): # i parcourt chaque lettre dans le mot considéré
        valeur = valeur_lettre(mot[i]) # ord retourne la valeur que Python associe à un caractère
        # Les majuscules commencent à 65 donc on retire 64
        valeur_mot = valeur_mot + valeur # On somme les valeurs associées à chaque lettre constituant le mot
        
    return valeur_mot

assert alphabetical_value('"COLIN"') == 53

def solve():
    # retourne le total des scores des mots du fichier considéré
    f = open('Fichier exo 22.txt', 'r') # J'ai renommé le fichier sur lequel on travaille
    liste_noms = []
    liste_triee = []
    somme = 0
    
    for lignes in f: # lignes parcourt f
        liste_noms = lignes.split(',') #split(',') sépare les chaînes de caractères
        liste_triee = sorted(liste_noms, key = str.lower) #tri par ordre alphabétique
        
    for i in range(0, len(liste_triee)):
        name_score = alphabetical_value(liste_triee[i]) * (i+1)
        somme = somme + name_score
        
    return somme

 
print(solve())