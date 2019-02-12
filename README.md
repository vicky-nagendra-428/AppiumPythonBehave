This is the test automation framework using Appium, Python and Behave framework with page object model.
And I have used IOS test app for writing test cases.


Prerequisites
--------------------------------------------------
install python

install intelliJ or what ever IDE you like to code

install behave package

install appium, selenium and other required packages
--------------------------------------------------


To Run the tests just run the below command from the root folder of the project.
Ensure that features folder should be under root folder.

------------------------------------------------
behave
------------------------------------------------

behave command runs all the features that are inside the features folder.


You can limit the scenarios/features by specifying the tags

------------------------------------------------
behave --tags=tag_name

example : behave --tags=smoke_tests
------------------------------------------------

