from tenancy.models import Tenant
from ruamel.yaml import YAML
from pathlib import Path
import sys

file = Path('/opt/netbox/initializers/tenants.yml')
if not file.is_file():
  sys.exit()

with file.open('r') as stream:

  yaml=YAML(typ='safe')
  tenants = yaml.load(stream)

  optional_assocs = {}

  if tenants is not None:

    for params in tenants:

      for assoc, details in optional_assocs.items():

        if assoc in params:
          model, field = details
          query = { field: params.pop(assoc) }

          params[assoc] = model.objects.get(**query)

      tenant, created = Tenant.objects.get_or_create(**params)

      if created:
        print("Created Tenant", tenant.name)