from collections import defaultdict, deque
import time

# Currencies are like weighted edges in a graph from one currency node to another
# For finding optimal "path" in graph, we might be able to use:
# - Djikstra's algorithm
# - Bellman-Ford algorithm
# - Floyd-Warshall algorithm

# Based on how each works we can start crossing some out. Djikstra's algorithm will
# probably not be too helpful because of its greedy nature. It will find the min/max
# currency path at the current time, but it won't be able to take into account future
# negative weights/cycles where we are able to find an arbitrage opportunity.

# Floyd-Warshall is a good candidate and might work because it essentially checks every
# possible path between two nodes and updates our distance/currency at using this path for every
# other node. It can also detect negative cycles which is a plus for our goal in this problem.
# This will end up being O(currencies^3) which becomes pretty inefficient for > 100.

# Bellman-Ford gives us the best of both worlds in a sense. It is able to work for negative
# weights/cycles unlike Djiksta's and it doesn't do excessive computations like Floyd-Warshall, so it
# might be the best choice for this problem.

usd_to_eur = 0.90
eur_to_jpy = 135.00
jpy_to_usd = 0.0085

def arbitrage_bf(edges, start_currency, start_amount) -> str:
    graph = defaultdict(dict)
    for fro, to, rate in edges:
        graph[fro][to] = rate

    exchange = {start_currency: start_amount}
    # longest possible path in graph with n nodes could be n-1 edges
    # longest path visiting each node once to cycle back to start is n-1+1 = n edges
    for _ in range(len(graph)):
        for fro in graph:
            if fro not in exchange:
                continue
            for to in graph[fro]:
                if exchange.get(to, 0) < exchange[fro] * graph[fro][to]:
                    exchange[to] = exchange[fro] * graph[fro][to]
                    if to == start_currency:
                        return f"Arbitrage Opportunity Exists. {start_currency}: {start_amount = }, end_amount = {exchange[to]}"

    return "No Arbitrage Opportunity Exists"

edges = [
    ("USD", "EUR", usd_to_eur),
    ("EUR", "JPY", eur_to_jpy),
    ("JPY", "USD", jpy_to_usd),
]

# If arbitrage opportunity exists, it can be spammed to make infinite money glitch
# We can limit how many exchanges we make to be more realistic, and then find the best arbitrage
# opportunity for this limit.
# Modified SPFA based off Bellman-Ford to not traverse all edges and track the number of exchanges
def arbitrage_spfa(edges, start_currency, start_amount, max_exchanges=None) -> str:
    graph = defaultdict(dict)
    for fro, to, rate in edges:
        graph[fro][to] = rate

    exchange = {start_currency: start_amount}
    q = deque([start_currency])

    best_profit, cycle = start_amount, False
    exchanges_left = max_exchanges if max_exchanges is not None else len(graph)

    while q and exchanges_left:
        exchanges_left -= 1
        next_exchange = exchange.copy()
        for _ in range(len(q)):
            fro = q.popleft()

            for to in graph[fro]:
                curr_money = exchange[fro] * graph[fro][to]
                if next_exchange.get(to, 0) < curr_money:
                    next_exchange[to] = curr_money

                    if to == start_currency and curr_money > best_profit:
                        best_profit = curr_money
                        cycle = True
                    q.append(to)

        exchange = next_exchange

    return (
        f"Arbitrage Opportunity Exists. {start_currency}: start_amount = {start_amount}, end_amount = {best_profit}"
        if cycle
        else "No Arbitrage Opportunity Exists"
    )

# My first function would give a lesser arbitrage opportunity for this testcase than the second function
# edges = [
#     ("USD", "EUR", 0.5),
#     ("EUR", "USD", 2.1),
#     ("USD", "JPY", 0.5),
#     ("JPY", "USD", 2.2),
# ]

# Final thing I can think of is if we want to find the best arbitrage given that we cannot
# spam infinite money glitch, but also given that we might be able to find many negative cycles/arbitrages
# in the path from a currency to itself.
# Example: USD -> EUR -> GBP -> . . . -> USD
#                  ^      ^
#                 +|     +|
#                  v      v
#                 JPY    FRA
# If we increase our limitation to being able to visit each currency twice, we can find the best
# arbitrage/path to take using a dfs. Although it gets computationally expensive with more currencies,
# we might be able to implement some sort of caching to make it more effective
def arbitrage_dfs(edges, start_currency, start_amount) -> str:
    graph = defaultdict(dict)
    for fro, to, rate in edges:
        graph[fro][to] = rate

    best_profit = start_amount
    seen = defaultdict(int)
    seen[start_currency] = 1
    
    def dfs(fro, amount):
        nonlocal best_profit
        if fro == start_currency and seen[fro] == 2:
            best_profit = max(best_profit, amount)
            return

        for to in graph[fro]:
            if seen[to] < 2:
                seen[to] += 1
                dfs(to, amount * graph[fro][to])
                seen[to] -= 1

    dfs(start_currency, start_amount)
    return (
        f"Arbitrage Opportunity Exists. {start_currency}: start_amount = {start_amount}, end_amount = {best_profit}"
        if best_profit > start_amount
        else "No Arbitrage Opportunity Exists"
    )

# edges = [
#     ("USD", "EUR", 1.1),
#     ("EUR", "JPY", 1.1),
#     ("EUR", "USD", 1.1),  # lower arbitrage opportunity
#     ("JPY", "EUR", 1.1),
#     ("EUR", "GBR", 1.1),
#     ("GBR", "FRA", 1.1),
#     ("FRA", "GBR", 1.1),
#     ("GBR", "USD", 1.1),  # max arbitrage opportunity
# ]

# start_currency, start_amount = "USD", 1000 # 1032.75
# start_currency, start_amount = "EUR", 500 # 516.375
# start_currency, start_amount = "JPY", 250.39 # 258.5902725

# Bellman-Ford
print("Bellman-Ford:")
t1 = time.time()
print(arbitrage_bf(edges, start_currency, start_amount))
print("Time:", time.time() - t1, "\n")

# Modified SPFA + Bellman-Ford
print("SPFA:")
t1 = time.time()
print(arbitrage_spfa(edges, start_currency, start_amount))
print("Time:",time.time() - t1, "\n")

# DFS
print("DFS:")
t1 = time.time()
print(arbitrage_dfs(edges, start_currency, start_amount))
print("Time:", time.time() - t1, "\n")
