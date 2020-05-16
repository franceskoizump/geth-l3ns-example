from l3ns.ldc import DockerNode, DockerSubnet
from l3ns.base.network import Network, NetworkConcurrent
from l3ns import defaults

defaults.network = Network('16.0.0.0/8')
dockers = []
nodes = 3 
s = DockerSubnet(name='polygon', size=10)
for i in range(nodes):
    node = DockerNode('node'+str(i+2), image='eth', command='sh -c "distr/setup_account.sh ' + str(i+2) + '"')
    dockers.append(node)
    s.add_node(node)

for node in dockers:
    print(node.get_ip())

defaults.network.start(interactive=True)
