from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram(name="Advanced Web Service with On-Premise (colored)", show=False):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        primary \
            - Edge(color="brown", style="dashed") \
            - Redis("replica") \
            << Edge(label="collect") \
            << metrics
        grpcsvc >> Edge(color="brown") >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        primary \
            - Edge(color="brown", style="dotted") \
            - PostgreSQL("replica") \
            << Edge(label="collect") \
            << metrics
        grpcsvc >> Edge(color="black") >> primary

    aggregator = Fluentd("logging")
    aggregator \
        >> Edge(label="parse") \
        >> Kafka("stream") \
        >> Edge(color="black", style="bold") \
        >> Spark("analytics")

    ingress \
        >> Edge(color="darkgreen") \
        << grpcsvc \
        >> Edge(color="darkorange") \
        >> aggregator



from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Internet

with Diagram("Kubernetes Cluster with Router and MetalLB Load Balancers", show=False, direction="TB"):
    with Cluster("Kubernetes Cluster"):
        with Cluster("Deployment 1"):
            metal_lb_1 = Docker("MetalLB 1")
        with Cluster("Deployment 2"):
            metal_lb_2 = Docker("MetalLB 2")
        with Cluster("Deployment 3"):
            metal_lb_3 = Docker("MetalLB 3")

    internet = Internet("Internet")
    router = Server("Router")

    internet >> router
    router >> metal_lb_1
    router >> metal_lb_2
    router >> metal_lb_3


from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
# from diagrams.onprem.loadbalancer import LoadBalancer

with Diagram("Kubernetes Cluster with Router and MetalLB LoadBalancers", show=False):

    with Cluster("Kubernetes Cluster"):
        k8s_nodes = [Server("Deployment 1"), Server("Deployment 2"), Server("Deployment 3")]

    router = "Router"  # Use a text label to represent the router
    #
    # with Cluster("On-Premises"):
    #     lb1 = LoadBalancer("MetalLB 1")
    #     lb2 = LoadBalancer("MetalLB 2")
    #     lb3 = LoadBalancer("MetalLB 3")
    #
    # k8s_nodes >> router
    # router >> lb1
    # router >> lb2
    # router >> lb3

from diagrams import Cluster, Diagram
from diagrams.generic.network import Switch
from diagrams.k8s.compute import Deployment
from diagrams.onprem.compute import Server

with Diagram("Kubernetes Cluster with MetalLB LoadBalancers", show=False):
    with Cluster("Kubernetes Cluster"):
        deployment1 = Deployment("Deployment 1")
        deployment2 = Deployment("Deployment 2")
        deployment3 = Deployment("Deployment 3")

    router = Server("Router")

    router >> deployment1
    router >> deployment2
    router >> deployment3

    router >> Switch("Internet")

#minio server wala kaam
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.network import Internet
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server

with Diagram("Cloud Network", show=False):
    with Cluster("Clients"):
        clients = [Users("Client1"), Users("Client2"), Users("Client3")]

    with Cluster("Cloud Network"):
        cloud_network = Internet("Cloud Network")

    with Cluster("Minio Servers"):
        minio_servers = [S3("Minio1"), S3("Minio2"), S3("Minio3")]
#
# internet = Internet("Internet")

    with Cluster("Storage"):
        NVMe = Server("NVMe")

    # for client in clients:
    #     client >> cloud_network

    # cloud_network >> minio_servers
    minio_servers >> NVMe
    clients >> cloud_network
    cloud_network >> minio_servers






'''from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.programming.language import Python
from diagrams.onprem.network import Internet
from diagrams.onprem.client import Users
from diagrams.generic.network import Switch

with Diagram("Kubernetes Cluster with MetalLB Load Balancers", show=False):
    with Cluster("Kubernetes Cluster"):
        with Cluster("Load Balancer 1"):
            load_balancer_1 = Docker("MetalLB")
            load_balancer_1 - [Server("Deployment 1"), Server("Deployment 2")]

        with Cluster("Load Balancer 2"):
            load_balancer_2 = Docker("MetalLB")
            load_balancer_2 - [Server("Deployment 3"), Server("Deployment 4")]

        with Cluster("Load Balancer 3"):
            load_balancer_3 = Docker("MetalLB")
            load_balancer_3 - [Server("Deployment 5"), Server("Deployment 6")]

        internet = Internet("Internet")
        users = Users("Users")

        internet >> users
        users >> load_balancer_1
        users >> load_balancer_2
        users >> load_balancer_3'''


'''#kubernetes with load balancer
from diagrams import Diagram,Cluster
from diagrams.k8s.compute import Deployment
from diagrams.k8s.network import Service
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram("Kubernetes Cluster with Load Balancers", show=False):
    # Kubernetes Cluster
    users = Users("Users")
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


from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3

with Diagram("MinIO Server", show=False):
    with Cluster("Boundary"):
        ec2 = EC2("MinIO Server")
        s3 = S3("S3 Bucket")
        ec2 >> s3'''


'''from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.database import Postgresql
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Internet

with Diagram("Monitoring Stack", show=False):
    with Cluster("PostgreSQL Cluster"):
        pg = Postgresql("PostgreSQL")
        exporter = Docker("Exporter")
        pg >> exporter
        pg_monitor = Prometheus("PGMonitor")
        exporter >> Edge(label="Metrics") >> pg_monitor

    with Cluster("Prometheus Stack"):
        prometheus = Prometheus("Prometheus")
        alertmanager = Docker("Alertmanager")
        prometheus >> alertmanager
        prometheus >> Grafana("Grafana")

    jenkins = Jenkins("Jenkins")
    internet = Internet("Internet")

    jenkins >> Edge(label="Builds") >> pg_monitor
    internet >> Edge(label="Alerts") >> alertmanager'''


'''from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.database import Postgresql
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Internet
from diagrams.generic.network import Switch
from diagrams.aws.database import RDS

with Diagram("Monitoring Stack", show=False):
     with Cluster("PostgreSQL Cluster"):
          pg=Postgresql("Postgresql")
          pg1=Postgresql("Postgresql")
          pg2=Postgresql("Postgresql")
          pg3=Postgresql("Postgresql")
          exporter = RDS("pgMonitor Exporter")
          exporter1 = RDS("pgMonitor Exporter")
          exporter2 = RDS("pgMonitor Exporter")
          exporter3 = RDS("pgMonitor Exporter")
          pg >> exporter
          pg1 >> exporter1
          pg2 >> exporter2
          pg3 >> exporter3'''


    # with Cluster("Locust"):
    #     locust = Mobile("Locust")
    #     locust >> Router("Request") >> app
    #     app >> Router("Response") >> locust'''


          # with Cluster("Prometheus"):
          #      prometheus = Prometheus("Prometheus")
          #      exporter >>prometheus
          #      exporter1 >>prometheus
          #      exporter2 >>prometheus
          #      exporter3 >>prometheus

                # for client in clients:
    #     client >> cloud_network

               # with Cluster("Grafana"):
               #      gf=Grafana("Grafana")
               #      prometheus >>gf
               #      prometheus <<gf
               #
               #      with Cluster("Alertmanager"):
               #           al=Internet("Alertmanager")
               #           prometheus >>al
               #

from diagrams import Diagram, Cluster
from diagrams.onprem.database import Postgresql
from diagrams.generic.device import Mobile
from diagrams.generic.network import Router
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.client import User

with Diagram("Application Flow", show=False):
    with Cluster("Application"):
        user = User("User")
        app = Mobile("Application")
        user >> app
        app >> Postgresql("DB") >> Grafana("Grafana")

    with Cluster("Locust"):
        locust = Mobile("Locust")
        locust >> Router("Request") >> app
        app >> Router("Response") >> locust



from diagrams import Diagram, Cluster
from diagrams.onprem.database import Postgresql
from diagrams.generic.device import Mobile
from diagrams.generic.network import Router
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.client import User
from diagrams.aws.compute import EC2

with Diagram("Application Flow", show=False):
    with Cluster("Application"):
        locust = EC2("Locust")
        app = Mobile("Application")
        locust >> Postgresql("DB") >> Grafana("Grafana")
        locust >>app

        locust >> Router("Request") >> app
        app >> Router("Response") >> locust

    # with Cluster("Locust"):
    #     locust = Mobile("Locust")
    #     locust >> Router("Request") >> app
    #     app >> Router("Response") >> locust





from diagrams import Cluster, Diagram ,Node, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node
from diagrams.aws.general import TraditionalServer
from diagrams.aws.management import OpsworksApps
from diagrams.onprem.network import Haproxy
from diagrams.k8s.network import Service
from diagrams.custom import Custom


with Diagram("Cluster nesting", show=False):
    service=LoadBalancing("Service")

# with Cluster("Kubernetes"):
    with Cluster("HAproxy"):
        haproxy1 = Haproxy("HAproxy")
        haproxy2 = Haproxy("HAproxy")

        haproxy1 -Edge(style="solid") - haproxy2

        with Cluster("Node"):
            node =Node("Worker Node1")
            node1 =Node("Worker Node2")

            with Cluster("Nodes"):
                nodes=Node("Worker Nodes3")
                nodes2=Node("Worker Nodes4")
                nodes3=Node("Worker Nodes5")


    with Cluster("Services"):
        with Cluster("Apps"):
            ops_1=OpsworksApps("Apps 1")
            ops_2=OpsworksApps("Apps 2")
            ops_3=OpsworksApps("Apps 3")

            with Cluster('Server'):
                td_s=TraditionalServer("API server 1")
                td_s1=TraditionalServer("API server 2")
                td_s2=TraditionalServer("API server 3")

        ops_1>>ops_2
        ops_2>>ops_3

        td_s>>td_s1
        td_s1>>td_s2

        haproxy2 -Edge(style="solid") - nodes
        ops_3 -Edge(style=">") -haproxy1

        td_s1 -Edge(style="solid") - node

        # node << Edge(headport ="c",tailport="c",minlen="1",lhead="cluster_node") << nodes
        # node << Edge(headport ="c",tailport="c",minlen="1",lhead="cluster_node") << nodes






        # ops_3>>haproxy1
        # haproxy2>>nodes
        # nodes2<<node
        # nodes3<<node1
        #
        # node<<td_s1
        #
        # td_s1>>service


        # node <<Edge(headport="c",taipo)


from diagrams import Cluster, Diagram, Node, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node
from diagrams.aws.general import TraditionalServer
from diagrams.aws.management import OpsworksApps
from diagrams.onprem.network import Haproxy

with Diagram("Cluster nesting", show=False):
    service = LoadBalancing("Service")

    with Cluster("Kubernetes"):
        with Cluster("HAproxy"):
            haproxy1 = Haproxy("HAproxy")
            haproxy2 = Haproxy("HAproxy")

            haproxy1 - Edge(style="solid") - haproxy2

        with Cluster("Node"):
            node = Node("Worker Node1")
            node1 = Node("Worker Node2")

        with Cluster("Nodes"):
            nodes = Node("Worker Nodes3")
            nodes2 = Node("Worker Nodes4")
            nodes3 = Node("Worker Nodes5")

        with Cluster("Services"):
            with Cluster("Apps"):
                ops_1 = OpsworksApps("Apps 1")
                ops_2 = OpsworksApps("Apps 2")
                ops_3 = OpsworksApps("Apps 3")

                # Connect HAproxy cluster to the Apps cluster
                haproxy1 >> Edge(style="dashed") >> ops_1
                haproxy1 - Edge(style="dashed") - ops_2
                haproxy1 - Edge(style="dashed") - ops_3

            with Cluster('Server'):
                td_s = TraditionalServer("API server 1")
                td_s1 = TraditionalServer("API server 1")
                td_s2 = TraditionalServer("API server 1")
        #
        # ops_1 >> ops_2
        # ops_2 >> ops_3

        haproxy2>>nodes2
        nodes2>>node
        nodes3>>node1

from diagrams import Cluster, Diagram
from diagrams.gcp.network import LoadBalancing
from diagrams.onprem.network import Haproxy
from diagrams.onprem.network import Internet
from diagrams.onprem.network import Bind9
from diagrams.aws.compute import EC2
from diagrams.onprem.container import Docker
from diagrams.aws.management import OpsworksApps

with Diagram("Complex Cluster Structure", show=False):

    internet = Internet("Internet")

    with Cluster("Worker Nodes Cluster"):
        node1 = EC2("Worker Node 1")
        node2 = EC2("Worker Node 2")
        node3 = EC2("Worker Node 3")

    with Cluster("HAProxy Cluster"):
        haproxy1 = Haproxy("HAProxy 1")
        haproxy2 = Haproxy("HAProxy 2")

    internet >> haproxy1 >> node1
    internet >> haproxy2 >> node2
    internet >> node3

    with Cluster("Apps Cluster"):
        app1 = OpsworksApps("App 1")
        app2 = OpsworksApps("App 2")
        app3 = OpsworksApps("App 3")

    with Cluster("API Servers Cluster"):
        api_server1 = Docker("API Server 1")
        api_server2 = Docker("API Server 2")

    internet >> app1 >> api_server1
    internet >> app2 >> api_server1
    internet >> app3 >> api_server2
    #
    # vpn = Bind9("VPN")
    # internet >> Bind9 >> haproxy1
    # internet >> Bind9 >> haproxy2


'''from diagrams import Cluster, Diagram, Edge, Node
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.network import Ing, Service
from diagrams.aws.management import OpsworksApps
from diagrams.aws.general import TraditionalServer
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Node as K8sNode
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Haproxy
from diagrams.custom import Custom

with Diagram("Cluster nesting", show=False):
    service = LoadBalancing("Service")

    with Cluster("Kubernetes"):

        with Cluster("HAproxy"):
            haproxy1 = Haproxy("HAproxy")
            haproxy2 = Haproxy("HAproxy")

            haproxy1 - Edge(style="solid") - haproxy2

            with Cluster("Node"):
                node1 = Node("Worker Node1")
                node2 = Node("Worker Node2")

            with Cluster("Nodes"):
                nodes1 = Node("Worker Nodes3")
                nodes2 = Node("Worker Nodes4")
                nodes3 = Node("Worker Nodes5")

            # Connect HAproxy to Nodes cluster
            # haproxy1 - Edge(style="dotted") - op
            haproxy2 - Edge(style="line") - nodes3

        with Cluster("Services"):
            with Cluster("Apps"):
                ops_1 = OpsworksApps("Apps 1")
                ops_2 = OpsworksApps("Apps 2")
                ops_3 = OpsworksApps("Apps 3")

                haproxy1 - Edge(style="line") - ops_3

            with Cluster('Server'):
                td_s = TraditionalServer("API server 1")
                td_s1 = TraditionalServer("API server 2")
                td_s2 = TraditionalServer("API server 3")

        ops_1 >> ops_2
        ops_2 >> ops_3

        td_s >> td_s1
        td_s1 >> td_s2

        node1 << Edge(headport="c", tailport="c", minlen="1", lhead="cluster_node") << nodes1
        node2 << Edge(headport="c", tailport="c", minlen="1", lhead="cluster_node") << nodes1
#
#         # Connect HAproxy to Nodes cluster
# haproxy1 - Edge(style="dotted") - nodes1
# haproxy2 - Edge(style="dotted") - nodes1'''




from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node
from diagrams.aws.general import TraditionalServer
from diagrams.aws.management import OpsworksApps
from diagrams.onprem.network import Haproxy
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import VPC
from diagrams.onprem.compute import Server

with Diagram("Cluster nesting", show=False):
    Service = LoadBalancing("service")

    with Cluster("Kubernetes"):
        with Cluster("HAproxy"):
            haproxy1 = Haproxy("HAProxy 1")
            haproxy2 = Haproxy("HAProxy 2")

            haproxy1 - Edge(style="solid", color='black') - haproxy2

        with Cluster("allnodes"):
            with Cluster("Node"):
                node = Node("Worker Node1")
                node1 = Node("Worker Node 2")
            with Cluster("Nodes"):
                nodes = Node("Worker Node3")
                nodes1 = Node("Worker Node4")
                nodes2 = Node("Worker Node5")

    with Cluster("Service", graph_attr={"style": "rounded", "bgcolor": "pink", "boundrycolor": "darkblack",
                                       "color": "darkolivegreen4", "penwidth": "2.0"}):
        with Cluster("Apps"):
            opsworks_apps1 = VPC("Apps 1")
            opsworks_apps2 = VPC("Apps 2")
            opsworks_apps3 = VPC("Apps 3")

        with Cluster("Server"):
            traditional_server1 = Server("API Server 1")
            traditional_server2 = Server("API Server 2")
            traditional_server3 = Server("API Server 3")

    with Cluster('ad'):
        ad = EC2("Aadhaar")
    with Cluster("Np"):
        np = RDS("NPCI")

    opsworks_apps1 >> opsworks_apps2
    opsworks_apps2 >> opsworks_apps3

    haproxy2 >> Edge(style="solid", color="Red") >> nodes

    opsworks_apps3 >> Edge(style="solid", color="Red") >> haproxy1

    # Update the edge so that traditional_server2 triggers Service from the bottom
    traditional_server2 << Edge(style="solid", color="black") << Service

    Service >> Edge(style="solid", color='black') >> ad
    Service >> Edge(style="solid", color="black") >> np

    traditional_server1 >> traditional_server2
    traditional_server2 >> traditional_server3

    nodes << Edge(headport="C", tailport="C", minlen="1", lhead="cluster_Nodes", style='solid', color='black') << node
    nodes << Edge(headport="C", tailport="C", minlen="1", lhead="cluster_Nodes", style="solid", color="Red") << haproxy2


'''#yeh jaruri hai
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
            prometheus >> Edge(style="solid", color="black") >> al'''



'''from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.onprem.inmemory import Redis
from diagrams.aws.compute import EC2

with Diagram("Architecture Diagram", show=False):
    with Cluster("User"):
        user = Server("User")

    with Cluster("Main Cluster"):
        haproxy = RDS("HAProxy")
        with Cluster("Small Cluster"):
            sms_gateway = Server("SMS Gateway")
            with Cluster("App Server Cluster"):
                app_server = Server("App Server")
                haproxy2 = Haproxy2("HAProxy")
                worker_node = Server("Worker Node")
            sms_gateway >> app_server

        haproxy >> sms_gateway
        haproxy2 >> worker_node

    with Cluster("Minio Cluster"):
        minio_servers = [S3("Minio Server") for _ in range(4)]

    with Cluster("Worker Node Cluster"):
        worker_nodes = [Server(f"Worker Node {i+1}") for i in range(4)]

    with Cluster("Secondary Cluster"):
        haproxy3 = Haproxy2("HAProxy")
        with Cluster("Secondary App Server Cluster"):
            app_server2 = Server("App Server")
            worker_node2 = Server("Worker Node")
        haproxy3 >> app_server2

    user >> haproxy
    worker_node2 >> EC2("Trigger") >> worker_nodes
    haproxy3 >> S3("Minio Server")'''


# from diagrams import Cluster, Diagram
# from diagrams.generic.network import Firewall
# from diagrams.onprem.client import User
# from diagrams.k8s.infra import Node
# from diagrams.onprem.compute import Server
# from diagrams.onprem.container import Docker
# from diagrams.aws.storage import S3
# from diagrams.aws.database import RDS
# from diagrams.onprem.inmemory import Redis
# from diagrams.onprem.network import Internet
# from diagrams.onprem.queue import Kafka
# from diagrams.programming.framework import Spring
#
# with Diagram("Architecture Diagram", show=False):
#     with Cluster("Internet"):
#         user = User("User")
#         internet = Internet("Internet")
#
#         user >> internet
#
#     with Cluster("Main Cluster"):
#         haproxy1 = RDS("HAProxy1")
#         haproxy2 = RDS("HAProxy2")
#
#         with Cluster("Application Cluster"):
#             app_server = Docker("Application Server")
#             haproxy1 >> app_server
#
#         with Cluster("SMS Gateway Cluster"):
#             sms_gateway = Docker("SMS Gateway")
#             haproxy1 >> sms_gateway
#
#         haproxy2 >> haproxy1
#
#     with Cluster("Worker Cluster"):
#         worker1 = Node("Worker 1")
#         worker2 = Node("Worker 2")
#         worker3 = Node("Worker 3")
#         worker4 = Node("Worker 4")
#
#         haproxy2 >> worker1
#         haproxy2 >> worker2
#         haproxy2 >> worker3
#         haproxy2 >> worker4
#
#     with Cluster("Minio Cluster"):
#         minio1 = S3("Minio 1")
#         minio2 = S3("Minio 2")
#         minio3 = S3("Minio 3")
#         minio4 = S3("Minio 4")
#
#         worker4 >> minio1
#         worker4 >> minio2
#         worker4 >> minio3
#         worker4 >> minio4
#
#     redis = Redis("Redis")
#     kafka = Kafka("Kafka")
#
#     app_server >> redis
#     app_server >> kafka
#
#     internet >> haproxy1



from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Firewall
# from diagrams.generic.server import Rack, Server
from diagrams.aws.storage import S3
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.onprem.inmemory import Redis
from diagrams.programming.framework import Django

with Diagram("System Architecture", show=False):
    with Cluster("Main Cluster"):
        haproxy1 = Haproxy2("HAProxy")
        with Cluster("Small Cluster"):
            sms_gateway = Redis("SMS Gateway")
        with Cluster("Application Cluster"):
            app_server = Django("App Server")

    worker_node = Redis("Worker Node")
    edge1 = Edge(haproxy1, worker_node, label="Triggers")

    with Cluster("Right Cluster"):
        minio_servers = [S3("Minio Server") for _ in range(4)]

    edge2 = Edge(haproxy1, minio_servers, label="Load Balancing")
    edge3 = Edge(app_server, minio_servers, label="Storage")

    with Cluster("Minio Worker Cluster"):
        minio_workers = [Redis(f"Worker {i}") for i in range(3)]

    worker_node - edge1 - minio_workers

    sms_gateway >> app_server
    app_server >> minio_servers[0]

    for i, server in enumerate(minio_servers[1:]):
        minio_servers[i] >> server

    sms_gateway >> haproxy1
    app_server >> haproxy1

    haproxy2 = Haproxy2("HAProxy")
    with Cluster("Main Cluster"):
        haproxy2 >> haproxy1

    firewall = Firewall("Firewall")
    sms_gateway >> firewall >> haproxy1
    firewall - edge1

    worker_nodes = [Redis(f"Worker {i}") for i in range(4)]
    haproxy1 - edge1 - worker_nodes



'''from diagrams import Cluster, Diagram
from diagrams.generic.network import Firewall
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Minio
from diagrams.onprem.loadbalancer import HAProxy
from diagrams.onprem.network import Internet
from diagrams.onprem.network import SMS

with Diagram("Architecture Diagram", show=False):

    with Cluster("User"):
        user = Internet("User")

    with Cluster("Main Cluster"):
        haproxy_main = HAProxy("HAProxy")
        with Cluster("SMS Gateway"):
            sms_gateway = SMS("SMS Gateway")
        with Cluster("Application Server"):
            app_server = Server("Application Server")

    user >> haproxy_main
    haproxy_main >> sms_gateway
    haproxy_main >> app_server

    with Cluster("Worker Cluster"):
        haproxy_worker = HAProxy("HAProxy")
        with Cluster("Worker Nodes"):
            worker_nodes = [Server(f"Worker {i}") for i in range(1, 5)]
        haproxy_worker >> worker_nodes

    with Cluster("Minio Cluster"):
        minio_servers = [Minio(f"Minio {i}") for i in range(1, 4)]
    app_server >> minio_servers'''

'''from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Clickhouse
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.onprem.monitoring import Nagios

with Diagram("Cluster Diagram", show=False):
    with Cluster("Big Cluster"):
        haproxy1 = Haproxy2("HAProxy 1")
        haproxy2 = Haproxy2("HAProxy 2")

        with Cluster("Worker Nodes"):
            worker1 = Server("Worker Node 1")
            worker2 = Server("Worker Node 2")
            worker3 = Server("Worker Node 3")
            worker4 = Server("Worker Node 4")

        haproxy1 >> haproxy2
        haproxy1 >> worker1
        haproxy1 >> worker2
        haproxy2 >> worker3
        haproxy2 >> worker4

        with Cluster("Minio Servers"):
            minio1 = Clickhouse("Minio Server 1")
            minio2 = Clickhouse("Minio Server 2")
            minio3 = Clickhouse("Minio Server 3")
            minio4 = Clickhouse("Minio Server 4")

        haproxy2 >> minio1
        haproxy2 >> minio2
        haproxy2 >> minio3
        haproxy2 >> minio4

    with Cluster("SMS Gateway Cluster"):
        sms_gateway = Nagios("SMS Gateway")

    with Cluster("Application Server Cluster"):
        app_server1 = Server("Application Server 1")
        app_server2 = Server("Application Server 2")
        app_server3 = Server("Application Server 3")

    sms_gateway >> app_server1
    sms_gateway >> app_server2
    sms_gateway >> app_server3'''


from diagrams import Cluster, Diagram,Edge
from diagrams.k8s.infra import Node
from diagrams.onprem.database import Oracle
from diagrams.generic.network import Router
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Haproxy as Haproxy2
from diagrams.aws.storage import S3
from diagrams.gcp.network import FirewallRules
from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.compute import Server as RHEL
from diagrams.generic.network import Switch as Nexus
from diagrams.onprem.dns import Coredns
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.client import User




with Diagram("My Diagram",direction="LR"):
    with Cluster("mm"):
        with Cluster("Bhuvneshwar"):
            with Cluster(" kk"):
                wk=Node(" Worker")

            with Cluster(" Infnispan \n cache/ \n Application"):
                wk1=Node("Worker")
                wk2=Node("Worker")
                wk3=Node("Worker")
                wk4=Node("Worker")



            with Cluster("Presented \n Volume \n Minio"):
                Wkk=S3("Worker")
                Wkk1=S3("Worker")
                Wkk2=S3("Worker")
                Wkk3=S3("Worker")



            with Cluster("OCP \n CLUSTER \n 4.8.28"):
                ma1=Node("Master")
                ma2=Node("Master")
                ma3=Node("Master")



            with Cluster("-"):
                rehl=LinuxGeneral("Bastion \n  Controller  Host \n 10.194.74.90 \n RHEL")
                cp=Redis("10.194.74.105")
                nx=Nexus("NEXUS \n 10.194.74.194")
                dns=Coredns("DNS 1 \n 10.194.74.102")
                dns1=Coredns("DNS 2 \n 10.194.74.102")

    # with Cluster(" "):
        with Cluster(" "):
            HP=Haproxy2("Haproxy \n 10.194.74.100")
            HP1=Haproxy2("Haproxy \n 10.194.74.101")

            HP >> Edge(style="solid",color='black') >> wk
            HP1 >> Edge(style="solid",color='black') >> wk

        wk >> Edge(style="solid",color='black') >> wk1
        wk1 >> Edge(style="solid",color='black') >> Wkk
        Wkk >> Edge(style="solid",color='black') >> ma1



        user=User("USER")
        wall=FirewallRules(" ")

        with Cluster(" Shahstri \n Park"):
            mtlb=Router("MTLB")

            h1=Haproxy2("Haproxy")
            h2=Haproxy2("Haproxy")
            h3=Haproxy2("Haproxy")
            h4=Haproxy2("Haproxy")
            h5=Haproxy2("Haproxy")
            h6=Haproxy2("Haproxy")
            h7=Haproxy2("Haproxy")

    with Cluster(" "):
        sms=Server("SMS Gateway")
        ap=RHEL("Application server \n 10.247.51.161")

    HPP=Haproxy2("Haproxy \n 10.194.74.100")
    HPP1=Haproxy2("Haproxy \n 10.194.74.101")
    db=Oracle("Database \n Master \n 10.194.74.109")
    db1=Oracle("Database \n Master \n 10.194.74.110")




    db >> Edge(style="solid",color='black') >> db1


    ma1 >> Edge(style="solid",color='black') >> rehl
    dns1 >> Edge(style="solid",color='black') >> db
    dns1 >> Edge(style="solid",color='black') >> HPP
    HPP >> Edge(style="solid",color='black') >> HPP1
    HPP >> Edge(style="solid",color='black') >> sms
    # HPP1 >> Edge(style="solid",color='black') >> ap



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






















'''from diagrams import Diagram, Cluster
from diagrams.generic.os import LinuxGeneral
from diagrams.aws.network import VPCTrafficMirroring
from diagrams.generic.network import Switch as Nexus


with Diagram("Cluster Diagram", show=False):
    with Cluster("Top Cluster"):
        rhel = RHEL("RHEL")

        with Cluster("Middle Cluster"):
            with Cluster("Tea Cup"):
                tea_cup = Nexus("Tea Cup")

            with Cluster("Nexus"):
                nexus = Nexus("Nexus")

                with Cluster("DNS1"):
                    dns1 = VPCTrafficMirroring("DNS1")

                    with Cluster("DNS2"):
                        dns2 = VPCTrafficMirroring("DNS2")

        rhel >> tea_cup
        tea_cup >> nexus
        nexus >> dns1
        dns1 >> dns2'''



# from diagrams import Diagram, Cluster, Edge
# from diagrams.onprem.inmemory import Redis
# from diagrams.generic.network import Switch as Nexus
# from diagrams.generic.os import LinuxGeneral
# from diagrams.onprem.dns import Coredns
#
# with Diagram("Component Hierarchy", show=False):
#     with Cluster("Bastion Controller Host \n 10.194.74.90 \n RHEL"):
#         rhel = LinuxGeneral("RHEL")
#     with Cluster("10.194.74.105"):
#         cp = Redis("Redis")
#         Edge(color="black").to(rhel, cp)
#     with Cluster("NEXUS \n 10.194.74.194"):
#         nx = Nexus("Nexus")
#         Edge(color="black").to(cp, nx)
#     with Cluster("DNS 1 \n 10.194.74.102"):
#         dns = Coredns("CoreDNS")
#         Edge(color="black").to(nx, dns)
#     with Cluster("DNS 2 \n 10.194.74.102"):
#         dns2 = Coredns("CoreDNS")
#         Edge(color="black").to(dns, dns2)


'''from diagrams import Cluster, Diagram, Edge
from diagrams.generic.network import Switch
from diagrams.onprem.monitoring import Prometheus, Grafana,Nagios
from diagrams.onprem.inmemory import Memcached
from diagrams.onprem.database import HBase
# from diagrams.programming.framework import Grafana
# from diagrams.onprem.messaging import
from diagrams.onprem.container import Docker
# from diagrams.onprem.database import Sql

with Diagram("Architecture Diagram", show=False, direction="TB"):

    with Cluster("Prometheus Ecosystem"):
        prometheus = Prometheus("Prometheus")
        alertmanager = Nagios("Alertmanager")
        opsgenie = Memcached("Opsgenie")
        prometheus >> Edge(label="Triggered") >> alertmanager
        alertmanager >> Edge(label="Triggered") >> opsgenie

    with Cluster("Monitoring and Visualization"):
        grafana = Grafana("Grafana")
        prometheus >> Edge(label="Triggered") >> grafana

    with Cluster("Local Storage"):
        storage = HBase("Local Storage")
        prometheus >> Edge(label="Triggered") >> storage

    with Cluster("Application"):
        application = Docker("Application")
        exporter = Prometheus("Exporter")
        prometheus >> Edge(label="Triggered") >> application
        application >> Edge(label="Triggers Exporter") >> exporter

    with Cluster("3rd Party"):
        third_party = Switch("3rd Party System")
        exporter >> Edge(label="Triggered") >> third_party

    # Connect the components horizontally for better readability
    alertmanager >> Edge(direction="LR") >> grafana
    storage >> Edge(direction="LR") >> application'''


#
# from diagrams import Cluster, Diagram, Edge
# from diagrams.onprem.monitoring import Prometheus, Grafana, Thanos
# from diagrams.onprem.database import Dgraph
# from diagrams.onprem.container import Docker
# from diagrams.generic.network import Switch
# from diagrams.programming.framework import Backbone
#
# with Diagram("Monitoring Architecture", show=False, direction="TB"):
#     with Cluster("Prometheus Ecosystem"):
#         service_discovery = Switch("Service Discovery")
#         prometheus = Prometheus("Prometheus")
#         alertmanager = Thanos("Alertmanager")
#         prometheus >> Edge(label="Pulls Metrics") >> service_discovery
#         service_discovery >> Edge(label="Exports Metrics") >> prometheus
#         prometheus >> Edge(label="Sends Alerts") >> alertmanager
#
#     with Cluster("Application"):
#         application = Docker("Application")
#         exporter = Backbone("Exporter")
#         application >> Edge(label="Exposes Metrics") >> exporter
#
#     with Cluster("Database"):
#         database = Dgraph("Database")
#         prometheus >> Edge(label="Stores Metrics") >> database
#
#     with Cluster("Monitoring and Visualization"):
#         grafana = Grafana("Grafana")
#         grafana >> Edge(label="Queries Metrics") >> prometheus



'''from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana, Thanos
from diagrams.onprem.database import Dgraph
from diagrams.onprem.container import Docker
from diagrams.generic.network import Switch
from diagrams.onprem.storage import Glusterfs
from diagrams.programming.framework import Backbone


with Diagram("Monitoring Architecture", show=False, direction="TB"):
    with Cluster("Prometheus Ecosystem"):
            service=Glusterfs("Service \n Discovery")
            data=Dgraph("Local Storage")
            prom=Prometheus("Prometheus \n server")
            gf=Grafana("Data \n Visualization")
            al=Switch("Alertmanager")
            ap=Thanos("Application")
            ex=Backbone("Exporter")

            prom >> Edge(style="solid",color='black') >> data
            prom >> Edge(style="solid",color='black') >> gf'''

    # with Cluster(" "):
    #     prom=Prometheus("Prometheus \n server")
    #
    # with Cluster(" "):
    #     data=Dgraph("Local Storage")
    #
    # with Cluster(" "):
    #     gf=Grafana("Data \n Visualization")
    #
    # with Cluster(" "):
    #     al=Switch("Alertmanager")
    #
    # with Cluster(" "):
    #     ap=Thanos("Application")
    #
    # with Cluster(" "):
    #     ex=Backbone("Exporter")

        # prom >> Edge(style="solid",color='black') >> data
        # prom >> Edge(style="solid",color='black') >> gf
        #
        #
        #
        # prom >> al



from diagrams import Cluster, Diagram
from diagrams.onprem.monitoring import Prometheus,Grafana
from diagrams.onprem.database import Dgraph
from diagrams.onprem.client import User
from diagrams.onprem.container import Docker
from diagrams.aws.network import DirectConnect
from diagrams.azure.general import Developertools
from diagrams.aws.business import Workmail
from diagrams.aws.database import Aurora

with Diagram("Monitoring Architecture", show=False):
    with Cluster("Monitoring Stack"):
        prometheus = Prometheus("Prometheus")
        exporter = Docker("Exporter")
        local_storage = Aurora("Local Storage")
        service_discovery = Developertools("Service Discovery")
        grafana = Grafana("Grafana")
        alertmanager = DirectConnect("AlertManager")
        email = Workmail("Email")

        prometheus << exporter
        prometheus << local_storage
        prometheus << service_discovery
        grafana >> prometheus
        prometheus >> alertmanager >> email

    with Cluster("Application"):
        application = User("Application")
        application >> exporter

    application >> service_discovery


# from diagrams import Cluster, Diagram
# from urllib.request import urlretrieve
# from diagrams.onprem.monitoring import Prometheus,Grafana
# from diagrams.onprem.database import Dgraph
# from diagrams.onprem.client import User
# from diagrams.onprem.container import Docker
# from diagrams.onprem.network import Nginx
# from diagrams.aws.network import DirectConnect
# from diagrams.azure.general import Developertools
# from diagrams.onprem.security import Vault
# from diagrams.aws.business import Workmail
# from diagrams.aws.database import Aurora
#
# with Diagram("Monitoring Architecture", show=False, direction="TB"):
#     with Cluster(" "):
#         service = "Service \n Discovery"
#
#     with Cluster(" "):
#         pro=


# from diagrams.onprem.monitoring import Prometheus,Grafana
# from diagrams import Cluster, Diagram,Edge
# from diagrams.onprem.network import Nginx
# from diagrams.elastic.elasticsearch import Alerting
# from diagrams.aws.database import Aurora
# from diagrams.aws.storage import Snowmobile
# from diagrams.aws.integration import ConsoleMobileApplication
#
#
#
# with Diagram("Monitoring Architecture", show=False, direction="TB"):
#     with Cluster(" "):
#         service=Nginx("Service \n Discovery")
#
#     with Cluster(" "):
#         pro=Prometheus("Prometheus \n server")
#         service << Edge(style="solid",color='black',lable='Find Targets') << pro
#
#     with Cluster(" "):
#         db=Aurora("Local \n Storage")
#         pro >> Edge(style="solid",color='black') >> db
#
#     with Cluster(" "):
#         with Cluster(" "):
#             exp=Snowmobile("Exporter")
#             ap=ConsoleMobileApplication("Application")
#             pro >> Edge(style="solid",color='black',) >> exp >>ap
#
#     with Cluster(" "):
#         ap=ConsoleMobileApplication("Application")




# from diagrams.onprem.monitoring import Prometheus, Grafana
# from diagrams import Cluster, Diagram, Edge
# from diagrams.onprem.network import Nginx
# from diagrams.elastic.elasticsearch import Alerting
# from diagrams.generic.network import Switch
# from diagrams.aws.database import Aurora
# from diagrams.aws.storage import Snowmobile
# from diagrams.aws.business import Workmail
# from diagrams.aws.security import Detective
# from diagrams.aws.media import ElementalMediaconnect
# from diagrams.aws.integration import ConsoleMobileApplication
#
# with Diagram("Monitoring Architecture", show=False, direction="TB"):
#
#     with Cluster(".."):
#         pro = Prometheus("Prometheus \n server")
#         service = Switch("Service \n Discovery")
#         db=Aurora("Local \n Storage")
#         service << Edge(style="solid", color='black', label='Find \n Targets') << pro
#         pro >> Edge(style="solid", color='black',label='Stores \n Data') >> db
#
#     with Cluster("..."):
#         gf = Grafana("Data \n Visualization")
#         with Cluster(""):
#             al=Alerting("Alertmanager")
#     pro << Edge(style="solid", color='black',label='PromQL') << gf
#
#
#     with Cluster("...."):
#         ma=ElementalMediaconnect(" ")
#         ma1=Detective(" ")
#         pg=Workmail(" ")
#
#     with Cluster("."):
#         exp = Snowmobile("Exporter")
#         ap1=ConsoleMobileApplication("3rd Party \n Application")
#         ap = ConsoleMobileApplication("Application")
#
#
#     exp >> Edge(style="solid", color='black') >> ap1
#     ma1 << Edge(style="solid", color='black',label='Notifications') << al
#     pg - Edge(style="solid", color='white') - service
#
#
#     pro >> Edge(style="solid", color='black',label='Push Alerts') >> al
#     exp << Edge(style="solid", color='black',label='Pull Metrics') << pro
#     exp >> Edge(style="solid", color='black') >> ap





'''from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.network import Nginx
from diagrams.elastic.elasticsearch import Alerting
from diagrams.aws.database import Aurora
from diagrams.aws.storage import Snowmobile
from diagrams.aws.enablement import ManagedServices
from diagrams.aws.business import Workmail
from diagrams.aws.security import Detective
from diagrams.aws.media import ElementalMediaconnect
from diagrams.aws.integration import ConsoleMobileApplication



with Diagram("Monitoring Architecture", show=False, direction="TB"):
    with Cluster(" "):
        ex=Snowmobile("Exporter")
        ap=ConsoleMobileApplication("Application")


    service=ManagedServices("Service")
    pro=Prometheus("Prometheus \n server")
    db=Aurora("Local \n Storage")

    with Diagram("Monitoring Architecture", show=False, direction="TB"):
        with Cluster(" "):
            al=Alerting("Alertmanager")
            gf=Grafana("Data \n Visualization")
    pro >> Edge(style="solid", color='black') >> db
    service << Edge(style="solid", color='black') << pro
    # pro >> Edge(style="solid", color='black') >> ex
    # ex >> Edge(style="solid", color='black') >> ap'''



