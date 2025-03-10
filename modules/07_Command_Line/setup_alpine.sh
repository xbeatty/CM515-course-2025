#!/usr/bin/env bash

module purge
module load miniforge

# make the special conda configuration to /projects if the user has not done so
EID=${USER/@colostate.edu/}
ENV_DIRS="/projects/.colostate.edu/$EID/software/anaconda/envs"
PKG_DIRS="/projects/.colostate.edu/$EID/.conda_pkgs"
conda config --get envs_dirs | grep -q $ENVS_DIRS || conda config --add envs_dirs "$ENV_DIRS"
conda config --get pkgs_dirs | grep -q $PKG_DIRS || conda config --add pkgs_dirs "$PKG_DIRS"

ENV_NAME=CM515

conda env create --file CM515.yaml

# finish installing the bash kernel
conda activate $ENV_NAME
#python -m bash_kernel.install

# create configuration files/directories
CONFIGPATH=/home/$USER/.local/share/jupyter/kernels/${ENV_NAME}
mkdir -p $CONFIGPATH


# again, where is their project dir?
PROJ_DIR=/projects/.colostate.edu/${EID}

if ! [ -e ${PROJ_DIR} ]
then
    PROJ_DIR=/projects/$USER
fi

(
cat <<END_HEREDOC
{
"argv": [
"${PROJ_DIR}/software/anaconda/envs/${ENV_NAME}/bin/python",
"-m",
"bash_kernel",
"-f",
"{connection_file}"
],
"display_name": "${ENV_NAME}",
"language": "bash"
}

END_HEREDOC
) > $CONFIGPATH/kernel.json


echo "done."
echo "View configuration in $CONFIGPATH"
echo "You may now launch jupyterlab from ondemand and $ENV_NAME will appear as an option to notebooks and consoles."
echo "You can make a custom logo by transferring logo32x32.png and log64x64.png to $CONFIGPATH"
