from invoke import task

from .common import _print_command, _prompt


@task(iterable=['apps'], help={'apps': 'CLI applications to install'})
def install(c, apps=None):
    'Install required CLI applications for working with Kubernetes.'
    installs = ['k3d', 'kubectl', 'helm']
    if apps:
        installs.extend(apps)
    installs = list(set(installs))
    command = f'arkade get {installs[0]} && '
    for app in installs[1:-1]:
        command += f'arkade get {app} && '
    command += f' arkade get {installs[-1]}'
    _print_command('Install CLI apps', command)
    if _prompt():
        c.run(command)
