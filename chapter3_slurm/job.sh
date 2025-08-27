#!/bin/bash
#============ Slurm Options ===========
#SBATCH --job-name=hello-cluster
#SBATCH --partition=express
#SBATCH --time=0-00:01:00

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

#SBATCH --mail-user=YOUR_USER_NAME@northeastern.edu
#SBATCH --mail-type=END
#=======================================

# Load required module 
module load anaconda3

# Activate any necessary environments
source activate base

# Run program of interest here!
python3 hello_cluster.py
