from invoke import Collection

from scripts import cluster, dashboard, images

namespace = Collection(images, cluster, dashboard)
