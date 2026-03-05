"""
Apriori Algorithm - Example 1: Market Basket Analysis
=======================================================
Discovers frequent itemsets and association rules
from supermarket transaction data.

Author: Vincent Patrick O. Estrera 
Subject: Algorithm Design
"""

from itertools import combinations


def get_itemsets(transactions, size):
    """Generate all candidate itemsets of given size."""
    items = set()
    for t in transactions:
        items.update(t)
    if size == 1:
        return [frozenset([i]) for i in sorted(items)]
    # Generate from frequent (size-1) sets — called in loop below
    return None


def get_support(itemset, transactions):
    count = sum(1 for t in transactions if itemset.issubset(t))
    return count / len(transactions)


def apriori(transactions, min_support=0.4, min_confidence=0.6):
    # Step 1: Find frequent 1-itemsets
    all_items = sorted(set(item for t in transactions for item in t))
    frequent = {}
    k1 = [frozenset([i]) for i in all_items]
    freq_k = [s for s in k1 if get_support(s, transactions) >= min_support]
    for s in freq_k:
        frequent[s] = get_support(s, transactions)

    current_freq = freq_k
    k = 2

    # Step 2: Generate larger itemsets
    while current_freq:
        candidates = set()
        for a, b in combinations(current_freq, 2):
            union = a | b
            if len(union) == k:
                candidates.add(union)

        next_freq = []
        for c in candidates:
            sup = get_support(c, transactions)
            if sup >= min_support:
                frequent[c] = sup
                next_freq.append(c)

        current_freq = next_freq
        k += 1

    # Step 3: Generate association rules
    rules = []
    for itemset in frequent:
        if len(itemset) < 2:
            continue
        for size in range(1, len(itemset)):
            for antecedent in combinations(itemset, size):
                ant = frozenset(antecedent)
                con = itemset - ant
                if not con:
                    continue
                conf = frequent[itemset] / frequent.get(ant, 1)
                if conf >= min_confidence:
                    lift = conf / frequent.get(con, 1)
                    rules.append((ant, con, frequent[itemset], conf, lift))

    return frequent, rules


# ── Supermarket transactions ──────────────────────────
transactions = [
    {"bread", "butter", "milk"},
    {"bread", "butter"},
    {"bread", "milk", "eggs"},
    {"butter", "milk"},
    {"bread", "butter", "milk", "eggs"},
    {"bread", "butter"},
    {"milk", "eggs"},
    {"bread", "milk"},
    {"butter", "milk", "eggs"},
    {"bread", "butter", "milk"},
]

if __name__ == "__main__":
    print("=" * 55)
    print("  Apriori — Example 1: Market Basket Analysis")
    print("=" * 55)
    print(f"  Transactions : {len(transactions)}")
    print(f"  Min Support  : 40%")
    print(f"  Min Confidence: 60%")

    frequent, rules = apriori(transactions, min_support=0.4, min_confidence=0.6)

    print("\n📦 FREQUENT ITEMSETS:")
    print(f"  {'Itemset':<30} {'Support':>8}")
    print("  " + "-" * 40)
    for itemset, sup in sorted(frequent.items(), key=lambda x: -x[1]):
        print(f"  {str(set(itemset)):<30} {sup*100:>6.1f}%")

    print(f"\n🔗 ASSOCIATION RULES (confidence ≥ 60%):")
    print(f"  {'Antecedent':<20} → {'Consequent':<15} {'Conf':>7} {'Lift':>7}")
    print("  " + "-" * 55)
    for ant, con, sup, conf, lift in sorted(rules, key=lambda x: -x[3]):
        print(f"  {str(set(ant)):<20} → {str(set(con)):<15} {conf*100:>6.1f}% {lift:>6.2f}x")

    print("\n💡 Key Insight:")
    print("   Customers who buy bread + butter are very likely to also buy milk!")
