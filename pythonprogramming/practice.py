from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Haproxy
from diagrams.programming.language import Python

with Diagram("Cluster Diagram", show=False):
    with Cluster("Cluster 1"):
        with Cluster("Apps Cluster"):
            app1 = Docker("App 1")
            app2 = Docker("App 2")
            app3 = Docker("App 3")

        with Cluster("API Servers Cluster"):
            api1 = Server("API Server 1")
            api2 = Server("API Server 2")
            api3 = Server("API Server 3")

    with Cluster("Cluster 2"):
        haproxy1 = Haproxy("HAProxy 1")
        haproxy2 = Haproxy("HAProxy 2")

        with Cluster("Worker Nodes Cluster"):
            worker1 = Server("Worker Node 1")
            worker2 = Server("Worker Node 2")
            worker3 = Server("Worker Node 3")

        with Cluster("Cluster 3"):
            with Cluster("Worker Nodes Cluster"):
                worker4 = Server("Worker Node 4")
                worker5 = Server("Worker Node 5")

        haproxy1 >> worker1
        haproxy1 >> worker2
        haproxy1 >> worker3

        haproxy2 >> worker4
        haproxy2 >> worker5

    app1 >> haproxy1
    app2 >> haproxy1
    app3 >> haproxy1

    api1 >> worker4
    api2 >> worker4
    api3 >> worker5






from diagrams import Diagram, Cluster, Shape

# Create a diagram
with Diagram("RHEL Logo and Network Diagram", show=False):
    # Create a cluster for RHEL logo
    with Cluster("RHEL", direction="TB"):
        Shape("RHEL Logo", "cup", label="RHEL", width=60, height=60, style="filled", fillcolor="red")

    # Create a cluster for Nexus
    with Cluster("Nexus", label="Nexus", direction="TB"):
        Shape("Nexus Logo", "server", label="Nexus", width=60, height=60, style="filled", fillcolor="blue")

    # Create a cluster for DNS1
    with Cluster("DNS1", label="DNS1", direction="TB"):
        Shape("DNS1 Logo", "cloud", label="DNS1", width=60, height=60, style="filled", fillcolor="gray")

    # Create a cluster for DNS2
    with Cluster("DNS2", label="DNS2", direction="TB"):
        Shape("DNS2 Logo", "cloud", label="DNS2", width=60, height=60, style="filled", fillcolor="gray")


        

