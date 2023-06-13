# hotel_trip_advisor

## About The Project

The application code is equvalent to the Main branch, however rather than running locally, this application is written to be hosted on  Micorsoft Azure cloud services.  

The application images is hotested on the Microsoft Container Registry (bhflaskregistry)

The flask/workshop4-deployment.yml deploys the application image into a kubernetes cluster, allowing the application to scale as needed. Currently the .yml file is configured to run on a AZURE SQL Database, but this can be updated to any database. 

