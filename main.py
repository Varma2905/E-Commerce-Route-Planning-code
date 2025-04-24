import networkx as nx
import matplotlib.pyplot as plt
import time

# Get graph input from user
V = int(input("Enter the number of vertices (e.g., 5): "))
print("Enter the adjacency matrix row by row (space separated 0/1 values):")

graph = []
for i in range(V):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != V:
        print("Error: Row must have", V, "elements.")
        exit()
    graph.append(row)

path = [-1] * V
steps = []  # To store the route progress step-by-step

def is_safe(v, pos):
    if graph[path[pos - 1]][v] == 0 or v in path:
        return False
    return True

def ham_cycle_util(pos):
    if pos == V:
        if graph[path[pos - 1]][path[0]] == 1:
            steps.append(path[:pos] + [path[0]])  # Final cycle
            return True
        return False

    for v in range(1, V):
        if is_safe(v, pos):
            path[pos] = v
            steps.append(path[:pos+1])
            if ham_cycle_util(pos + 1):
                return True
            path[pos] = -1  # Backtrack
    return False

def ham_cycle():
    path[0] = 0
    steps.append([0])
    if not ham_cycle_util(1):
        print("No Hamiltonian Cycle found.")
        return False
    print("Hamiltonian Cycle:", steps[-1])
    draw_step_by_step_graph(steps)
    return True

def draw_step_by_step_graph(steps):
    G = nx.Graph()

    # Add all edges from adjacency matrix
    for i in range(V):
        for j in range(i, V):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G, seed=42)

    for i, step in enumerate(steps):
        plt.clf()  # Clear figure

        # Draw base graph
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')

        # Draw current path step
        if len(step) > 1:
            edge_list = [(step[j], step[j+1]) for j in range(len(step) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=3)

        plt.title(f"Step {i+1}: {step}")
        plt.pause(1.0)  # Pause between steps

    plt.show()

# Run the algorithm
ham_cycle()
