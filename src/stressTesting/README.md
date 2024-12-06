# 部署服务和部署svc
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 获取运行的服务
kubectl get pods

# 获取nodeport地址
kubectl get svc
