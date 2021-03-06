# NCAR JupyterHub Deployment

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/NCAR/jupyterhub-deploy/docker-images-build?logo=docker&style=for-the-badge)](https://github.com/NCAR/jupyterhub-deploy/actions?query=workflow%3Adocker-images-build)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/NCAR/jupyterhub-deploy/linting?label=linting&logo=github&style=for-the-badge)](https://github.com/NCAR/jupyterhub-deploy/actions?query=workflow%3Alinting)

**Table of Contents**

- [NCAR JupyterHub Deployment](#ncar-jupyterhub-deployment)
  - [Dependencies](#dependencies)
  - [Usage](#usage)

[K3d](https://github.com/rancher/k3d/) Deployment of NCAR Jupyterhub. This deployment is inspired by and adapted from [NERSC JupyterHub Deployment](https://github.com/NERSC/jupyterhub-deploy).

> k3d is a lightweight wrapper to run k3s (Rancher Lab’s minimal Kubernetes distribution) in docker. -- [k3d.io](https://k3d.io/)

## Dependencies

- docker
- arkade: https://github.com/alexellis/arkade
- invoke
- colorama
- k9s (Optional): https://github.com/derailed/k9s

Install (invoke, colorama) requirements:

```bash
python -m pip install -r requirements.txt
```

Install arkade:

```bash
# Note: you can also run without `sudo` and move the binary yourself
curl -sLS https://dl.get-arkade.dev | sudo sh
```

## Usage

```bash
$ invoke --list
Available tasks:

  cluster.create      Create a Kubernetes cluster.
  cluster.delete      Delete kubernetes cluster.
  dashboard.install   Install kubernetes-dashboard
  dashboard.proxy     Forward the dashboard to the local machine
  dashboard.token     Get token for loggin in.
  dep.install         Install required CLI applications for working with Kubernetes.
  hub.delete          Delete JupyterHub install.
  hub.install         Install JupyterHub Helm chart.
  hub.upgrade         Apply changes to the hub deployment.
  images.build        Build docker images.
```
