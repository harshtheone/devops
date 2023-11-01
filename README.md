Notes:
- docker-compose build
- docker-compose up

This is a self-contained little example data pipeline project.

1. Clone the code
2. Run the code (show a screenshot)
3. Show messages being passed between components (screenshot)
4. Show data populated in neo4j using the neo4j GUI at localhost: http://localhost:7474/browser/ (screenshot)
5. Use the elasticvue GUI (https://elasticvue.com/) to show the content of the elasticsearch index at localhost:9200 (screenshot). One message in the index should look like this: ```{
	"_index": "messages-test",
	"_type": "_doc",
	"_id": "d6oBbIoBmNUJVupvUGb-",
	"_version": 1,
	"_seq_no": 7,
	"_primary_term": 1,
	"found": true,
	"_source": {
		"content": "Message 29-2023-09-06 19:39:00.220912"
	}
}```
6. Explain in one printed page or less what this code does (text file)
7. Show a screenshot of the log messages from the running containers and explain how you would use these messages to debug the project/pipeline
8. Describe how to change the docker-compose for this project into a Kubernetes deployment, and service for each component. If it is needed, you can add a container registry for the producer and consumer, ConfigMaps, Secrets, Persistent Volumes, Helm charts, etc. The goal is for you to submit something that makes sense to you and that you can explain in the video interview. Bonus points if it actually runs, but the goal is to have you show that you understand the underlying technology. For example, you might include instructions like the following:

```
# Open ye olde Ubuntu Bash...
# install kubectl
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl

# deploy things ... 
kubectl apply -f zookeeper-deployment.yaml
kubectl apply -f zookeeper-service.yaml
kubectl apply -f kafka-deployment.yaml
kubectl apply -f kafka-service.yaml
...
# dance a little jig
```
If you prefer, you can use cloud services in your example instead of installing locally. For example, AKS with ACR, or ECR with EKS.
