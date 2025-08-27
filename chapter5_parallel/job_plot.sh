#!/bin/bash
#================== Slurm Options ==================
#SBATCH --job-name=er-plot
#SBATCH --partition=express
#SBATCH --time=0-00:01:00

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

#SBATCH --mail-user=YOUR_USER_NAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#===================================================

# ---------- Parameters ----------
INPUT_DIR="results"       # Directory containing p_*.csv files
OUT_DIR="figs"            # Directory for figures and summary CSV
PYTHON_SCRIPT="plot.py"   # Analysis script to execute
# --------------------------------------------------


# --- Environment Setup ---
mkdir -p logs results figs

# Load required module 
module load anaconda3

# Activate your project environment
source activate /home/ueda.m/conda/bootcamp

# --- Sanity checks ---
if [[ ! -f "${PYTHON_SCRIPT}" ]]; then
  echo "Error: ${PYTHON_SCRIPT} not found in $(pwd)" >&2
  exit 1
fi

if ! compgen -G "${INPUT_DIR}/p_*.csv" > /dev/null; then
  echo "Error: No CSV files found under ${INPUT_DIR}/p_*.csv" >&2
  exit 1
fi

# --- Run analysis ---
echo "[$(date)] Running: python ${PYTHON_SCRIPT} --input-dir ${INPUT_DIR} --out-dir ${OUT_DIR} --n-nodes ${N_NODES}"
python3 "${PYTHON_SCRIPT}" --input-dir "${INPUT_DIR}" --out-dir "${OUT_DIR}" --n-nodes "${N_NODES}"

echo "[$(date)] Job finished. Outputs written to ${OUT_DIR}"

