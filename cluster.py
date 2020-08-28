from invoke import task


def _prompt():
    actions = {'y': True, 'n': False, 'Y': True, 'yes': True, 'N': False, 'no': False}
    confirmation = input('\nProceed ([y]/n)? ') or 'y'
    try:
        return actions[confirmation]
    except KeyError:
        return False


def _print_command(command):
    print(f'Command: {command}')


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
        f'--servers {servers} --agents {agents} --port {port} --wait'
    )

    _print_command(command)
    if _prompt():
        c.run(command)
