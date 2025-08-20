#!/bin/bash
#============ Slurm Options ===========
#SBATCH --job-name=hello-cluster
#SBATCH --partition=short
#SBATCH --time=0-00:05:00

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

#SBATCH --mail-user=YOUR_USER_NAME@northeastern.edu
#SBATCH --mail-type=END
#=======================================

## Clear current env/modules
#conda deactivate
module purge

## Load required module 
module load explorer

## Activate any necessary environments
source activate base

## Run program of interest here!
python3 example1.py