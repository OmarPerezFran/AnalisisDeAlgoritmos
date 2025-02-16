from multiprocessing import Pool, cpu_count
import time
import math

def is_prime_bruteforce(n):
    """Verifica si un número es primo usando fuerza bruta"""
    if n < 2:
        return False
    # Prueba TODOS los números como posibles divisores
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    """Verifica si un número es primo usando método optimizado"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Solo prueba hasta la raíz cuadrada y solo números impares
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(args):
    """Encuentra números primos en un rango específico"""
    start, end, use_bruteforce = args
    primes = []
    for num in range(start, end):
        if use_bruteforce:
            if is_prime_bruteforce(num):
                primes.append(num)
        else:
            if is_prime_optimized(num):
                primes.append(num)
    return primes

def parallel_prime_finder(start, end, use_bruteforce=False, chunk_size=1000):
    """Encuentra números primos en paralelo"""
    # Crear rangos para dividir el trabajo
    ranges = []
    current = start
    while current < end:
        next_value = min(current + chunk_size, end)
        ranges.append((current, next_value, use_bruteforce))
        current = next_value

    num_processes = cpu_count()
    print(f"Utilizando {num_processes} procesos")

    with Pool(processes=num_processes) as pool:
        results = pool.map(find_primes_in_range, ranges)

    all_primes = []
    for prime_list in results:
        all_primes.extend(prime_list)
    
    return all_primes

def main():
    start_range = 1
    end_range = 10000  # Reducido para que la fuerza bruta no tarde demasiado
    
    # Prueba con método optimizado
    print("\nUsando método optimizado:")
    start_time = time.time()
    primes_optimized = parallel_prime_finder(start_range, end_range, use_bruteforce=False)
    optimized_time = time.time() - start_time
    
    # Prueba con fuerza bruta
    print("\nUsando fuerza bruta:")
    start_time = time.time()
    primes_bruteforce = parallel_prime_finder(start_range, end_range, use_bruteforce=True)
    bruteforce_time = time.time() - start_time
    
    # Mostrar resultados y comparación
    print("\nResultados:")
    print(f"Números primos encontrados: {len(primes_optimized)}")
    print(f"Primeros 5 primos: {primes_optimized[:5]}")
    print(f"Últimos 5 primos: {primes_optimized[-5:]}")
    
    print("\nComparación de tiempos:")
    print(f"Método optimizado: {optimized_time:.2f} segundos")
    print(f"Fuerza bruta: {bruteforce_time:.2f} segundos")
    print(f"La fuerza bruta fue {bruteforce_time/optimized_time:.1f}x más lenta")

if __name__ == "__main__":
    main()