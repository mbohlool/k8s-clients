import client_set

c=client_set.ClientSet(config_file='/Users/mehdy/.kube/config')
print c
v1=c.get_client('v1')
print v1
print v1.list_pod_for_all_namespaces(pretty=True, watch=False)