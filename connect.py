from openstack import connection


conn = connection.Connection(
    region_name='RegionOne',
    auth=dict(
        auth_url='http://192.168.0.27:5000/v3',
        username='cloud',
        password='chahWeiteegh9chu',
        project_id='bf61a57b38be479b9e43321830e7acfb',
        user_domain_id='admin_domain'),
    compute_api_version='3',
    identity_interface='internal')

##Bionic, pegar um hardware especifico

conn.get_flavor()

conn.network_find_network()

conn.create_server()
