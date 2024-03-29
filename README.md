[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=aliartiza75_flask-backend-application)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-backend-application&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-backend-application)


# Flask Backend Application

This repository contains backend logic and kubernetes manifests. I have used `minikube` for this project. Installation steps is given in this [gist](https://gist.github.com/aliartiza75/3a34f059de62c7de04727dae6a363ea8)

# Guidelines for containerizing backend 

* To build image
```bash
sudo docker run -t ht-be:0.0.1 -f Dockerfile .
```

* To run docker container on host machine
```bash
sudo docker run -e FLASK_ENV=development -e FLASK_HOST_IP=0.0.0.0 -e=FLASK_HOST_PORT=5001 -e Name=Irtiza -p 1001:5001 ht-be:0.0.1
```

# Guidelines for kubernetes deployment

* Deployment creation
```bash
sudo kubectl apply -f deployment.yaml
```

* Service creation
```bash
sudo kubectl apply -f htbe_service.yaml 
```

* Validating whether application is running or not. Use the command given below from host machine on which kubernetes is running
```
curl -X GET "http://<ip>:<port>/datetime"
```

# Guidelines for helm charts deployment
* Helm installation guidelines [link](https://helm.sh/docs/install/#installing-the-helm-client)

* Once the helm is installed, use the command given below to install tiller in kubernetes cluster:
```bash
helm init
```

* To create a helm chart folder:

```bash
helm create <app-name>
```

* To dry run the helm chart for debugging:
```bash
sudo helm install --dry-run --debug <chart-directory> 
```

* To purge a release
```bash
sudo helm del --purge <release-name>
```

* To check the status of a release
```bash
sudo helm ls --all <release-name>
```

* To search a helm package name
```bash
sudo helm search <package-name>
```

* To create a package from the helm charts folder
```bash
sudo helm package <helm-charts-package-folder-path>
```


# Important Notes
* Start the minikube cluster in the virtual machine drive in none mode [--vm-driver=none], otherwise services will not be accessible.
* Minikube will pull images from the dockerhub.
* In some cases minikube cluster doesn't work properly, one quick fix is to delete the cluster and restart the minikube cluster.
