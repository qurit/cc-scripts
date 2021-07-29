# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin
export PATH

# Path to directory containing the Duetto toolbox
DUETTOROOT=/home/jtang1/projects/def-curibe/duetto;

# Path to Duetto hdf5 plugin library
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${DUETTOROOT}/io/rdf/hdf5_plugin_library/;
HDF5_PLUGIN_PATH=${DUETTOROOT}/io/rdf/hdf5_plugin_library/;
export LD_LIBRARY_PATH;
export HDF5_PLUGIN_PATH;

