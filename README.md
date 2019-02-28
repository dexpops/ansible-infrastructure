# Ansible infrastructure
Ansible infrastructure

Thoughts about infrastucture:

* Ansible is fine for setting up infrastcutre that is not in a part of an ongoing development - e.g netbox or consul
* Coreos ignition templates for immutable infrastructure services like bitcoin, ipam provisioners etc. that are part of ongoing development
* When coreos ignition files are used, than ansible is used for test only with --check --diff to see everything is as espected. This also sets an test driven development

##  Service discovery:

* Use consul as service discovery for dynamic inventory. TTL will also remove stale infrastructure

##Do we really need provisioning in the cloud?
Instead of using the empty AMIs you could bake your own AMI and skip the whole provisioning part completely but I see a giant flaw in this setup. Every change, even a small one, requires recreation of the whole instance. If it’s a change somewhere on the base level then you’ll need to recreate your whole fleet. It quickly becomes unusable in case of deployment, security patching, adding/removing a user, changing config and other simple things.

Even more so if you bake your own AMIs then you should again provision it somehow and that’s where things like Ansible appears again. My recommendation here is again to use Packer with Ansible.

So in the most cases, I’m strongly for the provisioning because it’s unavoidable anyway.

# How to use Ansible with Terraform
Now, returning to the actual provisioning I found 3 ways to use Ansible with Terraform after reading the heated discussion at this GitHub issue. Read on to find the one that’s most suitable for you.

# Ansivle terraform invengtory
command ansible-playbook -i hosts/inventory_inf playbooks/infrastructure.yml

https://github.com/adammck/terraform-inventory/blob/master/bin/dist

create own version `./dist 0.8.0`

# Logical datacenters
http://www.historyplace.com/worldhistory/topten/index.html

Yorktown
Hastings
Stalingrad
Leipzig
Antietam
Cajamarca
Waterloo
Vienna

TODO:

* Add env vars to vpncloud for in cointainer replacement
* mape vpncloud a smaller image
* To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled'
* Make sure nomad server is not exposede to public internet
* Setup openvpn

# TIPS
systemctl list-units --no-pager

sys-devices-virtual-net-docker0.device
sys-devices-virtual-net-wantun0.device

BindsTo=sys-devices-virtual-net-wantun0.device
After=sys-devices-virtual-net-wantun0.device`

docker run --net=demo --rm -it robertxie/ubuntu-nettools

docker run --rm --net=host --name=dnsmasq -p 53:53/tcp -p 53:53/udp -v /etc/dnsmasq/dnsmasq.conf:/etc/dnsmasq/dnsmasq.conf:ro --cap-add=NET_ADMIN andyshinn/dnsmasq:2.75 \
--log-facility=- --conf-file=/etc/dnsmasq/dnsmasq.conf --log-queries -d