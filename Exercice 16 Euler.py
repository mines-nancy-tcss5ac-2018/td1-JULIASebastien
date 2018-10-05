def solve(n):
    number = 2**n
    somme = 0
    while number > 0 :
        reste = number % 10
        somme = somme + reste
        number = number // 10
    return somme


assert solve(15) == 26
print(solve(1000))
