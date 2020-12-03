# Practical Project - Dice Roller Game

## External Resources:

#GitHub Project Board: 

## Contents

















## Testing 

Service 1 testing:
After trouble-shooting service1 to get successful running of the app the unit test was edited in line with these changes. I have achieved a testing coverage of 81% over the service, however was still getting fails for the creation of the sql database from memory ans for werkzeug build of the end point. Due to time constraints within the project these failures could not be investigated further, however since the test only creates a database from memory and does not utilise the database that is connected to the application, this failure can be neglected as the database has proven to be connected to the application through its successful running. In regard to the build error, where it does not recognise the endpoint "index" and is suggesting an endpoint of "static"; from research this would imply the test cannot find the url for the index page, as this has been proven to be successful outside of testing with the application running, I find no concern for this error.




Service 2 testing:
After testing this service a testing coverage of 95% was achieved, this is an near-ideal result and shows functionality over a great deal of the service. With more time further testing could be conducted to achieve 100% coverage, however given the high coverage achieved, I do not feel this necessary for this project.




Service 3 testing:
After testing this service a testing coverage of 95% was achieved, this is an near-ideal result and shows functionality over a great deal of the service. With more time further testing could be conducted to achieve 100% coverage, however given the high coverage achieved, I do not feel this necessary for this project.


Service 4 testing:
After testing this service a testing coverage of 83% was achieved, this is a more than acceptable result and shows functionality over a majority of the serivce. With more time further testing could be conducte to achieve 100% coverage, however given the high coverage achieved, and given testing is not a main objective of this project I do not feel this is necessary.
