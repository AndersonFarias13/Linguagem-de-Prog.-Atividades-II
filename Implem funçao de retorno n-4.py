
# -*-coding : latin1-*-
# Testa se o n�mero � primo
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

# Para x de 1 a 100
for x in range(1, 101):
    if is_prime(x):
        print x
