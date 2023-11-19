# [Day-2] Load Data to BigQuery via Airbyte

## Run Airbyte via Docker

- Execute the command below to run airbyte server via [docker-compose](https://github.com/Immersive-DataEngineer-Resource/ingestion-data/tree/main/ingestion_airbyte) or download the airbyte docker-compose from the [documentation](https://docs.airbyte.com/quickstart/deploy-airbyte). 

- This `sh` file will setup airbyte installation, download its dependencies and make sure the airbyte is running.

```
./run-ab-platform.sh
```

- Once all the installation is complete, open the browser, go to airbyte dashboard in http://localhost:8000 and login with this credential.
```
username: airbyte
password: password
```

- We are going to load Corona data from this [url](https://storage.googleapis.com/covid19-open-data/v2/latest/epidemiology.csv) to BigQuery dataset via airbyte. 

## Create Service Account on GCP 

![](./_images/airbyte__sa_details_1.png)


![](./_images/airbyte__sa_details_2.png)


![](./_images/airbyte__sa_details_3.png)

![](./_images/airbyte__sa_create_keys.png)


![](./_images/airbyte__sa_add_keys.png)

![](./_images/airbyte__sa_json_key.png)


## Create Source in Airbyte

![create-source](./_images/airbyte__create_source.png)


## Create Destination in Airbyte

- To create connection, supply the Project ID, Dataset Location and Dataset ID from GCP to the Destination dashboard.

- Also, we should copy service-account.json key and paste it to the required textbox.

![create-destination](./_images/airbyte__create_destination.png)


## Sync Data from Airbyte Source to Destination

![](./_images/airbyte__sync.png)
