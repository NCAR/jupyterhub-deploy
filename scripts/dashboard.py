from invoke import task

from .common import _print_command, _prompt


@task
def install(c):
    """Install kubernetes-dashboard"""
    command = (
        'arkade install kubernetes-dashboard --wait '
        '&& kubectl apply -f k8s/dashboard'
    )
    _print_command('Install kubernetes dashboard', command)
    if _prompt():
        c.run(command)


@task
def token(c):
    """Get token for loggin in."""
    command = (
        'kubectl -n kubernetes-dashboard describe secret '
        "$(kubectl -n kubernetes-dashboard get secret | grep admin-user-token | awk '{print $1}')"
    )
    _print_command('Get token to use for loggin in', command)
    if _prompt():
        c.run(command)


@task
def proxy(c):
    """Forward the dashboard to the local machine"""
    command = 'kubectl proxy'
    _print_command('Forward kubernetes-dashboard to local machine', command)

    if _prompt():
        c.run(command)
