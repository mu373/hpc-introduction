import sys
import os
import networkx as nx
import pandas as pd
import numpy as np

# Create the list of all p values we want to test
# [0.0, 0.1, ..., 1.0]
p_values = [i / 10.0 for i in range(11)] 

def run_simulation(task_id, n_nodes, n_simulations):
    """
    Runs ER graph simulations for (n_simulations) times for a specific parameter value. Results are collected into a pandas DataFrame and saved to a single CSV file.

    Parameters
    ----------
    task_id : int
        The SLURM array task ID, which determines the specific p value to use.
    n_nodes : int
        Number of nodes in the ER graph.
    n_simulations : int
        Number of simulation (replications) to run for a specified p value.
    
    Returns
    -------
    None

    """

    # --- 1. Determine Parameters for this Job ---

    # Select the p for this specific job using the task_id as an index
    # (task_id is 1-based, so we subtract 1 for 0-based list index)
    try:
        p_this_job = p_values[task_id - 1]
    except IndexError:
        print(f"Error: Task ID {task_id} is out of bounds for p_values list.")
        sys.exit(1)

    print(f"This job will run {n_simulations} simulations for p = {p_this_job:.1f}")

    # --- 2. Run simulations and Collect Results ---
    # Create an empty list to store the results of each replication
    results_list = []

    for i in range(n_simulations):
        # Generate the ER graph
        G = nx.erdos_renyi_graph(n=n_nodes, p=p_this_job)

        # Calculate metrics
        avg_clustering = nx.average_clustering(G)
        avg_degree = np.mean([deg for node, deg in dict(G.degree()).items()])
        
        # Append results for this replication as a dictionary to our list
        results_list.append({
            'p': p_this_job,
            'trial_id': i,
            'avg_clustering': avg_clustering,
            'avg_degree': avg_degree
        })

    # --- 3. Save All Results to CSV using pandas ---
    # Convert the list of dictionaries to a pandas DataFrame
    results_df = pd.DataFrame(results_list)

    # Define the output file path
    # Output path: results/p_<p_value>.csv
    output_dir = "results"
    output_filename = os.path.join(output_dir, f"p_{p_this_job:.1f}.csv")

    # Write the DataFrame to a CSV file.
    results_df.to_csv(output_filename, index=False)

    print(f"Finished. Results for {len(results_df)} trials saved to {output_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python er_simulation_final.py <SLURM_ARRAY_TASK_ID>")
        sys.exit(1)

    try:
        task_id = int(sys.argv[1])
    except ValueError:
        print(f"Error: Task ID must be an integer. Received: {sys.argv[1]}")
        sys.exit(1)

    # Define fixed simulation parameters
    N_NODES = 1000
    N_SIMULATIONS = 100 # We repeat the simulation 100 times for each p value

    # Run the main function
    run_simulation(task_id=task_id, n_nodes=N_NODES, n_simulations=N_SIMULATIONS)