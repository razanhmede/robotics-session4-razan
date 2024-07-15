#Assignment 4 OOP PYTHON
##Overview

This project focuses on simulating various types of robots with specific functionalities like cleaning and cooking. Each robot type inherits from a base Robot class, enabling shared and specialized behaviors.

##Features

###Robot Class: Base class defining common attributes and methods.
###CleaningRobot Class: Inherits from Robot, with additional methods for cleaning tasks.
###CookingRobot Class: Inherits from Robot, focusing on culinary tasks.
###MaintenanceRobot Class: Inherits from CleaningRobot and Cooking Robot for multitasking.
###Testing : Utilizes unittest for comprehensive testing of robot functionalities.

##Usage:
 1- Clone the repository URL
 2- Build and run the docker container 
 3- Create instances of CleaningRobot, CookingRobot, or MaintenanceRobot with specified attributes in the main file
 4- Run Tests using: python -m unittest discover -s tests