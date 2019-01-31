# ansible
Ansible infrastructure

Thougts about infrastucture:

Ansible is fine for setting up infrastcutre that is not in a part of an ongoing development - e.g netbox or consul
Coreos ignition templates for immutable infrastructure services like bitcoin, ipam provisioners etc. that are part of ongoing development
When coreos ignition files are used, than ansible is used for test only with --check --diff to see everything is as espected. This also sets an test driven development

Using consul as service discovery for dynamic inventory.

