# Google Cloud container deployment on Cloud Run

## Login

gcloud init

export GCP_REGION="europe-west3"
export GCP_PROJECT_ID="vindrogames-backend-develop"
export GCP_REPO_NAME="porra-django-repo"
export IMAGE_NAME="porra-django"

## Create Artifact repository

gcloud artifacts repositories create porra-django-repo --repository-format=docker \
    --location=europe-west3 --description="Porra Django 2.0"

gcloud builds submit --region=$GCP_REGION --tag $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$GCP_REPO_NAME/$IMAGE_NAME:tag1