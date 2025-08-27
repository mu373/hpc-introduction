#!/bin/bash
#============ Slurm Options ===========
#SBATCH --job-name=er-graph-sim
#SBATCH --partition=short
#SBATCH --time=0-00:1:00

#SBATCH --array=1-11 # This is an array job with 11 tasks

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

#SBATCH --output=logs/p_value_%a.out
#SBATCH --error=logs/p_value_%a.err

#SBATCH --mail-user=YOUR_USER_NAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#=======================================

# --- Environment Setup ---
mkdir -p logs results figs

# Load required module 
module load anaconda3

# Activate your project environment
source activate /home/ueda.m/conda/bootcamp

# Run program, passing the array task ID as an argument
echo "Starting job for SLURM_ARRAY_TASK_ID: $SLURM_ARRAY_TASK_ID"
python3 sim.py $SLURM_ARRAY_TASK_ID
echo "Job finished."
