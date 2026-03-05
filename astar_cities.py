"""
A* Algorithm - Example 2: City Route Finder (Graph-based)
==========================================================
Simulates GPS routing between cities using A*.
Each city has (x, y) coordinates used for heuristic distance.

Author: Binsoy
Subject: Algorithm Design
"""

import heapq
import math

# City coordinates (for heuristic — straight-line distance)
CITIES = {
    "Manila":    (0,  0),
    "Laguna":    (1, -2),
    "Batangas":  (0, -4),
    "Quezon":    (3,  1),
    "Camarines": (6,  0),
    "Albay":     (8, -1),
    "Sorsogon":  (9, -2),
    "Davao":     (15,-5),
}

# Road connections: (city_a, city_b, distance_km)
ROADS = [
    ("Manila",    "Laguna",    54),
    ("Manila",    "Quezon",    140),
    ("Laguna",    "Batangas",  61),
    ("Laguna",    "Quezon",    100),
    ("Quezon",    "Camarines", 220),
    ("Batangas",  "Camarines", 300),
    ("Camarines", "Albay",     100),
    ("Albay",     "Sorsogon",  60),
    ("Sorsogon",  "Davao",     900),
]


def build_graph(roads):
    graph = {}
    for a, b, dist in roads:
        graph.setdefault(a, []).append((b, dist))
        graph.setdefault(b, []).append((a, dist))
    return graph


def euclidean_heuristic(city, goal, coords):
    x1, y1 = coords[city]
    x2, y2 = coords[goal]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) * 60  # scale to km estimate


def astar_cities(graph, coords, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path, node = [], current
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + euclidean_heuristic(neighbor, goal, coords)
                heapq.heappush(open_set, (f, neighbor))

    return None, float('inf')


if __name__ == "__main__":
    print("=" * 50)
    print("  A* Algorithm — Example 2: City Route Finder")
    print("=" * 50)

    graph = build_graph(ROADS)
    start, goal = "Manila", "Davao"

    print(f"\n📍 Finding shortest route: {start} → {goal}\n")
    path, total_km = astar_cities(graph, CITIES, start, goal)

    if path:
        print("✅ Optimal Route Found!")
        print("   " + " → ".join(path))
        print(f"\n📏 Total Distance: {total_km} km")

        print("\n--- Step-by-step ---")
        for i in range(len(path) - 1):
            a, b = path[i], path[i+1]
            for x, y, d in ROADS:
                if (x == a and y == b) or (x == b and y == a):
                    print(f"   {a:<12} → {b:<12}  {d} km")
    else:
        print("❌ No route found.")
