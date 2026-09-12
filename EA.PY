import random

distance = {
    'A': {'A': 0, 'B': 32, 'C': 10, 'D': 18},
    'B': {'A': 32, 'B': 0, 'C': 30, 'D': 23},
    'C': {'A': 10, 'B': 30, 'C': 0, 'D': 12},
    'D': {'A': 18, 'B': 23, 'C': 12, 'D': 0}
}

print("\nDistance Matrix:")
for city in distance:
    print(city, distance[city])

population = [
    ''.join(random.choice('01') for _ in range(4))
    for _ in range(5)
]

def fitness(ch):
    return ch.count('1')

print("\nInitial Population:")
for i, ch in enumerate(population):
    print(f"Chromosome {i + 1}: {ch}, Fitness = {fitness(ch)}")

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)

    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]

    print(f"\nParent 1: {p1}")
    print(f"Parent 2: {p2}")
    print(f"Crossover Point: {point}")
    print(f"Child 1: {c1}")
    print(f"Child 2: {c2}")

    return c1, c2

p1 = population[0]
p2 = population[1]
c1, c2 = crossover(p1, p2)

p3 = population[2]
p4 = population[3]
c3, c4 = crossover(p3, p4)

c5 = population[4]

children = [c1, c2, c3, c4, c5]

print("\nAfter Crossover:")
for i, ch in enumerate(children):
    print(f"Chromosome {i + 1}: {ch}, Fitness = {fitness(ch)}")

for i in range(len(children)):
    pos = random.randint(0, 3)
    child = list(children[i])

    if child[pos] == '0':
        child[pos] = '1'
    else:
        child[pos] = '0'

    children[i] = ''.join(child)

print("\nAfter Crossover + 1-bit Mutation:")
for i, ch in enumerate(children):
    print(f"Chromosome {i + 1}: {ch}, Fitness = {fitness(ch)}")

print("\nInitial Fitness:")
for i, ch in enumerate(population):
    print(f"Chromosome {i + 1}: {ch}, Fitness = {fitness(ch)}")