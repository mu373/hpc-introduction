# Introduction to HPC

## Overview
This repository includes sample codes for the NetSI PhD Bootcamp 2025 session.
- Title: "Introduction to High-Performance Computing"
- Presentor/Author: [Minami Ueda](https://minamiueda.com/)
- Date: August 27, 2025
- Venue: [Network Science Institute](https://www.networkscienceinstitute.org/)

## Goals for this session
- Get familiar with the concept of parallel computation and HPC clusters
- Understand how to use modules and conda, and submit jobs with Slurm.

## Contents

1. Introduction
    - What is HPC and why?
    - System overview
    - Core concepts
        - Nodes: Login node and computing node
        - Partition
        - Job, job array
    - Slurm: job manager
    - Open OnDemand
1. Environment setup
    - Setup VSCode
    - Connect to Explorer with SSH
    - Basic Linux commands
    - Clone repository from GitHub
1. Batch jobs on Slurm
    - Slurm job file
    - Slurm commands
1. Managing softwares and environments
    - Enviroment modules `module`
    - Anaconda
1. Running simulations in parallel
    - ER graph simulation for different $p$ value
1. Best practices

## Codes
```txt
├── chapter3_slurm
│   ├── hello_cluster.py
│   └── job.sh
├── chapter5_parallel
│   ├── job_plot.sh      # Slurm batch file for plotting results
│   ├── job_sim.sh       # Slurm batch file for ER graph simulations
│   ├── plot.py          # Python script to plot results from CSV
│   └── sim.py           # Python script to simulate ER graphs with different p-values
├── LICENSE
└── README.md
```