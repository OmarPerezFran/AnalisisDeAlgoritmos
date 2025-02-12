def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# comb(n, k) = n! / (k! * (n - k)!)
def combinations(n: int, k: int) -> int:
    combination = factorial(n) / (factorial(k) * factorial(n - k))
    return combination

# var(n, k) = n! / (n - k)!
def variations(n: int, k: int) -> int:
    variation = factorial(n) / factorial(n - k)
    return variation

def birthday(n):
    return 1 - (variations(366, n) / (366 ** n))

def main():
    people = [10, 20, 35, 60]

    for person in people:
        print(
            f'En un grupo de {person} personas, la probabilidad de que al menos dos personas cumplan años el mismo dia es {round(birthday(person), 5)}.')
        print('-----------------------------------------------------------------')

if __name__ == '__main__':
    main()