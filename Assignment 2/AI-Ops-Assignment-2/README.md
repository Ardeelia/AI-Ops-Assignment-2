# AI-Ops-Assignment-2

The following are the instructions to run the questions, Each question has its own python notebook of the form Q.ipynb. All these files will need to be pulled to run the commands. Also the writeup and written answers to all the questions are located in the pdf file. The evidence and the demo of the code running can be found in the video link which is in the video link folder of this repository. The AI Readme file is also present in this repository within the same folder.
Q1. These are the commands for Q1
docker build -t video_test_single_stage .
docker build -f Multi_Stage_Dockerfile -t video_test_multi_stage .
Docker images - will show the two docker images and their size difference can be observed

Q2. The following below are the commands for Q2
docker compose up -d --build
curl -X POST "http://localhost:8000/v1/models/email-classifier:predict" \
     -H "Content-Type: application/json" \
     -d '{
       "instances": [
         "Congratulations! You won a $1000 gift card, click here to claim now",
         "Hey, are we still meeting for lunch at 12:30 PM today?"
       ]
     }'
Running this curl command twice will show a drop in latency proving that the prediction has been stored in Redis and is thus faster on the second try

Q3.
minikube start --nodes 2 --cpus 2 --memory 4096 --driver=docker
minikube image build -t video_test_email_verifier -f Q3_Dockerfile .
minikube image load docker.io/library/video_test_email_verifier:latest
kubectl apply -f job-multi-node.yaml
kubectl get pods -o wide -w
This command will show the process being completed and the collect results cell in the Q3 notebook can be run to see the table showing the number of invalid rows

Q4.
docker build -f Dockerfile-Q4 -t email-classifier:v1 .
minikube image load email-classifier:v1 
kubectl apply -f k8s-manifest.yaml
kubectl get pods -l app=email-classifier

kubectl delete pod <pod-name>

kubectl get pods -l app=email-classifier

Update code of Q4 notebook to include version in the form 
@app.get("/healthz") def healthz(): return {"status": "ok", "version": "v2", "pod": POD_NAME, "node": NODE_NAME}


docker build -f Dockerfile-Q4 -t email-classifier:v2 .
minikube image load email-classifier:v2
kubectl set image deployment/email-classifier-deployment predictor=email-classifier:v2 --record
kubectl rollout status deployment/email-classifier-deployment

kubectl rollout history deployment/email-classifier-deployment

The following commands and instructions will show the changed rollout history

