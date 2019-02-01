# Create a web server
resource "digitalocean_droplet" "netbox" {

  region  = "fra1"
  image   = "coreos-stable"
  name    = "fra1-netbox-infr01"
  size    = "1gb"
  private_networking = true

  ssh_keys = [
    "${digitalocean_ssh_key.kj.fingerprint}"
  ]

}

# Create a web server
resource "digitalocean_droplet" "consul" {

  count = 2
  region  = "fra1"
  image   = "coreos-stable"
  name    = "fra1-consul-clstr01-infr0${count.index + 1}"
  size    = "1gb"
  private_networking = true

  ssh_keys = [
    "${digitalocean_ssh_key.kj.fingerprint}"
  ]

}