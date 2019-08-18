## 1. Start StreamNet & CLI service 

```bash
conflux_dag_two_nodes.sh
start_cli_two_nodes.sh
```
## 2. Configure nginx https

You need to buy a domain and https certificate first.
place server.key and server.pem in /etc/nginx.

Then place the nginx.conf in /etc/nginx and restart nginx.

## 3. k8s deployment

```bash
kubectl apply -f streamnet-dep.yml # deploy cluster
kubectl port-forward pod/streamnet-5c44964cfd-d69wh 8888:5000 # expose port of a single pod

kubectl describe pods streamnet-5c44964cfd-s67fp
curl http://localhost:8888/add_neighbors -X POST -H "Content-Type: application/json" -d @neighbor.json # connect pods

kubectl apply -f streamnet-svc.yml # expose streamnet-cli services
```
