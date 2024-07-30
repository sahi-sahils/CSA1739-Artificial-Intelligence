from collections import deque

def water_jug_problem(capacity_jug4, capacity_jug3, target):
    visited_states = set()
    queue = deque([(0, 0)])

    while queue:
        jug4, jug3 = queue.popleft()

        if (jug4, jug3) == target:
            print("Steps:", [(0, 0)] + list(visited_states))
            return

        visited_states.add((jug4, jug3))

        # Fill jug4
        queue.append((capacity_jug4, jug3))

        # Pour water from jug3 to jug4
        pour_jug3_to_jug4 = (min(capacity_jug4, jug4 + jug3), max(0, jug3 - (capacity_jug4 - jug4)))
        queue.append(pour_jug3_to_jug4)

        # Empty jug3
        queue.append((jug4, 0))

    print(f"Cannot get exactly {target} gallons in the {capacity_jug4}-gallon jug.")

# Example: Get exactly 2 gallons in the 4-gallon jug and 0 gallons in the 3-gallon jug
water_jug_problem(4, 3, (2, 0))
