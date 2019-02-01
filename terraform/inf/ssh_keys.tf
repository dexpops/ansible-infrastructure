# Create a new SSH key
resource "digitalocean_ssh_key" "kj" {
  name       = "cardno:000606334270"
  public_key = "${var.ssh_key_public}"
}
