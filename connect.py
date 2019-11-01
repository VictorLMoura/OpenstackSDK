import openstack
import time

#Initialize  cloud
conn = openstack.connect(cloud = 'openstack')




#Find flavor with at least 1024M of region_name
def list_flavors(conn):
        print("List Flavors:")

        for flavor in conn.compute.flavors():
                print(flavor)

flavor = conn.get_flavor_by_ram(1024)

#Boot a server, wait for it to boot.

#Find network
def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(network)

conn.create_server(
    'server', image=image, flavor=bionic,wait= True, auto_ip = True,network = network)

conn.delete_server(
    'server')

print("Deletou Instancia")
