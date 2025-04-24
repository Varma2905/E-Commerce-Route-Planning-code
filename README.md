# E-Commerce-Route-Planning-code
🧭 Hamiltonian Cycle Visualizer
This Python script finds a Hamiltonian Cycle in a user-provided undirected graph using Backtracking. It also visualizes the step-by-step traversal using networkx and matplotlib.

📌 Features
Accepts input as an adjacency matrix.

Uses backtracking to find a Hamiltonian cycle (if it exists).

Visualizes the progress of the search step-by-step.

🛠️ Requirements
Make sure you have Python and the following libraries installed:

bash
Copy
Edit
pip install matplotlib networkx
🚀 How to Run
Save the script as hamiltonian_cycle.py.

Run it:

bash
Copy
Edit
python hamiltonian_cycle.py
Enter the number of vertices and the adjacency matrix when prompted.

Example input:

pgsql
Copy
Edit
Enter the number of vertices (e.g., 5): 5
Enter the adjacency matrix row by row (space separated 0/1 values):
Row 1: 0 1 1 0 1
Row 2: 1 0 1 1 0
Row 3: 1 1 0 1 0
Row 4: 0 1 1 0 1
Row 5: 1 0 0 1 0
📈 Output
Prints the Hamiltonian Cycle if found.

Shows a step-by-step graph visualization of the search process.
