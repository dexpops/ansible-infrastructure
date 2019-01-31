from tenancy.models import Tenant
from virtualization.models import Cluster
from virtualization.models import ClusterType
from ruamel.yaml import YAML
from pathlib import Path
import sys

file = Path('/opt/netbox/initializers/clusters.yml')
if not file.is_file():
  sys.exit()

with file.open('r') as stream:

  yaml=YAML(typ='safe')
  clusters = yaml.load(stream)

  optional_assocs = {
    'type': (ClusterType, 'slug')
  }

  if clusters is not None:

    for params in clusters:

      for assoc, details in optional_assocs.items():

        if assoc in params:
          model, field = details
          query = { field: params.pop(assoc) }

          params[assoc] = model.objects.get(**query)

      try:
        cluster, created = Cluster.objects.get_or_create(**params)
      except Exception as error:
        created = False

      if created:
        print("Created Cluster", cluster.name)