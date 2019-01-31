from tenancy.models import Tenant
from virtualization.models import ClusterType
from ruamel.yaml import YAML
from pathlib import Path
import sys

file = Path('/opt/netbox/initializers/cluster_types.yml')
if not file.is_file():
  sys.exit()

with file.open('r') as stream:

  yaml=YAML(typ='safe')
  cluster_types = yaml.load(stream)

  optional_assocs = {}

  if cluster_types is not None:

    for params in cluster_types:

      for assoc, details in optional_assocs.items():

        if assoc in params:
          model, field = details
          query = { field: params.pop(assoc) }

          params[assoc] = model.objects.get(**query)

      try:
          cluster_type, created = ClusterType.objects.get_or_create(**params)
      except Exception as error:
        created = False

      if created:
        print("Created ClusterType", cluster_type.name)