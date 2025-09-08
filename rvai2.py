import heapq


def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        goal_index = goal.index(state[i])
        x1, y1 = i // 3, i % 3
        x2, y2 = goal_index // 3, goal_index % 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors


def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    return path[::-1]


def a_star_manhattan(initial, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial, goal), 0, initial))
    came_from = {initial: None}
    cost_so_far = {initial: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return None


def get_input():
    print("Enter the initial state (9 values from 0-8, use 0 for the blank space):")
    initial_state = tuple(map(int, input().split()))
    print("Enter the goal state (9 values from 0-8, use 0 for the blank space):")
    goal_state = tuple(map(int, input().split()))

    return initial_state, goal_state


def print_solution(path):
    if path:
        print("Solution path:")
        for step in path:
            print(step)
    else:
        print("No solution found")


if __name__ == "__main__":
    initial_state, goal_state = get_input()
    solution = a_star_manhattan(initial_state, goal_state)
    print_solution(solution)
