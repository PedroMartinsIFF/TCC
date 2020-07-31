import os

op = input("Deseja iniciar o cluster? Y / N \n")

if op == "Y":
    os.system('kind create cluster')
    os.system('kubectl create namespace argo')
    os.system('kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default')
    os.system(' kubectl create configmap -n argo workflow-controller-configmap --from-literal=config="containerRuntimeExecutor: pns" ')
    os.system('kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/v2.4.3/manifests/install.yaml')
else:
    exit()

# kubectl port-forward -n argo svc/argo-ui 8080:80