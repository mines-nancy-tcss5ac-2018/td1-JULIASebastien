def miroir(x):
    #retourne le nombre renvers� par rapport � x
    chaine = str(x)
    chaine_inverse = ''
    for lettre in reversed(chaine):
        chaine_inverse += lettre
    x_miroir = int(chaine_inverse)
    return x_miroir

def est_palindrome(x):
    # retourne True si x est un palindrome
    x_miroir = miroir(x)
    if x_miroir == x:
        return True
    else:
        return False

def est_lychrel(x):
    # retourne True si x est un nombre de Lychrel
    for i in range(1, 51):
        x = x + miroir(x)
        if est_palindrome(x):
            return False
    return True

def solve(n):
    # retourne le nombre de nombres de Lychrel qui sont inf�rieurs � n
    compteur_lychrel = 0
    for i in range(1, n+1):
        if est_lychrel(i):
            compteur_lychrel = compteur_lychrel + 1
    return compteur_lychrel


print(solve(10000))