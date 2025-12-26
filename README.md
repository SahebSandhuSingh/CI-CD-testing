# ML CI/CD Pipeline with GitHub Actions & Docker

## Overview
This project demonstrates a **complete CI/CD pipeline for a machine learning project** using **GitHub Actions** and **Docker**.  
Every code change is automatically **tested**, **containerized**, and **delivered** as a Docker image.

The project is built to understand **core MLOps concepts** such as automation, reproducibility, and continuous delivery.

---

## Objectives
- Automate testing of ML code using CI
- Ensure reproducible environments using Docker
- Deliver deployable ML artifacts automatically
- Learn industry-standard MLOps workflows

---


---

## ⚙️ Tech Stack
- Python 3.10  
- scikit-learn  
- pytest  
- GitHub Actions  
- Docker  
- Docker Hub  

---

## 🔁 CI/CD Workflow

### Continuous Integration (CI)
Triggered on every push or pull request:
1. Code is checked out
2. Dependencies are installed
3. Automated tests are run using `pytest`
4. Pipeline fails if any test fails

### Continuous Delivery (CD)
After CI passes:
1. Docker image is built
2. Image is tagged using the Git commit SHA
3. Image is pushed to a **private Docker Hub repository**

---

## Dockerization
The project is containerized to:
- Ensure consistent runtime environments
- Avoid dependency-related issues
- Produce deployment-ready artifacts

---

## Security
- Docker Hub credentials are stored using **GitHub Secrets**
- No sensitive information is hardcoded
- Supports private Docker repositories

---

## Building Docker Image on Local Mahcine
docker build -t ml-ci-cd .
docker run ml-ci-cd
