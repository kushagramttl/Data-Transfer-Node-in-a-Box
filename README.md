# Data-Transfer-Node-in-a-Box

# 1. Vision and Goals Of The Project:

We are reaching a point in science where our ability to generate and collect experimental data is outstripping our ability to move, store and reliably retrieve it. To realize the maximum impact of trillions of dollars of global research the results from those experiments need to be accessible to as wide a community as possible. Whereas research results in the past were neatly summarized in research papers totaling kilobytes, modern research generates artifacts that are an order of a billion times larger (petabyte scale). While storage and networking hardware have advanced apace with this torrent of data, their orchestration - the ability to share and move large datasets globally - lags painfully.

The project aims to make large data transfers less painful for the end users of ScienceDMZ and focuses on the following:
   * Users must have a way of packaging their data(ScienceDMZ and DTNs) into a container collection.
   * Users must have access to a portal where they can register their packaged containers and coordinate their data transfers.
   * Transfers must work in a reasonably fast and reliable manner, with some kind of network checking/monitoring before and during the moving of data.

# 2. Users/Personas Of The Project:

This project targets researchers and scientists who are dealing with giant data sets and have a great need for sharing and moving large datasets globally. 
There are mainly two users who will be using the application:
1. Sender
2. Receiver
* Sender: 
 * Users will have access to a portal where they can initiate large data transfers. Once they successfully register and log in to this website,  they will be able to download Dockerfile and docker-compose.yaml file from the docker hub.
 * When the user runs these files, it will build two containers - minion and controller container.
 * The controller container will poll commands from the portal. These commands are given by the sender on the portal.
 * The sender can initiate the transfer using the minio client command through the portal. The controller container will start the transfer. The commands for transfer :
   1. First, sender will create an alias for receiver’s container using the mc command: mc config host add --api s3v4 bobmachine http://bobmachine.bobco.com :9000 accesskey  secret
   2. Then the sender will transfer using the following command: mc config host add --api s3v4 bobmachine http://bobmachine.bobco.com :9000 accesskey  secret
 * (Note : the receiver needs to send it’s minio accesskey and secret key to the sender via email/message).
   * The controller container will also send the status updates to the portal continuously. 

* Receiver: 
  * On the receiver side, the receiver too has to login on the portal and download the files from the docker-hub. (same step that sender did).
  * The receiver will put the minio access key and secret key on the portal.
  * The minio container for the receiver will receive the files (sender has already initiated using his keys).
  * The minio container will save these files to the local file system of the receiver.
 

# 3. Scope and Features Of The Project:

The solution would be presented as a Proof of Concept where the team plans to create a technology backlog to learn the technologies required for the project. Such as learning how to create containers and using services such as MinIO.
  * Presents a simple compelling interface for end-users.
    * Addition and management of users of the system.
    * Ability to create containers of data.
    * Option to initiate, stop and restart container transfer.
    * Option to evaluate network parameters.
  * Integration of perfSonar for network performance
  * Evaluation of Docker and OpenShift for creating data containers.
    * Create container using the evaluated platform
          
The team will be evaluating if it is possible to include performance tuning on OS and network level in the scope of the project based upon experimentation results and the fact that it is dependent upon server availability and server configuration.

# 4. Solution Concept

This project aims to use a Science DMZ to package data into a collection of containers that can be deployed by end users to get improved performance out of their storage and networking and; as a starting point for system administrators to achieve performance only currently attainable by the most skilled.
The Science DMZ is a portion of the network, built at or near the campus or laboratory's local network perimeter that is designed such that the equipment, configuration, and security policies are optimized for high-performance scientific applications rather than for general-purpose business systems or “enterprise” computing.

![Solution Concept](images/DataTransferNodeInABox.png)

The solution will consist of a Data Transfer Portal which will allow users to login and start containerization of data. The data inside containers would then be transferred over high speed networks from source to destination where the minio container of the receiver saves the data in the local file system.
Before the transfer is initiated, the solution proposes to perform Data Path Characterization by evaluating network parameters.

The solution proposes to follow the mentioned steps for transfer of data:

* User can download the container using docker
* Add image to the container which will contain the data to be transfered
* Container transfers data from source to destination using transfer protocol like HTTP and S3
* Receiver would receive the data in local file system(like laptop or virtual machine)
* Sender can stop the transfer of data if required

The solution would be using services such as MinIO which allows a consistent, performant and scalable object store. It can handle unstructured, large data such as photos, videos, log files, container images, backups etc. The solution also uses S3 and HTTP protocols for swift transfer of containers over the network reliably.


# 5. Acceptance Criteria
The project acceptance will be based on the following criteria:
* Creation of an image container where data can be stored
* Transfer of container from a source to destination
* A portal where the user can login to perform the above operations

Initially, the portal only needs to cover basic necessity that supports the mentioned operations

# 6. Release Planning
Due for Week1:
* Django setup
* Learning about protocol for transfer of files
* Learning about image and container creation

For March 12, 2021:
* Create container that can store data
* Learn about communication between 2 containers
* Django setup for user access to portal
* Learn about network transfer using HTTP and S3

The further releases of applications are not fixed yet for a particular date and are dependent on evaluation results from experiments being conducted for the project.


The further releases of application are not fixed yet for a particular date and are dependent on evaluation results from experiments being conducted for the project.

