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
- look at https://www.youtube.com/watch?v=c4nTKMU6fBU  minute 10 when making the drawio inforgraph
- `master node`
  - Kubernetes API Server
    - `cubectl` ==> CLI tool that we use to talk to the master node.
    - Talks to the worker nodes
  - `Scheduler`
    - decides where things need to go
    - decides which worker-node gets assigned a pod
  - `Controller Manager`
  - `etcd`
    - key-value store database
    - stores the state of the system


- `pod`
    - Smallest logical unit that you can deploy int o a kubernetes cluster.
    - consists of:
        - one or more containers (one most of the time).
        - shared volumes
        - shared IP address

- `worker node`
     - each node has its own public addressable ip address
     - each worker node has a `kubelet` that talks to the API server



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
- `flux`

#### YouTube videos
- John Saville: https://www.youtube.com/c/NTFAQGuy
- Microservices: https://www.youtube.com/watch?v=CZ3wIuvmHeM
- Cloud networking: https://www.youtube.com/watch?v=sCR3SAVdyCc&list=PLOspHqNVtKAA_5N3pI49wkH4WsTkeZ_iQ
- cloud fundamentals: https://www.youtube.com/watch?v=20QUNgFIrK0&list=PLOspHqNVtKAC-_ZAGresP-i0okHe5FjcJ
- Setting up kubernetes in Azure: https://www.youtube.com/watch?v=eyvLwK5C2dw
- Service monitors: https://www.youtube.com/watch?v=_NtRkBipepg
- Terraform with azure kubernetes: https://www.youtube.com/watch?v=bHjS4xqwc9A
- crash course in kubernetes on azure: https://www.youtube.com/watch?v=Ess4VaQzdWw
- a crash course in azure kubernetes services: https://www.youtube.com/watch?v=Ess4VaQzdWw
- service mesh: what and why: https://www.youtube.com/watch?v=rVNPnHeGYBE
- AKS cluster: https://www.youtube.com/watch?v=NnwQZyi0BAs
- Understand Azure kubernetes service architecture: https://www.youtube.com/watch?v=Au7Xocb99dA&list=PLaYx14SsCrOtobvdbeExcV4ZVRWsLc51I
- https://www.youtube.com/watch?v=0qotVMX-J5s&list=PLOspHqNVtKABAVX4azqPIu6UfsPzSu2YN
- https://www.youtube.com/watch?v=2vMEQ5zs1ko
- https://www.youtube.com/playlist?list=PLOspHqNVtKABAVX4azqPIu6UfsPzSu2YN