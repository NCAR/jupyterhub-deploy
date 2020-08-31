# NCAR JupyterHub Deployment

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/NCAR/jupyterhub-deploy/CI?logo=docker&style=for-the-badge)](<[df](https://github.com/NCAR/jupyterhub-deploy/actions?query=workflow%3ACI)>)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/NCAR/jupyterhub-deploy/linting?label=linting&logo=github&style=for-the-badge)](https://github.com/NCAR/jupyterhub-deploy/actions?query=workflow%3Alinting)

**Table of Contents**

- [NCAR JupyterHub Deployment](#ncar-jupyterhub-deployment)
  - [Requirements](#requirements)
  - [Usage](#usage)

[K3d](https://github.com/rancher/k3d/) Deployment of NCAR Jupyterhub. This deployment is inspired by and adapted from [NERSC JupyterHub Deployment](https://github.com/NERSC/jupyterhub-deploy).

> k3d is a lightweight wrapper to run k3s (Rancher Lab’s minimal Kubernetes distribution) in docker. -- [k3d.io](https://k3d.io/)

## Requirements

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
$ invoke --list
Available tasks:

  cluster.create      Create a Kubernetes cluster.
  dashboard.install   Install kubernetes-dashboard
  dashboard.proxy     Forward the dashboard to the local machine
  dashboard.token     Get token for loggin in.
  hub.install         Install JupyterHub Helm chart.
  images.build        Build docker images.
```
