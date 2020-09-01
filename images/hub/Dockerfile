FROM jupyterhub/k8s-hub:0.9.0-n164.h60d45c1
LABEL maintainer="NCAR XDev Team <xdev@ucar.edu>"

RUN \
  python3 -m pip install git+https://github.com/andreas-h/sshauthenticator.git@v0.1 \
                         git+https://github.com/jupyterhub/batchspawner.git         \
                         git+https://github.com/jupyterhub/wrapspawner.git          \
                         git+https://github.com/nersc/sshspawner.git


CMD ["jupyterhub", "--config", "/etc/jupyterhub/jupyterhub_config.py", "--debug"]
