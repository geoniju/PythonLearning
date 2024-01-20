##### To open a shell in the pod:

    kubectl exec -it test-pod -- /bin/sh

##### To make request to the cluster ip service from within cluster
Replace the IP with the ClusterIP of your service

    curl http://internal-service.default.svc.cluster.local


##### To make request to the LoadBalancer service from withing cluster
Replace <cluster-ip> with the actual ClusterIP of your service

    curl http://<cluster-ip>:80
    curl http://<service-name>:80
    curl http://<service-name.default.svc.cluster.local>:80

##### To make request to the LoadBalancer service from outside cluster
Replace <external-ip> with the actual external IP address of your LoadBalancer

    curl http://<external-ip>


##### To make request to the NodePort service from within cluster
Replace <cluster-ip> with the actual ClusterIP of your service
Replace <nodeport> with the actual NodePort assigned to your service
    
    curl http://<cluster-ip>:80
    curl http://<service-name>:80
    curl http://<service-name.default.svc.cluster.local>:80

##### To make request to the NodePort service from outside cluster

*Find external ip of one of cluster nodes*

    kubectl get nodes -o wide
Look for the external IP under the EXTERNAL-IP column.

*Find NodePort of the service*

    kubectl get services nodeport-service

Replace <external-ip> with the actual external IP of one of the cluster nodes
Replace <nodeport> with the actual NodePort assigned to your service
    
    curl http://<external-ip-of-cluster-node>:<nodeport>

##### Headless service creates individual DNS entries for each pod in a stateful set

To check dns entries

    nslookup web-0.web.default.svc.cluster.local
    
This should show you the DNS entries that Kubernetes has created for each pod in the format: 

    <pod-name>.<service-name>.<namespace>.svc.cluster.local
    
    curl http://web-0.web.default.svc.cluster.local