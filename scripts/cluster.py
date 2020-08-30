from invoke import task

from .common import _print_command, _prompt


@task(
    help={
        'name': 'Name of the kubernetes cluster',
        'agents': 'How many agents you want to create',
        'servers': 'How many servers you want to create',
        'api-port': 'The Kubernetes API server port exposed on the LoadBalancer',
        'port': 'Map ports from the node containers to the host',
    }
)
def create(
    c, name='jhub', agents=3, servers=1, api_port=6550, port='8080:80@loadbalancer'
):
    'Create a Kubernetes cluster.'

    command = (
        f'k3d cluster create {name} --api-port {api_port} '
        f'--servers {servers} --agents {agents} --port {port} '
        '--k3s-server-arg "--no-deploy=traefik" --wait'
    )

    _print_command(command)
    if _prompt():
        c.run(command)
