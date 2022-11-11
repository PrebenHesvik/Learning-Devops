### Kubernetes (K8S)
#### A Container Orchestration System used for:
- `Automatic deployment` of the containerized applications across different servers.
- `Distribution of the load` across multiple servers
- `Auto-scaling` of the deployed applications
- `Networking` between the services (for example between frontend, backend, db)
- `Monitoring`, `health check`, and `insight` of the containers
    - we can use tools like `prometheus`, `istio`, `kiali`
- `Replacement` of the failed containers.


<br>


#### Key concepts
- `pod`
    - Smallest logical unit that you can deploy int o a kubernetes cluster.
    - consists of:
        - one or mroe containers (one most of the time).
        - shared volumes
        - shared IP address

- `worker node`
     - each node has its own public addressable ip address
     - `kublet`

- `cubectl` ==> CLI tool

- `service registry`

- `service`
    - a grouping of several pods
    - A `service.yaml` file will define each service.
    - `cluster ip` ==> a type of service. It enables access to that service from within the kubernetes network.
    - A service allows for `load balance requests`.
    - `node port` ==> assigns the same public accessable IP address to each node used in a service, and we can connect to the service from the outside through the node port. The node port needs to maintain a registry of the nodes in the service.
    - `load balancer` ==> a cloud provider will spin up a NLB (work load balancer) for every service you expose, and the NLB will route directly to the service associated.
    - `external ip`
    - `ingress`
    - `istio` ==> provides traffic management, policy enforcement and telemetry collection.
    - `operator framework`
    - `knative` ==>
        - build
        - serve => snapshots, intellignet routing, scaling
        - event ==> triggers, pipelines

- `kube dns`

- `helm` ==> a package manager for kubernetes
    - `tiller` ==> server side component of helm

#### YouTube videos
- John Saville: https://www.youtube.com/c/NTFAQGuy
- Microservices: https://www.youtube.com/watch?v=CZ3wIuvmHeM
- Cloud networking: https://www.youtube.com/watch?v=sCR3SAVdyCc&list=PLOspHqNVtKAA_5N3pI49wkH4WsTkeZ_iQ
- cloud fundamentals: https://www.youtube.com/watch?v=20QUNgFIrK0&list=PLOspHqNVtKAC-_ZAGresP-i0okHe5FjcJ
- https://www.youtube.com/watch?v=0qotVMX-J5s&list=PLOspHqNVtKABAVX4azqPIu6UfsPzSu2YN
- https://www.youtube.com/watch?v=2vMEQ5zs1ko
- https://www.youtube.com/playlist?list=PLOspHqNVtKABAVX4azqPIu6UfsPzSu2YN