from invoke import task

images = {'hub': 'images/hub'}


@task(
    help={
        'name': 'Identifier of the docker image to build. '
        f'Valid values include {list(images.keys())}'
    }
)
def build(c, name=None):
    """Build docker images."""
    if name is not None and name in images:
        image = images[name]
        command = f'cd {image} && docker build -t {name} .'
        print(command)
        c.run(command)
