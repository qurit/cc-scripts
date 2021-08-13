import sys
import os
import itertools
import datetime
import glob

assert sys.version_info >= (3,7), "Python 3.7 is required for dictionaries to maintain order."
#(Some implementations of Python 3.6 might satisfy this too, but it is
# a specification in 3.7.)

print(os.getcwd())

fileOpts = {
    "petDataDir": [
        # "/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/1m/",
        # "/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/2m/",
        # "/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/5m/",
        "/project/6053072/jtang1/jt_unlist/lymph-piq-withBkg/10m/"
    ],
    "attenDataDir": ["/project/6053072/phantoms/Lymphoma_quantification/LYMPH_PIQ/WithBkg/CTAC/"],
    "reconAlgorithm": ["OSEM"]
}

userConfig = {
    # "nX": [192, 256],
    # "zFilter": [2, 4, 6],
    # "beta": [200, 600]
}

slurmOpts = {
    "account": "def-curibe",
    "time": "5:00:00",
    "ntasks": 1,
    "cpus-per-task": 2,
    "mem-per-cpu": "4G",
    "mail-user": "jitang@bccrc.ca",
    "mail-type": "ALL"
}

def tupleToDict(tpl: tuple, sourceDict: dict):
    keys = list(sourceDict.keys())
    retDict = {}
    for i in range(len(tpl)):
        retDict[keys[i]] = tpl[i]
    return retDict

def getNumFoldersWithPrefix(prefix):
    return len(glob.glob(f"{prefix}*"))

def getNewFolderName(prefix):
    return f"{prefix}_{getNumFoldersWithPrefix(prefix)}"

containerFolderPrefix = f"{datetime.datetime.now().strftime('%Y%m%d')}"
containerFolderName = getNewFolderName(containerFolderPrefix)
print(containerFolderName)

#bashLines = ["#!/bin/bash"]
#counter = 0
#for fileOptTpl in itertools.product(*fileOpts.values()):
#    for configTpl in itertools.product(*userConfig.values()):
#        counter += 1
#        fOpt = tupleToDict(fileOptTpl, fileOpts)
#        cOpt = tupleToDict(configTpl, userConfig)
#
#        scanDuration = fOpt["petDataDir"].split('/')[-2]
#        # print(scanDuration)
#
#        # folderPattern = f"recon_{fOpt['reconAlgorithm']}_{scanDuration}_z{cOpt['zFilter']}_b{cOpt['beta']}_{datetime.datetime.now().strftime('%Y%m%d')}"
#        folderPattern = f"recon_{fOpt['reconAlgorithm']}_nIt{cOpt['nIterations']}_{datetime.datetime.now().strftime('%Y%m%d')}"
#
#        numExistingFolders = len(glob.glob(f"{folderPattern}*"))
#
#        folderName = f"{folderPattern}_{numExistingFolders}"
#        jobName = f"{fOpt['reconAlgorithm']}_nIt{cOpt['nIterations']}"
#        seriesName = jobName
#
#        print(folderName)
#        os.mkdir(folderName)
#
#        mFileLines = [f'disp("Hello from {folderName}/runDuetto.m")', "workDir = pwd;"]
#        mFileLines.extend([f"{k} = '{v}';" for k, v in fOpt.items()])
#        
#        mFileLines.append("userConfig = ptbUserConfig(reconAlgorithm, petDataDir, attenDataDir, workDir);")
#        for k, v in cOpt.items():
#            if type(v) == str:
#                mFileLines.append(f"userConfig.{k} = '{v}';")
#            elif type(v) == int:
#                mFileLines.append(f"userConfig.{k} = {v};")
#            else:
#                raise TypeError("userConfig options must be of type str or int")
#
#        mFileLines.append(f"userConfig.dicomSeriesNumber = {700+counter};")
#        mFileLines.append(f"userConfig.dicomSeriesDesc = '{seriesName}';")
#        mFileLines.append(f"reconImage = ptbRunRecon(userConfig);")
#
#        with open(os.path.join(folderName, "runDuetto.m"), "w", newline='\n') as f:
#            f.write("\n".join(mFileLines))
#        
#        slFileLines = ["#!/bin/bash -l", f"#SBATCH --job-name={jobName}"]
#        slFileLines.extend([f"#SBATCH --{k}={v}" for k, v in slurmOpts.items()])
#        slFileLines.extend([
#            "module load nixpkgs/16.09",
#            "module load matlab/2018a",
#            'matlab -nodisplay -r "runDuetto"'
#        ])
#
#        with open(os.path.join(folderName, "recon.sl"), "w", newline='\n') as f:
#            f.write("\n".join(slFileLines))
#
#        bashLines.extend([
#            f"cd {folderName}",
#            "sbatch recon.sl",
#            "cd ..",
#            "sleep 3" #seconds; sleeping is recommended by Compute Canada to maintain responiveness of Slurm for all users.
#        ])
#
#bashScriptPrefix = f"submit_jobs_{datetime.datetime.now().strftime('%Y%m%d')}_"
#numExistingScripts = len(glob.glob(f"{bashScriptPrefix}*.sh"))
#with open(f"{bashScriptPrefix}{numExistingScripts}.sh", 'w', newline='\n') as f:
#    f.write("\n".join(bashLines))
