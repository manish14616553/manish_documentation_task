# 1.minio server walakaam
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.network import Internet
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server

with Diagram("Cloud Network", show=False):
    with Cluster("Clients"):
        clients = [Users("Client1"), Users("Client2"), Users("Client3")]
        cloud_network = Internet("Cloud Network")
        minio_servers = [S3("Minio1"), S3("Minio2"), S3("Minio3")]
        NVMe = Server("NVMe")

    # with Cluster("Cloud Network"):
    #     cloud_network = Internet("Cloud Network")
    #
    # with Cluster("Minio Servers"):
    #     minio_servers = [S3("Minio1"), S3("Minio2"), S3("Minio3")]
#
# internet = Internet("Internet")
#
#     with Cluster("Storage"):
#         NVMe = Server("NVMe")

    # for client in clients:
    #     client >> cloud_network

    # cloud_network >> minio_servers
    minio_servers >> NVMe
    clients >> cloud_network
    cloud_network >> minio_servers


#kubernetes with load balancer
from diagrams import Diagram,Cluster
from diagrams.k8s.compute import Deployment
from diagrams.k8s.network import Service
# from diagrams.onprem.client import Users
from diagrams.aws.compute import EC2
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram("Kubernetes Cluster with Load Balancers", show=False):
    # Kubernetes Cluster
    users = EC2("Router")
    # # ingress = Service("Ingress")
    # db = PostgreSQL("Database")

    with Cluster("Kubernetes Cluster"):
        lb1 = Service("LoadBalancer 1")
        lb2 = Service("LoadBalancer 2")
        lb3 = Service("LoadBalancer 3")
        deployment1 = Deployment("Deployment 1")
        deployment2 = Deployment("Deployment 2")
        deployment3 = Deployment("Deployment 3")

        lb1 >> deployment1
        lb2 >> deployment2
        lb3 >> deployment3
        # users >> ingress
        # deployment1 - db
        # deployment2 - db
        # deployment3 - db
        users >> lb1
        users >> lb2
        users >> lb3
        
# from diagrams.onprem.ci import Jenkins
# from diagrams.onprem.container import Docker
# from diagrams.generic.network import Switch


#monitoring
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.database import Postgresql
from diagrams.onprem.network import Internet
from diagrams.aws.database import RDS
with Diagram("Monitoring Stack", show=False, direction="TB", outformat="png"):
     with Cluster(" "):
          with Cluster("PostgreSQL "):
               pg=Postgresql("Postgresql")
               pg1=Postgresql("Postgresql")
               pg2=Postgresql("Postgresql")
               pg3=Postgresql("Postgresql")
               exporter = RDS("pgMonitor Exporter")
               exporter1 = RDS("pgMonitor Exporter")
               exporter2 = RDS("pgMonitor Exporter")
               exporter3 = RDS("pgMonitor Exporter")

               pg >> Edge(style="solid",color="black") >> exporter
               pg1 >> Edge(style="solid",color="black") >> exporter1
               pg2 >> Edge(style="solid",color="black") >> exporter2
               pg3 >> Edge(style="solid",color="black") >> exporter3


          prometheus = Prometheus("Prometheus")
          exporter >> Edge(style="solid",color="black") >> prometheus
          exporter1 >> Edge(style="solid",color="black") >> prometheus
          exporter2 >> Edge(style="solid",color="black") >> prometheus
          exporter3 >> Edge(style="solid",color="black") >> prometheus

     with Cluster(" "):
          with Cluster(" "):
               gf=Grafana("Grafana")
               prometheus >> Edge(style="solid",color="black") >> gf
               prometheus << Edge(style="solid",color="black") << gf
               al=Internet("Alertmanager")
               prometheus >> Edge(style="solid",color="black") >> al



          # with Cluster("Prometheus"):
          #      prometheus = Prometheus("Prometheus")
          #      exporter >>prometheus
          #      exporter1 >>prometheus
          #      exporter2 >>prometheus
          #      exporter3 >>prometheus
          #      gf=Grafana("Grafana")
          #      prometheus >>gf
          #      prometheus <<gf
          #      al=Internet("Alertmanager")
          #      prometheus >>al

               # # with Cluster("Grafana"):
               #      gf=Grafana("Grafana")
               #      prometheus >>gf
               #      prometheus <<gf
               #      al=Internet("Alertmanager")
               #      prometheus >>al
                    
                    # with Cluster("Alertmanager"):
                    #      al=Internet("Alertmanager")
                    #      prometheus >>al


from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node
from diagrams.onprem.network import Haproxy
from diagrams.aws.network import VPC
from diagrams.onprem.compute import Server



with Diagram("Cluster nesting", show=False):
    Service=LoadBalancing("service")


    with Cluster("Kubernetes"):
        with Cluster("HAproxy"):
            haproxy1=Haproxy("HAProxy 1")
            haproxy2=Haproxy("HAProxy 2")

            haproxy1 - Edge(style="solid",color='black') - haproxy2

        with Cluster("allnodes"):
            with Cluster("Node"):
                node = Node("Worker Node1")
                node1 = Node("Worker Node 2")
            # with Cluster("3nodes"):
            with Cluster("Nodes"):
                nodes=Node("Worker Node3")
                nodes1=Node("Worker Node4")
                nodes2=Node("Worker Node5")

    with Cluster("Service", graph_attr={"style": "rounded", "bgcolor": "pink", "boundrycolor":"darkblack", "color": "darkolivegreen4", "penwidth": "2.0"}):
        with Cluster("Apps"):
            opsworks_apps1=VPC("Apps 1")
            opsworks_apps2=VPC("Apps 2")
            opsworks_apps3=VPC("Apps 3")

        with Cluster("Server"):
            traditional_server1=Server("API Server 1")
            traditional_server2=Server("API Server 2")
            traditional_server3=Server("API Server 3")


    opsworks_apps1 >> opsworks_apps2
    opsworks_apps2 >> opsworks_apps3

    haproxy2 >> Edge(style="solid",color="black") >> nodes

    opsworks_apps3 >> Edge(style="solid",color="black") >> haproxy1
    # node >> Edge(style="solid",color="black",errno="up") >> traditional_server2

    traditional_server2 >> Edge(style="solid",color="black") >> Service




    traditional_server1 >> traditional_server2
    traditional_server2 >> traditional_server3

    node << Edge(headport="C",tailport="C",minlen="1",lhead="cluster_Node",style='solid',color='black') << nodes
    node << Edge(headport="C",tailport="C",minlen="1",lhead="cluster_Node",style="solid",color="black") << nodes

from diagrams import Cluster, Diagram,Edge
from diagrams.k8s.infra import Node
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.aws.storage import S3
from diagrams.gcp.network import FirewallRules
from diagrams.generic.os import RedHat
from diagrams.aws.network import ELB
from diagrams.generic.network import Switch as Nexus
from diagrams.onprem.dns import Coredns
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.client import User


with Diagram("My Diagram"):
    with Cluster("mm"):
        with Cluster("Bhuvneshwar"):
            with Cluster(" ."):
                wk=Node(" Worker \n 10.194.74.115")

            with Cluster(" "):
                HP=Haproxy2("Haproxy \n 10.194.74.100")
                HP1=Haproxy2("Haproxy \n 10.194.74.101")

            with Cluster("."):
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
                rehl=RedHat("Bastion \n  Controller  Host \n 10.194.74.90 \n RHEL")
                cp=Redis("10.194.74.105")
                nx=Nexus("NEXUS \n 10.194.74.194")
                dns=Coredns("DNS 1 \n 10.194.74.102")
                dns1=Coredns("DNS 2 \n 10.194.74.102")


        # with Cluster(" "):
        #     HP=Haproxy2("Haproxy \n 10.194.74.100")
        #     HP1=Haproxy2("Haproxy \n 10.194.74.101")

            HP >> Edge(style="solid",color='black') >> wk
            HP1 >> Edge(style="solid",color='black') >> wk

        wk >> Edge(style="solid",color='black') >> wk1
        wk1 - Edge(style="dotted",color='white') - Wkk
        Wkk - Edge(style="dotted",color='white') - ma1



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
    h7 >> Edge(style="solid",color='black') >> HP




from diagrams import Diagram
from diagrams.generic.network import Switch
from diagrams.onprem.client import User
from diagrams.generic.network import Switch
from diagrams.generic.network import Router
from diagrams.custom import Custom

with Diagram("SMS Gateway and Application Server", show=False):
    internet = Switch("Internet")
    user = User("User")
    switch = Switch("Switch")
    router = Router("Router")
    sms_gateway = Custom("SMS Gateway", "./sms_gateway.png")
    app_server = Custom("Application Server", "./app_server.png")

    user >> switch >> router >> internet
    internet >> router >> switch >> app_server
    internet - sms_gateway




from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.database import Postgresql
from diagrams.onprem.network import Internet
from diagrams.aws.database import RDS

with Diagram("Monitoring Stack", direction="TB", outformat="png"):
    with Cluster("Database Cluster"):
        with Cluster("PostgreSQL "):
            pg = Postgresql("Postgresql")
            pg1 = Postgresql("Postgresql")
            pg2 = Postgresql("Postgresql")
            pg3 = Postgresql("Postgresql")
            exporter = RDS("pgMonitor Exporter")
            exporter1 = RDS("pgMonitor Exporter")
            exporter2 = RDS("pgMonitor Exporter")
            exporter3 = RDS("pgMonitor Exporter")

            pg >> Edge(style="solid", color="black") >> exporter
            pg1 >> Edge(style="solid", color="black") >> exporter1
            pg2 >> Edge(style="solid", color="black") >> exporter2
            pg3 >> Edge(style="solid", color="black") >> exporter3

    with Cluster("Monitoring Cluster"):
        prometheus = Prometheus("Prometheus")
        exporter >> Edge(style="solid", color="black") >> prometheus
        exporter1 >> Edge(style="solid", color="black") >> prometheus
        exporter2 >> Edge(style="solid", color="black") >> prometheus
        exporter3 >> Edge(style="solid", color="black") >> prometheus


        with Cluster("Grafana & Alertmanager"):
            gf = Grafana("Grafana")
            prometheus >> Edge(style="solid", color="black") >> gf
            prometheus << Edge(style="solid", color="black") << gf
            al = Internet("Alertmanager")
            prometheus >> Edge(style="solid", color="black") >> al






    # with Cluster(" "):
    #     sms=Server("SMS Gateway")
    #     ap=RHEL("Application server \n 10.247.51.161")
    #
    # HPP=Haproxy2("Haproxy \n 10.194.74.100")
    # HPP1=Haproxy2("Haproxy \n 10.194.74.101")
    # db=Oracle("Database \n Master \n 10.194.74.109")
    # db1=Oracle("Database \n Master \n 10.194.74.110")




from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams import Cluster, Diagram, Edge
from diagrams.elastic.elasticsearch import Alerting
from diagrams.generic.network import Switch
from diagrams.aws.database import Aurora
from diagrams.aws.storage import Snowmobile
from diagrams.aws.business import Workmail
from diagrams.aws.security import Detective
from diagrams.aws.media import ElementalMediaconnect
from diagrams.aws.integration import ConsoleMobileApplication


with Diagram("Monitoring Stack", direction="LR", outformat="png"):
    with Cluster(' '):
        with Cluster(''):
            se=Switch('Service \n Discovery')
            pro=Prometheus("Prometheus \n Server")
            db=Aurora('Local \n Storage')

            se << Edge(style="solid", color="black") << pro
            pro >> Edge(style="solid", color="black") >> db

    gf=Grafana("Data \n Visualization")
    al=Alerting('Alertmanager')
    ap=ConsoleMobileApplication('Application \n Client Library')
    ex=Snowmobile('Exporter')
    ap3rd=ConsoleMobileApplication('3rd Party Application')
    ex >> Edge(style="solid", color="black") >> ap
    ex >> Edge(style="solid", color="black") >> ap3rd
    pro >> Edge(style="solid", color="black") >> ex
    pro >> Edge(style="solid", color="black") >> al







    pro >> Edge(style="solid", color="black") >> gf
    # pro >> Edge(style="solid", color="black") >> al
    with Cluster('.'):
        ma=Workmail(" ")
        op=Detective(" ")
        pg=ElementalMediaconnect(" ")
        al >> Edge(style="solid", color="black") >> op
        op >> Edge(style="dotted", color="white") >> ma
        pg >> Edge(style="dotted", color="white") >> op


        ma >> Edge(style="dotted", color="white") >> se


from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams import Cluster, Diagram, Edge
from diagrams.elastic.elasticsearch import Alerting
from diagrams.generic.network import Switch
from diagrams.aws.database import Aurora
from diagrams.aws.storage import Snowmobile
from diagrams.aws.business import Workmail
from diagrams.aws.security import Detective
from diagrams.aws.media import ElementalMediaconnect
from diagrams.aws.integration import ConsoleMobileApplication

with Diagram("Monitoring Stack", direction="TB", outformat="png"):
    with Cluster(' '):
        with Cluster(''):
            se = Switch('Service \n Discovery')
            pro = Prometheus("Prometheus \n Server")
            db = Aurora('Local \n Storage')

            se << Edge(style="solid", color="black") << pro
            pro >> Edge(style="solid", color="black") >> db

    ap = ConsoleMobileApplication('Application \n Client Library')
    ex = Snowmobile('Exporter')
    ap3rd = ConsoleMobileApplication('3rd Party Application')

    # Shift ConsoleMobileApplication and Snowmobile to the right side of Prometheus
    pro >> Edge(style="solid", color="black") >> ap
    pro >> Edge(style="solid", color="black") >> ex
    ex >> Edge(style="solid", color="black") >> ap3rd

from diagrams import Diagram, Cluster
from diagrams.onprem.monitoring import Prometheus,Grafana,Thanos, Splunk
from diagrams.aws.storage import Snowmobile
from diagrams.onprem.compute import Server
from diagrams.generic.network import Switch
from diagrams.aws.compute import EC2
from diagrams.aws.business import Workmail
from diagrams.programming.framework import Flask

with Diagram("Monitoring Architecture", show=False, direction="TB"):
    with Cluster("Prometheus Server"):
        local_storage = Snowmobile("Local Storage")
        service_discovery = Server("Service Discovery")
        prometheus = Prometheus("Prometheus")
        prometheus - local_storage
        prometheus - service_discovery

    with Cluster("Application Server"):
        app_server = Flask("Application")
        exporter = Thanos("Exporter")
        app_server - exporter

    with Cluster("Alerting"):
        alertmanager = Splunk("Alertmanager")
        email = Workmail("Email")
        alertmanager - email

    with Cluster("Visualization"):
        grafana = Grafana("Grafana")

    local_storage >> prometheus
    service_discovery >> prometheus
    exporter >> prometheus
    alertmanager >> prometheus
    email >> alertmanager
    prometheus >> grafana

