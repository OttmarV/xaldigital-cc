# xaldigital-cc
Coding Challenge

Goals Accomplished:
  - Design the E-R from the database and create the structure based on the files attached.
  - Ingest the data from the centos server to the postgres database.
  - At least the ‘read’ request must be supported for the API (Query only includes reading 20 rows)
  - The server where the API is going to be deployed must have access only to the postgres
database. And the centos server must have access only to the postgres database as well.
  - Validate the column state has a length of 2 and only contains letters (Using unit tests)
  - Your code could run on Docker as well.

Instructions:
  1. Install Docker Desktop and Docker Compose
  2. Download this repository
  3. Once everything is downloaded, open a terminal, then change to xaldigital-cc/ directory. 
```console
foo@bar:~$ cd xaldigital-cc
```
  4. Then again, change directory into src/ directory 
```console
foo@bar:~$ cd src
```
  5. Once in xaldigital-cc/src/, run docker compose command to launch the multi-container app. This will download the required images, and will launch the containers with the services and networks configured in xaldigital-cc/src/docker-compose.yml file. This step might take a while the first time it is executed.
```console
foo@bar:~$ docker-compose up
```
  At this step, python file xaldigital-cc/src/datalake/code/main.py will run, this script reads the csv file found in xaldigital-cc/src/datalake/code/raw, performs a few tests and loads it into the postgres database container. Looking something like this:
  
![image](https://user-images.githubusercontent.com/17484897/175212602-cdef1241-5a67-49c9-bc10-e092fde5ef50.png)

  6. Once the load is completed, centos container will go offline. Postgres and api containers will still be running. To make sure data was loaded successfully, we will run a query through our API, reading 50 rows from the table users within the database.
  
  [http://localhost:8080/docs#/default](http://localhost:8080/docs#/default "Title")
  
  
  ![image](https://user-images.githubusercontent.com/17484897/175216855-4619aeda-1a60-42ac-b096-009adf00939c.png)

  ![image](https://user-images.githubusercontent.com/17484897/175217116-e642785e-b08c-4f09-809b-481c9048e227.png)

  ![image](https://user-images.githubusercontent.com/17484897/175217328-beb4b7e0-98c7-4f0b-9270-55e17652e593.png)

  In response body we can see the data pulled from postgres container.

  ![image](https://user-images.githubusercontent.com/17484897/175217518-74a22ae3-b9df-45c9-b7a5-9abaf07cf92d.png)


  
