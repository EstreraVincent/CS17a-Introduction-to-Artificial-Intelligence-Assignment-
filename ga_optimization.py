"""
Genetic Algorithm - Example 2: Mathematical Function Optimization
=================================================================
Uses GA to find the MAXIMUM value of f(x) = -x^2 + 10x + 5
within the range x ∈ [-5, 15].

True maximum: x = 5, f(5) = 30

This demonstrates how GA can optimize without derivatives
(unlike gradient descent), making it useful for neural network
weight tuning, hyperparameter search, etc.

Author: Vincent Patrick O. Estrera 
Subject: Algorithm Design
"""

import random

random.seed(0)

# ── Problem Definition ─────────────────────────────────
def f(x):
    """Target function to MAXIMIZE."""
    return -x**2 + 10*x + 5

X_MIN, X_MAX = -5.0, 15.0
POP_SIZE    = 50
GENERATIONS = 200
MUTATION_RATE = 0.15
ELITE_COUNT = 5


# ── GA Operations ──────────────────────────────────────
def random_individual():
    return random.uniform(X_MIN, X_MAX)


def create_population():
    return [random_individual() for _ in range(POP_SIZE)]


def fitness(x):
    return f(x)  # Directly maximize f(x)


def select(population):
    """Roulette-wheel selection (fitness-proportionate)."""
    fits = [fitness(x) - min(fitness(p) for p in population) + 1e-6
            for x in population]
    total = sum(fits)
    r = random.uniform(0, total)
    cumulative = 0
    for ind, fit in zip(population, fits):
        cumulative += fit
        if cumulative >= r:
            return ind
    return population[-1]


def crossover(p1, p2):
    """Arithmetic crossover — blend parents."""
    alpha = random.random()
    child = alpha * p1 + (1 - alpha) * p2
    return max(X_MIN, min(X_MAX, child))


def mutate(x):
    if random.random() < MUTATION_RATE:
        x += random.gauss(0, 1.5)
        x = max(X_MIN, min(X_MAX, x))
    return x


def genetic_algorithm():
    population = create_population()
    best_x    = max(population, key=fitness)
    best_val  = fitness(best_x)
    history   = []

    for gen in range(GENERATIONS):
        # Elitism: carry over best individuals
        population.sort(key=fitness, reverse=True)
        new_pop = population[:ELITE_COUNT]

        while len(new_pop) < POP_SIZE:
            p1 = select(population)
            p2 = select(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop
        current_best = max(population, key=fitness)
        current_val  = fitness(current_best)

        if current_val > best_val:
            best_val = current_val
            best_x   = current_best

        if gen % 40 == 0 or gen == GENERATIONS - 1:
            history.append((gen, round(best_x, 4), round(best_val, 4)))

    return best_x, best_val, history


if __name__ == "__main__":
    print("=" * 55)
    print("  Genetic Algorithm — Example 2: Function Optimization")
    print("=" * 55)
    print("  Function : f(x) = -x² + 10x + 5")
    print(f"  Range    : x ∈ [{X_MIN}, {X_MAX}]")
    print(f"  Goal     : MAXIMIZE f(x)")
    print(f"  Known Max: f(5) = 30 ← GA should find this\n")

    best_x, best_val, history = genetic_algorithm()

    print("📈 Evolution Progress:")
    print(f"  {'Generation':<12} {'Best x':>10} {'f(x)':>12}")
    print("  " + "-" * 36)
    for gen, x, val in history:
        print(f"  {gen:<12} {x:>10.4f} {val:>12.4f}")

    print(f"\n🏆 RESULT:")
    print(f"  Best x found : {best_x:.6f}")
    print(f"  f(best x)    : {best_val:.6f}")
    print(f"  True maximum : x=5.0, f(5)=30.0")
    print(f"  Error        : {abs(best_x - 5.0):.6f}")
    print(f"\n✅ GA successfully located the function maximum!")
    print("💡 This same technique applies to tuning ML model hyperparameters.")
