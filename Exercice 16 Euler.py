def solve(n):
    # retourne la somme des nombres constituant 2**n
    number = 2**n
    somme = 0
    while number > 0 :
        # on sort de la boucle lorsque number n'est plus strictement positif
        reste = number % 10
        somme = somme + reste
        number = number // 10
    return somme


assert solve(15) == 26
print(solve(1000))
