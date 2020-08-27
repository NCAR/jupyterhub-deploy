from invoke import task

images = {'base': 'jupyterhub-base'}


@task(
    help={
        'name': 'Identifier of the docker image to build. '
        f'Valid values include {list(images.keys())}'
    }
)
def build(c, name=None):
    if name is not None and name in images:
        image = images[name]
        command = f'cd {image} && docker build -t {image} .'
        print(command)
        c.run(command)
