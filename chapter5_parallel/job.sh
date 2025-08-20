#!/bin/bash
#============ Slurm Options ===========
#SBATCH --job-name=er-graph-sim
#SBATCH --partition=short
#SBATCH --time=0-00:10:00

#SBATCH --array=1-11 # This is an array job with 11 tasks

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

#SBATCH --output=results/p_value_%a.out
#SBATCH --error=results/p_value_%a.err

#SBATCH --mail-user=YOUR_USER_NAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#=======================================

# --- Environment Setup ---
# It's good practice to create directories upfront
mkdir -p results

# Clear current env/modules
module purge

# Load required module 
module load anaconda3/2024.06

# Activate your project environment
# Replace 'hpc_workshop_env' with the name of your conda environment
source activate hpc_workshop_env

# Run program, passing the array task ID as an argument
echo "Starting job for SLURM_ARRAY_TASK_ID: $SLURM_ARRAY_TASK_ID"
python3 er_simulation.py $SLURM_ARRAY_TASK_ID
echo "Job finished."