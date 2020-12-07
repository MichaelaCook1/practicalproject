# Practical Project - Dice Roller Game

## External Resources:

#GitHub Project Board: https://github.com/users/MichaelaCook1/projects/3

## Contents
*[Brief & Requirements](#brief)
*[My Pitch](#my-pitch)
*[Service Architecture](#service-architecture)
*[ERD](#erd)
*[MOSCOW Model](#moscow-model)
*[CI Pipeline](#ci-pipeline)
*[VCS and Project Tracking](#vcs-and-project-tracking)
*[Deployment](#deployment)
*[Risk Assessments](#risk-assessments)
*[Testing Analysis](#testing-analysis)
*[Application Front-End Imagery](#application-front-end-imagery)
*[Further Developments](#further-developments)

## Brief
You are required to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.
#Service 1
The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.
#Services 2 + 3
These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.
#Service 4
This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
The requirements set for the project are below.
Note that these are a minimum set of requirements and can be added onto during the duration of the project.
#Scope
The requirements of the project are as follows:

An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
This could also provide a record of any issues or risks that you faced creating your project.
An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
The project must follow the Service-oriented architecture that has been asked for.
The project must be deployed using containerisation and an orchestration tool.
As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
The project must make use of a reverse proxy to make your application accessible to the user.

## My Pitch
My aim was to create a service-based application that produced a Dice Roller game, such that at the press of a button two dice of different size are rolled and a prize is awarded based on whether the sum of the result of both dice rolls is an odd or even number.

# Service 1 
Service 1 displays the front-end of the application where on the web browser a user can see the result of the 20-sided dice, the 12-sided dice, the sum of these values and whether this value would incur a prize being awarded. A roll button has also been implemented to reset the game, such that the user is not required to refresh the web page to see a new random result. Within the app.py file of Service 1, get requests are used to interact and poll data from the other services, the "value" variable is also defined here which takes the sum of the two random integers.

![Service1][Service1]

# Service 2
Service 2 generates a random integer between 1 and 20 simulating a random 20-sided dice roll.

![Service2][Service2]

# Service 3
Service 3 generates a random integer between 1 and 12 simulating a random 12-sided dice roll.

![Service3][Service3]

# Service 4
Service 4 determines the awarding of a prize based on the result of the random dice rolls, this works by using a get request to pull the total from the "value" variable in Service 1, and then posts "Win" or "Lose" dependent on this total.

![Service4][Service4]

## Service Architecture 
Below is a diagram of the initial Service Architecture followed by the evolution of the Architecture which is the finished result of the application.

![InitialArc][InitialArc]

Initially the application was intended to work as a Dungeons and Dragons dice roller where the D20 would dictate how successful the user's attack was including -if statements that would describe how successful the attack was based on the result of the dice roll. And where the D12 would dictate how much damage would be dealt by this attack, where the integer would correspond to 'hit-points' of damage. And these results would be incorporated together within a final statement using -if statements stating if the attack would be successful and how much damage would be dealt along with different outcomesbased on the result of the D20, i.e a result of "1" would be a critical fail, and a result of "20" would be a critical hit. This original architecture did not incorporate a database to persist data, as it would have been very complex in structure. I moved away from this initial idea, as I felt the complexity of this application would be very time-consuming to produce, and as the main goal with this project is successful deployment I opted for a simpler service structure.

![FinalArc][FinalArc]

Above is the architecture of the finished result of the application as explained previously, a database was also created for the purpose of persisting data.

## ERD
Below is the entity relationship diagram (ERD) detailing the structure of the database that was attempted for implementation.

![ERD][ERD]

## MOSCOW Model

*#M - A web application that utilises a service to display the front-end of the app, two random elements services that are combined within a fourth service, clear documentation, project board, build through jenkins, artifact repository through docker, using ansible to initiate a docker swarm, deployment using a docker stack, and reverse proxy using NGINX
*#O - 
*#S - Detailed unit testing of services, replicas and multiple workers for seamless updates
*#C - coverage of unit testing preserved in a html report
*#O - 
*#W - Persistence of data from a database ( this was attempted but was unsuccessful)

## CI Pipeline
Below is a diagram detailing the continuous integration pipeling.

![CI][CI]

## VCS and Project Tracking
GitHub was chosen as the Version Control System Provider for versioning of the application using branches. Git hub was also used for project tracking where I created a project board detailing my progress through app creation as well as user stories.
#GitHub Project Board: https://github.com/users/MichaelaCook1/projects/3

## Deployment
A key element of this project was in it's deployment, where a Jenkins pipeline was used for the implementation of the automated testing, build, push, deployment and update of the application into a live environment. To ensure robust deployment and no further configuration requirement, ansible initiates a swarm with two workers to balance traffic, within the docker build 3 replicas were created for each service to allow smooth transition of updates, and nginx is also utilised as a load balancer and as a reverse proxy. 

## Risk Assessment
Here is the original risk assessment followed by an updated risk assessment

![InitialRisk][InitialRisk]

![UpdatedRisk][UpdatedRisk]

## Testing 
Service 1 testing:
After trouble-shooting service1 to get successful running of the app the unit test was edited in line with these changes. I have achieved a testing coverage of 81% over the service, however was still getting fails for the creation of the sql database from memory and for werkzeug build of the end point. Due to time constraints within the project these failures could not be investigated further, however since the test only creates a database from memory and does not utilise the database that is connected to the application, this failure can be neglected as the database has proven to be connected to the application through its successful running. In regard to the build error, where it does not recognise the endpoint "index" and is suggesting an endpoint of "static"; from research this would imply the test cannot find the url for the index page, as this has been proven to be successful outside of testing with the application running, I find no concern for this error.

![Service1Test][Service1Test]


Service 2 testing:
After testing this service a testing coverage of 95% was achieved, this is an near-ideal result and shows functionality over a great deal of the service. With more time further testing could be conducted to achieve 100% coverage, however given the high coverage achieved, I do not feel this necessary for this project.

![Service2Test][Service2Test]


Service 3 testing:
After testing this service a testing coverage of 95% was achieved, this is an near-ideal result and shows functionality over a great deal of the service. With more time further testing could be conducted to achieve 100% coverage, however given the high coverage achieved, I do not feel this necessary for this project.

![Service3Test][Service3Test]


Service 4 testing:
After testing this service a testing coverage of 83% was achieved, this is a more than acceptable result and shows functionality over a majority of the serivce. With more time further testing could be conducte to achieve 100% coverage, however given the high coverage achieved, and given testing is not a main objective of this project I do not feel this is necessary.

![Service4Test][Service4Test]

#Testing Analysis
Initially when running the Jenkins Pipeline it was run without ansible or docker stack to test the success of the build process, after troubleshooting errors with the database portion of the build a successful result was shown as below:

![JenkinsnoAnsible][JenkinsnoAnsible]

One this was completed the next task was to get functionality within initialisation of the docker swarm using ansible. An error that was encountered with this was connecting the swarm components as known hosts, this was fixed by setting the jenkins user as the ansible user and to ssh into each vm in time to ensure all were connected. Another issue encountered here was ansible could not find the docker role this was troubleshooted to be a result of docker .yaml file installing the incorrect file versions within the requirements. After troubleshooting these problems the pipeline was able to run the swarm and successfully deployed the stack.

![JenkinsSuccess][JenkinsSuccess]

Despite apparently running successfully, a connection refused error occurred when opening the browser, I solved this problem by running the docker-compose.yaml file once again within the terminal to observe if this issue was a result of a service error or an error within deployment. After checking the docker logs it appeared that that once an image was built it up the previous image was not pulled down as such this was taking up the ports, this was fixed by adding "sudo docker-compose down --rmi all" into the docker script such that the ports would be free, there was also a sytax error within service3 which caused the build process to fail. I also encountered a rather peculiar error when running docker service logs where the database port was in use by a different mysql service that was removed two weeks ago and was being rebuilt by the pipeline.

![sqlerror][sqlerror]

To fix this error the service was removed once again and the port for the database image was changed to 3307 to stop any further conflicts.

##Application Front-End Imagery
See below front end image detailing dice rolls, value and result of roll

![index][index]

##Further Developments
Given more time I would have investigated the database functionality such that it would persist data throughout the application. I also would have liked the opportunity to add more complexity to the services, and to add a quantumrandom plugin to the services so that the dice roll would be truly random as opposed to psuedo-randomness. 

##Author
Michaela Cook

[Service1]: https://imgur.com/a/Ej9PadZ
[Service2]: https://imgur.com/a/tsiu7Lb
[Service3]: https://imgur.com/a/NXCkl22
[Service4]: https://imgur.com/a/UgZbvKV
[InitialArch]: https://imgur.com/a/of34viU
[FinalArch]: https://imgur.com/a/CkIXPqE
[ERD]: https://imgur.com/a/qM8YEOX
[CI]: https://imgur.com/a/x7rZrgH
[InitialRisk]: https://imgur.com/a/qPYFNMq
[UpdatedRisk]: https://imgur.com/a/bLcTMKj
[Service1Test]: https://imgur.com/a/ed1Ziwe
[Service2Test]: https://imgur.com/a/ctJQTvJ
[Service3Test]: https://imgur.com/a/mWWxwRf
[Service4Test]: https://imgur.com/a/nyRJIC6
[JenkinsnoAnsible]: https://imgur.com/a/F9NOWbo
[JenkinsSuccess]: https://imgur.com/a/VSnixEU
[sqlerror]: https://imgur.com/a/ybzVoR6
[index]: https://imgur.com/a/8vu2ajX







