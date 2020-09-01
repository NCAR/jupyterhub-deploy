from invoke import Collection

from scripts import cluster, dashboard, dep, hub, images

namespace = Collection(images, cluster, dashboard, hub, dep)
