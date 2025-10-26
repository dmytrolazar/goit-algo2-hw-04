import networkx as nx
import pandas as pd

# Створюємо граф
G = nx.DiGraph()

# Додаємо ребра та їх пропускні здатності
edges = [
    ("Термінал 1", "Склад 1", 25), ("Термінал 1", "Склад 2", 20), ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15), ("Термінал 2", "Склад 4", 30), ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15), ("Склад 1", "Магазин 2", 10), ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15), ("Склад 2", "Магазин 5", 10), ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20), ("Склад 3", "Магазин 8", 15), ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20), ("Склад 4", "Магазин 11", 10), ("Склад 4", "Магазин 12", 15), ("Склад 4", "Магазин 13", 5), ("Склад 4", "Магазин 14", 10)
]

G.add_weighted_edges_from(edges, weight='capacity')

# Формуємо таблицю результатів
results = []
for terminal, shop in [(x, y) for x in [n for n in G.nodes if str(n).startswith('Термінал')] for y in [n for n in G.nodes if str(n).startswith('Магазин')]]:
    if nx.has_path(G, terminal, shop):
        flow, _ = nx.maximum_flow(G, terminal, shop, flow_func=nx.algorithms.flow.edmonds_karp)
        results.append((terminal, shop, flow))
df_results = pd.DataFrame(results, columns=["Термінал", "Магазин", "Фактичний Потік (одиниць)"])

# Відображаємо результати
print(df_results)
