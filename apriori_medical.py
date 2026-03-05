"""
Apriori Algorithm - Example 2: Medical Symptom-Diagnosis Analysis
==================================================================
Finds associations between symptoms appearing together
in patient records to assist in diagnosis.

Author: Vincent Patrick O. Estrera 
Subject: Algorithm Design
"""

from itertools import combinations


def get_support(itemset, transactions):
    return sum(1 for t in transactions if itemset.issubset(t)) / len(transactions)


def apriori(transactions, min_support=0.3, min_confidence=0.5):
    all_items = sorted(set(item for t in transactions for item in t))
    frequent = {}

    freq_k = [frozenset([i]) for i in all_items
               if get_support(frozenset([i]), transactions) >= min_support]
    for s in freq_k:
        frequent[s] = get_support(s, transactions)

    current_freq = freq_k
    k = 2
    while current_freq:
        candidates = {a | b for a, b in combinations(current_freq, 2) if len(a | b) == k}
        next_freq = []
        for c in candidates:
            sup = get_support(c, transactions)
            if sup >= min_support:
                frequent[c] = sup
                next_freq.append(c)
        current_freq = next_freq
        k += 1

    rules = []
    for itemset in frequent:
        if len(itemset) < 2:
            continue
        for size in range(1, len(itemset)):
            for ant_tuple in combinations(itemset, size):
                ant = frozenset(ant_tuple)
                con = itemset - ant
                if not con:
                    continue
                conf = frequent[itemset] / frequent.get(ant, 1)
                if conf >= min_confidence:
                    lift = conf / frequent.get(con, 1)
                    rules.append((ant, con, frequent[itemset], conf, lift))
    return frequent, rules


# ── Patient records: sets of symptoms/conditions ──────
patient_records = [
    {"fever", "cough", "fatigue", "flu"},
    {"fever", "cough", "flu"},
    {"fever", "headache", "flu"},
    {"cough", "fatigue", "bronchitis"},
    {"fever", "cough", "fatigue", "flu"},
    {"headache", "fatigue", "migraine"},
    {"fever", "rash", "dengue"},
    {"cough", "fatigue", "flu"},
    {"fever", "cough", "flu"},
    {"headache", "fever", "flu"},
    {"rash", "fever", "dengue"},
    {"cough", "bronchitis"},
    {"fever", "cough", "fatigue", "flu"},
    {"headache", "migraine"},
    {"fever", "rash", "dengue"},
]

if __name__ == "__main__":
    print("=" * 60)
    print("  Apriori — Example 2: Medical Symptom Analysis")
    print("=" * 60)
    print(f"  Patient Records : {len(patient_records)}")
    print(f"  Min Support     : 30%")
    print(f"  Min Confidence  : 50%")

    frequent, rules = apriori(patient_records, min_support=0.3, min_confidence=0.5)

    print("\n🩺 FREQUENT SYMPTOM COMBINATIONS:")
    print(f"  {'Symptoms/Conditions':<40} {'Support':>8}")
    print("  " + "-" * 50)
    for itemset, sup in sorted(frequent.items(), key=lambda x: (-len(x[0]), -x[1])):
        print(f"  {str(set(itemset)):<40} {sup*100:>6.1f}%")

    print(f"\n🔗 DIAGNOSTIC ASSOCIATION RULES:")
    print(f"  {'IF (Symptoms)':<28} → {'THEN (Likely)':<18} {'Conf':>7} {'Lift':>7}")
    print("  " + "-" * 65)
    for ant, con, sup, conf, lift in sorted(rules, key=lambda x: -x[3]):
        print(f"  {str(set(ant)):<28} → {str(set(con)):<18} {conf*100:>6.1f}% {lift:>6.2f}x")

    print("\n💡 Key Insight:")
    print("   Patients with fever + cough have a high probability of flu diagnosis.")
    print("   This can help doctors prioritize flu tests for such patients.")
