#!/bin/bash -l
#SBATCH --job-name=recon
#SBATCH --account=def-curibe   # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=3:00:00        # adjust this to match the walltime of your job      
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=6000M             # adjust this according to the memory requirement per node you need
#SBATCH --mail-user=jitang@bccrc.ca # adjust this to match your email address
#SBATCH --mail-type=ALL

# Choose a version of MATLAB by loading a module:

module load nixpkgs/16.09
module load matlab/2018a

matlab -nodisplay -r "runScript_PETCT"