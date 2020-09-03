from invoke import task

from .common import _print_command, _prompt


@task
def install(
    c, namespace='jhub', release='jhub', version='0.9.0', values='hub/config.yaml'
):
    """Install JupyterHub Helm chart."""
    command = (
        f'kubectl create namespace {namespace} && '
        'helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/ &&  '
        'helm repo update && '
        f'helm upgrade --install {release} jupyterhub/jupyterhub '
        f'--namespace {namespace} --version {version} --values {values} --wait'
    )

    _print_command('Install JupyterHub Helm chart', command)
    if _prompt():
        c.run(command)

    command = f'kubectl get pod --namespace {namespace}'
    _print_command(f'Get pods created in namespace={namespace}', command)
    if _prompt():
        c.run(command)

    command = f'kubectl get service --namespace {namespace}'
    _print_command('Find IP and port of the JupyterHub proxy-public service', command)
    if _prompt():
        c.run(command)


@task
def delete(c, namespace='jhub', release='jhub'):
    'Delete JupyterHub install.'
    command = f'helm delete {release} && kubectl delete namespace {namespace}'
    _print_command('Delete JupyterHub install', command)
    if _prompt():
        c.run(command)
