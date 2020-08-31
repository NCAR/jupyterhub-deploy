from invoke import Collection

from scripts import cluster, dashboard, hub, images

namespace = Collection(images, cluster, dashboard, hub)
