from collections import deque

class TowerPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.num_towers = len(initial_state)

        # Validation
        for tower in initial_state + goal_state:
            if sorted(tower) != tower:
                raise ValueError("Blocks in each tower must be sorted in descending order.")
    
    def bfs(self):
        queue = deque([(self.initial_state, [])])
        visited = set()

        while queue:
            current_state, moves = queue.popleft()
            state_tuple = tuple(tuple(tower) for tower in current_state)

            if state_tuple in visited:
                continue

            visited.add(state_tuple)

            if current_state == self.goal_state:
                return moves

            for i in range(self.num_towers):
                for j in range(self.num_towers):
                    if i != j and current_state[i]:
                        new_state = [list(tower) for tower in current_state]
                        new_state[j].append(new_state[i].pop())
                        queue.append((new_state, moves + [(i, j)]))
        return None

    def h_val(self, state):
        mismatches = 0
        for tower, goal_tower in zip(state, self.goal_state):
            mismatches += sum(1 for x, y in zip(tower, goal_tower) if x != y)
        return mismatches

    def greedy(self):
        from heapq import heappush, heappop

        heap = [(self.h_val(self.initial_state), self.initial_state, [])]
        visited = set()

        while heap:
            _, current_state, moves = heappop(heap)
            state_tuple = tuple(tuple(tower) for tower in current_state)

            if state_tuple in visited:
                continue

            visited.add(state_tuple)

            if current_state == self.goal_state:
                return moves

            for i in range(self.num_towers):
                for j in range(self.num_towers):
                    if i != j and current_state[i]:
                        new_state = [list(tower) for tower in current_state]
                        new_state[j].append(new_state[i].pop())
                        heappush(heap, (self.h_val(new_state), new_state, moves + [(i, j)]))
        return None

    def a_star(self):
        from heapq import heappush, heappop

        def f_val(state, g):
            return g + self.h_val(state)

        heap = [(f_val(self.initial_state, 0), 0, self.initial_state, [])]
        visited = set()

        while heap:
            _, g, current_state, moves = heappop(heap)
            state_tuple = tuple(tuple(tower) for tower in current_state)

            if state_tuple in visited:
                continue

            visited.add(state_tuple)

            if current_state == self.goal_state:
                return moves

            for i in range(self.num_towers):
                for j in range(self.num_towers):
                    if i != j and current_state[i]:
                        new_state = [list(tower) for tower in current_state]
                        new_state[j].append(new_state[i].pop())
                        heappush(heap, (f_val(new_state, g + 1), g + 1, new_state, moves + [(i, j)]))
        return None


def get_tower_input(prompt, num_towers):
    towers = []
    print(prompt)
    for i in range(num_towers):
        tower = input(f"Tower {i+1}: ").strip()
        towers.append(list(map(int, tower.split())) if tower else [])
    return towers


if __name__ == "__main__":
    num_towers = int(input("Enter the number of towers: "))
    print("Initial State:")
    initial_state = get_tower_input("Enter the blocks in each tower (space-separated):", num_towers)

    print("Goal State:")
    goal_state = get_tower_input("Enter the blocks in each tower (space-separated):", num_towers)

    puzzle = TowerPuzzle(initial_state, goal_state)

    print("\nSolving using A* Search...")
    moves = puzzle.a_star()

    if moves:
        print(f"Solved in {len(moves)} moves.")
        for move in moves:
            print(f"Move from Tower {move[0]+1} to Tower {move[1]+1}")
    else:
        print("No solution found.")
