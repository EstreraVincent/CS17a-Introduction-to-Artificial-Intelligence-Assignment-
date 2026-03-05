"""
Genetic Algorithm - Example 1: Traveling Salesman Problem (TSP)
===============================================================
A salesman must visit N cities exactly once and return home.
GA evolves increasingly shorter routes over generations.

Author: Vincent Patrick O. Estrera 
Subject: Algorithm Design
"""

import random
import math

# ── City coordinates ──────────────────────────────────
CITIES = {
    "Manila":   (0,   0),
    "Cebu":     (8,  -6),
    "Davao":    (14, -10),
    "Iloilo":   (5,  -5),
    "Zamboanga":(10, -8),
    "Cagayan":  (13, -4),
    "Batangas": (1,  -3),
    "Leyte":    (11, -7),
}

CITY_NAMES = list(CITIES.keys())

random.seed(42)


def distance(c1, c2):
    x1, y1 = CITIES[c1]
    x2, y2 = CITIES[c2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def total_distance(route):
    d = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    return d + distance(route[-1], route[0])  # return to start


def create_population(size):
    population = []
    for _ in range(size):
        route = CITY_NAMES[:]
        random.shuffle(route)
        population.append(route)
    return population


def fitness(route):
    return 1 / total_distance(route)


def select_parents(population):
    """Tournament selection."""
    tournament = random.sample(population, 5)
    return max(tournament, key=fitness)


def crossover(p1, p2):
    """Order crossover (OX)."""
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end+1] = p1[start:end+1]
    fill = [c for c in p2 if c not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child


def mutate(route, rate=0.1):
    """Swap mutation."""
    route = route[:]
    if random.random() < rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


def genetic_algorithm(pop_size=100, generations=500):
    population = create_population(pop_size)
    best_route = min(population, key=total_distance)
    best_dist  = total_distance(best_route)

    history = []

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            p1 = select_parents(population)
            p2 = select_parents(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        current_best = min(population, key=total_distance)
        current_dist = total_distance(current_best)

        if current_dist < best_dist:
            best_dist  = current_dist
            best_route = current_best

        if gen % 100 == 0:
            history.append((gen, round(best_dist, 2)))

    return best_route, best_dist, history


if __name__ == "__main__":
    print("=" * 55)
    print("  Genetic Algorithm — Example 1: TSP")
    print("=" * 55)
    print(f"  Cities      : {len(CITY_NAMES)}")
    print(f"  Population  : 100")
    print(f"  Generations : 500")
    print(f"\n  Running evolution...")

    best_route, best_dist, history = genetic_algorithm()

    print("\n📈 Evolution Progress:")
    print(f"  {'Generation':<12} {'Best Distance':>15}")
    print("  " + "-" * 28)
    for gen, dist in history:
        print(f"  {gen:<12} {dist:>15.2f} units")

    print(f"\n🏆 BEST ROUTE FOUND:")
    route_str = " → ".join(best_route) + f" → {best_route[0]}"
    print(f"  {route_str}")
    print(f"\n📏 Total Distance: {best_dist:.2f} units")
    print("\n💡 GA evolved a near-optimal route by simulating natural selection!")
