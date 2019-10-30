from openstack import connection
import openstack


#Initialize  cloud
conn = openstack.connect(cloud = 'openstack')

for server in conn.compute.server():
    print(server.to_dict())


#Upload an image to the cloud

image = conn.create_image(
    'ubuntu-trusty', filename = 'ubuntu-trusty.qcow2', wait = True)
)

#Find flavor with at least 512M of region_name

flavor = conn.get_flavor_by_ram(512)


#Boot a server, wait for it to boot.

conn.create_server(
    'server', image=image, flavor=flavor, wait= True, auto_ip = True)
)









#conn = connection.Connection(
#    region_name='RegionOne',
#    auth=dict(
#        auth_url='http://192.168.0.27:5000/v3',
#        username='admin',
#        password='chahWeiteegh9chu',
#        project_id='bf61a57b38be479b9e43321830e7acfb',
#        user_domain_id='admin_domain'),
#    compute_api_version='3',
#    identity_interface='internal')



##Bionic, pegar um hardware especifico

#conn.get_flavor()

#conn.network_find_network()

#conn.create_server()
