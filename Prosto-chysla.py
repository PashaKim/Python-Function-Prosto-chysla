def is_prime(a):
    if a == 1:
        return False
    for d in range(2,a):
        if a%d == 0:
            return False
    return True
a = int(input('Число: '))
if is_prime(a) == True:
    print('Простое')
else:
    print('не простое')
