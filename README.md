# System Resource Monitoring Application with Docker, AWS EKS, and GitHub Actions


### I developed a containerized system resource monitoring solution leveraging Docker, Kubernetes, and AWS EKS to provide real-time data on CPU usage, RAM, and disk space. This solution uses Python for data processing and Flask to serve metrics, enabling efficient resource monitoring in scalable, cloud-native environments.



### This project leverages several key technologies:

- Docker: For containerizing the application, enabling easy deployment and consistent environments.
- AWS EKS (Elastic Kubernetes Service): Used to create a scalable and flexible Kubernetes cluster on AWS.
- Helm: Simplifies managing configurations and deploying the Kubernetes application using charts.
- GitHub Actions: CI/CD pipeline automating the processes of building, testing, and deploying the application.



### Project Workflow

- Containerization: I created a Dockerfile and built a Docker image, which was then published on Docker Hub, allowing easy deployment of the application on the Kubernetes cluster.
- Kubernetes and Helm: I set up an AWS EKS cluster and created Kubernetes configuration files, including deployment.yaml, service.yaml, and ingress.yaml. Using Helm, I deployed these files and installed an ingress controller to allow external access to the application.
- CI/CD Pipeline: I automated CI/CD processes with GitHub Actions, enabling:
- Building and publishing the Docker image on Docker Hub.
- Automatically updating the image tag in the Helm chart after each deployment.



### GitHub Actions Pipeline

The CI/CD pipeline consists of the following stages:

- build – Fetches the repository, sets up Python, installs dependencies, and performs syntax checks.
- code-quality – Runs code linting and formatting tools (flake8 and black).
- push – Builds and publishes the Docker image to Docker Hub.
- update-newtag-in-helm-chart – Automatically updates the image tag in the Helm chart to ensure the latest version is deployed to the EKS cluster.



### Final Outcome

The project culminates in a fully automated deployment of a system resource monitoring application on an EKS cluster. With Helm and GitHub Actions, the deployment is flexible, manageable, and ready for continuous updates without manual intervention.
