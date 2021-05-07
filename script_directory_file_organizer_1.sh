#!/bin/bash

# ===== PBS OPTIONS =====
### Set the job name
#PBS -N Jmoe_script
### Specify queue to run in
#PBS -q copperhead
### Specify number of CPUs for job
#PBS -l nodes=1:ppn=1,mem=8GB
### Specify runtime
#PBS -l walltime=8:00:00

# ==== Main ======
python script_directory_file_organizer_1.py