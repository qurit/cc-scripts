#!/bin/bash -l
#SBATCH --job-name=mlab_unlist
#SBATCH --account=def-curibe
#SBATCH --time=2:30:00         # adjust this to match the walltime of your job
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1      # adjust this if you are using parallel commands
#SBATCH --mem-per-cpu=16G             # adjust this according to the memory requirement per node you need
#SBATCH --mail-user=jitang@bccrc.ca # adjust this to match your email address
#SBATCH --mail-type=ALL

module load nixpkgs/16.09
module load matlab/2018a

matlab -nodisplay -r "unlistStatic"
