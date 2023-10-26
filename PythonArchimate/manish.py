from diagrams import Cluster, Diagram,Edge
from diagrams.k8s.infra import Node
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.aws.storage import S3
from diagrams.gcp.network import FirewallRules
from diagrams.generic.os import RedHat
from diagrams.aws.network import ELB
from diagrams.generic.network import Switch as Nexus
from diagrams.generic.network import Subnet
from diagrams.onprem.dns import Coredns
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.client import User


with Diagram("monitoring diagram"):
    with Cluster("Users"):
        user1=User("user1")
        user2=User("user1")
        user3=User("user1")
        user4=User("user1")

    with Cluster("APp"):
        network=Subnet("Application")

    with Cluster("Loadbalancer"):
        server1=S3("Minio Server")
        server2=S3("Minio Server")
        server3=S3("Minio Server")

    user1 >> Edge(style='Solid') >>network
    user2 >> Edge(style='Solid') >>network
    user3 >> Edge(style='Solid') >>network
    user4 >> Edge(style='Solid') >>network

    network >> Edge(style='Solid') >>server1
    network >> Edge(style='Solid') >>server2
    network >> Edge(style='Solid') >>server3



from diagrams import Cluster, Diagram,Edge
from diagrams.k8s.infra import Node
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.aws.storage import S3
from diagrams.gcp.network import FirewallRules
from diagrams.onprem.auth import Boundary
from diagrams.aws.network import ELB
from diagrams.generic.network import Switch as Nexus
from diagrams.onprem.dns import Coredns
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.client import User


with Diagram("My Diagram"):
    with Cluster("mm"):
        with Cluster("Bhuvneshwar"):
            with Cluster(" "):
                HP=Haproxy2("Haproxy \n 10.194.74.100")
                HP1=Haproxy2("Haproxy \n 10.194.74.101")

            with Cluster("Openshift \n Cluster"):
                with Cluster("."):
                    wk=Node(" Worker \n 10.194.74.115")
                with Cluster(" Infnispan \n cache/ \n Application"):
                    wk1=Node("Worker \n 10.194.74.116")
                    wk2=Node("Worker \n 10.194.74.117")
                    wk3=Node("Worker \n 10.194.74.118")
                    wk4=Node("Worker \n 10.194.74.119")

                with Cluster("Presented \n Volume \n Minio"):
                    Wkk=S3("Worker \n 10.194.74.120")
                    Wkk1=S3("Worker \n 10.194.74.121")
                    Wkk2=S3("Worker \n 10.194.74.122")
                    Wkk3=S3("Worker \n 10.194.74.123")


                with Cluster("OCP \n CLUSTER \n 4.8.28"):
                    ma1=Node("Master \n 10.194.74.112")
                    ma2=Node("Master \n 10.194.74.113")
                    ma3=Node("Master \n 10.194.74.114")



            with Cluster("-"):
                rehl=Boundary("Bastion \n  Controller  Host \n 10.194.74.90 \n RHEL")
                cp=Redis("10.194.74.105")
                nx=Nexus("NEXUS \n 10.194.74.194")
                dns=Coredns("DNS 1 \n 10.194.74.102")
                dns1=Coredns("DNS 2 \n 10.194.74.102")


        # with Cluster(" "):
        #     HP=Haproxy2("Haproxy \n 10.194.74.100")
        #     HP1=Haproxy2("Haproxy \n 10.194.74.101")

            HP >> Edge(style="solid",color='black') >> wk
            HP1 >> Edge(style="solid",color='black') >> wk

        wk >> Edge(style="solid",color='black') >> wk2
        wk2 - Edge(style="dotted",color='white') - Wkk1
        Wkk1 - Edge(style="dotted",color='white') - ma2




        user=User("USER")
        wall=FirewallRules(" ")

        with Cluster(" Shahstri \n Park"):
            mtlb=ELB("LB")

            h1=Haproxy2("Haproxy")
            h2=Haproxy2("Haproxy")
            h3=Haproxy2("Haproxy")
            h4=Haproxy2("Haproxy")
            h5=Haproxy2("Haproxy")
            h6=Haproxy2("Haproxy")
            h7=Haproxy2("Haproxy")

    ma1 - Edge(style="dotted",color='white') - rehl
    user >> Edge(style="solid",color='black') >> wall
    wall >> Edge(style="solid",color='black') >> mtlb
    mtlb >> Edge(style="solid",color='black') >> h1
    mtlb >> Edge(style="solid",color='black') >> h2
    mtlb >> Edge(style="solid",color='black') >> h3
    mtlb >> Edge(style="solid",color='black') >> h4
    mtlb >> Edge(style="solid",color='black') >> h5
    mtlb >> Edge(style="solid",color='black') >> h6
    mtlb >> Edge(style="solid",color='black') >> h7
    h5 >> Edge(style="solid",color='black') >> HP





'''from diagrams import Cluster, Diagram,Edge
from diagrams.onprem.network import Haproxy as Haproxy2

with Diagram("My Diagram"):
    with Cluster("mm"):
        with Cluster("Bhuvneshwar"):
            with Cluster(" "):
                HP=Haproxy2("Haproxy \n 10.194.74.100")
                HP1=Haproxy2("Haproxy \n 10.194.74.101")'''
