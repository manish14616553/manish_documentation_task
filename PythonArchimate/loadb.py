'''from diagrams import Diagram
from diagrams.onprem.compute import Server
from diagrams.generic.virtualization import Virtualbox
from diagrams.onprem.network import Nginx
from diagrams.generic.network import Switch
from diagrams.generic.network import Firewall
with Diagram("KVM Load Balancing Architecture", show=False):
    # KVM Hosts
    kvm_host1 = Virtualbox("KVM Host 1")
    kvm_host2 = Virtualbox("KVM Host 2")

    # Virtual Machines
    vm1 = Server("VM 1")
    vm2 = Server("VM 2")

    # NGINX Servers
    nginx1 = Nginx("NGINX 1")
    nginx2 = Nginx("NGINX 2")

    # Load Balancer
    load_balancer = Firewall("Load Balancer")

    # Connecting Components
    kvm_host1 >> vm1 >> nginx1 >> load_balancer
    kvm_host2 >> vm2 >> nginx2 >> load_balancer
    load_balancer >> Switch("Internet")'''

'''from diagrams import Diagram, Cluster,Edge
from diagrams.onprem.container import Containerd

with Diagram("VM Interaction Diagram", show=False):
    with Cluster("VM 1"):
        vm1 = Containerd("VM 1")

    with Cluster("VM 2"):
        vm2 = Containerd("VM 2")
        vm2 >> Edge(style="solid",color='black',label='http://192.168.122.147') >> vm1
        vm1 >> Edge(style="solid",color='black',label='http://192.168.122.147') >> vm2'''


'''from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Caddy


# Diagram definition
with Diagram("Web Page Routing", show=False):
    with Cluster("192.168.122.147"):
        user = Server("User")
        nginx_manish = Caddy("Manish Web Page")
        user >> nginx_manish
    with Cluster("192.168.122.147"):
        user = Server("User")
        nginx_sudhanshu = Caddy("Sudhanshu Web Page")
        user >> nginx_sudhanshu
    user >> Python("Hit Request")'''



'''from diagrams import Diagram, Cluster,Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Containerd
from diagrams.onprem.network import Caddy
from diagrams.onprem.client import User
from diagrams.generic.os import LinuxGeneral

with Diagram("Transform iptables into a TCP load balancer"):
    with Cluster("Computer"):
        user=User("user")

        with Cluster("VM 1 \n Source"):
            with Cluster(" "):
                vm1 = LinuxGeneral("Linux1 \n Ubuntu 20.04")
            with Cluster("caddy"):
                with Cluster(""):
                    ca=Caddy("caddy")

        with Cluster("VM 2 \n Destination"):
            with Cluster(" "):
                vm2 = LinuxGeneral("Linux \n Ubuntu 20.04")
            with Cluster("caddy"):
                with Cluster(""):
                    ca1=Caddy("caddy")

        with Cluster("cd"):
            cd=Caddy("http:// \n 192.168.122.147")

    with Cluster("."):
        ip = Containerd("iptable into \n loadbalancer")

    cd >> Edge(style="solid",color='black',label='Curl hit 1') >> vm1
    cd >> Edge(style="solid",color='black',label='Curl hit 2') >> vm2
    user >> Edge(style="solid",color='black',label='http://192.168.122.147') >> cd
    ip >> Edge(style="solid",color='black') >> vm2
    ca >> Edge(style="solid",color='black') >> ip'''


from urllib.request import urlretrieve

from diagrams import Cluster, Diagram,Edge
from diagrams.generic.os import LinuxGeneral



with Diagram('myda'):
    with Cluster("man"):
        mm=LinuxGeneral("linux")

        manish='data:image/jpeg;base64,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'
        mymy='manish.png'
        urlretrieve(manish,mymy)

        a >> Edge(style="solid",color='black') >> mm








