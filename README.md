# CS17a-Introduction-to-Artificial-Intelligence-Assignment-

# Algorithm Design — Programming Assignment
**Course:** Algorithm Design & Analysis  
**School:** University of Southern Mindanao (USM)  
**Program:** BS Computer Science  
**The code i send and add in here, on GitHub might not run successfully, as you can see there is an emoji with X and Check. But, i fixed and run them without debugging on the Visual Code Studio, as you can see on each Output Screenshots. The 6 algorithms are running successfully.
---

## 📁 Project Structure

```
algorithms/
├── astar/
│   ├── astar_maze.py         # Example 1: Grid Maze Navigation
│   └── astar_cities.py       # Example 2: City Route Finder (GPS)
├── apriori/
│   ├── apriori_market.py     # Example 1: Market Basket Analysis
│   └── apriori_medical.py    # Example 2: Medical Symptom-Diagnosis
├── genetic/
│   ├── ga_tsp.py             # Example 1: Traveling Salesman Problem
│   └── ga_optimization.py    # Example 2: Mathematical Function Optimization
└── README.md
```

---

## 1. 🔍 A* Algorithm (A-Star)

### What is A*?
A* is a **pathfinding and graph traversal algorithm** that efficiently finds the shortest path between two nodes. It uses a cost function:

```
f(n) = g(n) + h(n)
```

- `g(n)` = actual cost from start to the current node  
- `h(n)` = heuristic estimate from current node to goal  
- Always expands the node with the **lowest f(n)** first

### Why A*?
A* is both **complete** (always finds a path if one exists) and **optimal** (finds the shortest path), making it superior to plain BFS or Dijkstra in most real-world scenarios.

### Example 1 — Grid Maze Navigation
```
python astar/astar_maze.py
```
Navigates through a 7×7 grid maze with walls, finding the shortest path from `(0,0)` to `(6,6)` using **Manhattan distance** as the heuristic.

**Sample Output:**
```
  0 1 2 3 4 5 6
0 S * * # . . .
1 . # * # . # .
2 . # * . . # .
3 . . * # # # .
4 # # * * * * .
5 . . . # # * #
6 . . . . . * G

✅ Path found! Length: 13 steps
```

### Example 2 — City Route Finder (GPS-style)
```
python astar/astar_cities.py
```
Finds the shortest road route between Philippine cities using **Euclidean distance** as the heuristic.

**Sample Output:**
```
✅ Optimal Route Found!
   Manila → Quezon → Camarines → Albay → Sorsogon → Davao
📏 Total Distance: 1420 km
```

---

## 2. 📊 Apriori Algorithm

### What is Apriori?
Apriori is a **frequent itemset mining** algorithm that discovers hidden relationships (association rules) in datasets. It follows the **Apriori principle**:

> *If an itemset is infrequent, all its supersets must also be infrequent.*

### Key Metrics
| Metric | Formula | Meaning |
|--------|---------|---------|
| **Support** | freq(X) / total | How often X appears |
| **Confidence** | freq(X∪Y) / freq(X) | How often X → Y is correct |
| **Lift** | Confidence / Support(Y) | Strength of the rule |

### Example 1 — Market Basket Analysis
```
python apriori/apriori_market.py
```
Analyzes 10 supermarket transactions to discover which products are bought together.

**Key Rule Found:**
```
{'eggs'} → {'milk'}    Confidence: 100.0%   Lift: 1.25x
{'butter'} → {'milk'}  Confidence: 71.4%    Lift: 0.89x
```

### Example 2 — Medical Symptom Analysis
```
python apriori/apriori_medical.py
```
Analyzes 15 patient records to find symptom-diagnosis associations.

**Key Rule Found:**
```
{'cough', 'fever'} → {'flu'}   Confidence: 100.0%   Lift: 1.88x
```
Patients with both cough AND fever are very likely diagnosed with flu.

---

## 3. 🧬 Genetic Algorithm (Evolution-Inspired)

### What is a Genetic Algorithm?
A **Genetic Algorithm (GA)** is a metaheuristic optimization algorithm inspired by Charles Darwin's theory of **natural selection**. It evolves a population of candidate solutions toward better solutions over generations.

### How It Works
```
1. INITIALIZATION  → Generate random population of solutions
2. SELECTION       → Choose fittest individuals (tournament/roulette)
3. CROSSOVER       → Combine two parents to produce offspring
4. MUTATION        → Randomly alter genes to maintain diversity
5. REPEAT          → Until convergence or max generations reached
```

### Why Genetic Algorithms?
GAs are useful when:
- The search space is **too large** for exhaustive search
- The problem has **no known derivative** (unlike gradient descent)
- Solutions are **complex structures** (routes, configurations, etc.)

### Example 1 — Traveling Salesman Problem (TSP)
```
python genetic/ga_tsp.py
```
Evolves the optimal visiting route across 8 Philippine cities to minimize total travel distance.

**Sample Output:**
```
📈 Generation 0:    39.53 units
📈 Generation 100:  38.97 units

🏆 BEST ROUTE: Manila → Batangas → Iloilo → Cebu → Zamboanga → Davao → Leyte → Cagayan → Manila
📏 Total Distance: 38.97 units
```

### Example 2 — Mathematical Function Optimization
```
python genetic/ga_optimization.py
```
Uses GA to find the maximum of `f(x) = -x² + 10x + 5` in range `[-5, 15]`.

**Sample Output:**
```
🏆 RESULT:
  Best x found : 5.000003
  f(best x)    : 30.000000
  True maximum : x=5.0, f(5)=30.0
  Error        : 0.000003

✅ GA successfully located the function maximum!
```

---

## ⚙️ Requirements

- Python 3.7+
- No external libraries required (uses only `heapq`, `math`, `random`, `itertools` from standard library)

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/algorithm-design.git
cd algorithm-design

# Run any example directly
python astar/astar_maze.py
python astar/astar_cities.py
python apriori/apriori_market.py
python apriori/apriori_medical.py
python genetic/ga_tsp.py
python genetic/ga_optimization.py
```

---

## 📚 Summary Table

| Algorithm | Type | Use Case | Time Complexity |
|-----------|------|----------|----------------|
| A* | Pathfinding | Maps, Games, GPS | O(b^d) |
| Apriori | Data Mining | Recommendations, Medical | O(2^n) worst case |
| Genetic Algorithm | Metaheuristic | Optimization, NP-Hard problems | O(g × p × f) |

---

*Submitted for Algorithm Design & Analysis — USM BSCS*
