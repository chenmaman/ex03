
#Robots Simulation


We design and develop a complex software system includes various panels:
Robots communication simulation, algorithm revaluation location and condition, GUI display system
and a testing interface to check readiness and quality.
In this exercise we will understand the problem space by entities diagram and the implemention in Scipy in XP methodology.

* running the project in pycharm with Anconda library

###General definition of project :
* There is a group of "robots" is defined environment.
* Each robot has a unique identification number (index) and the ability at any time to listen to the environment or
Broadcast message, ie either when a transmitter robot receives information from the environment is not.
* Communication model (channel): a robot can pick up only one message at any point of time. The more
A broadcast message from a greater distance so that the probability that it will be absorbed lower
(just broadcast a message over 500 meters - the probability of its absorption is 0, which aired from a unit less than 50 meters from its absorption probability is 1).
When the signal strength of a unit at a distance r (less than 500) is the following formula 2 ^ (R-500)
Several overlapping messages) broadcast at the same time (interfere with each other in the following way: the power of
M1 broadcast message from R1 has reduced the amount of the strengths of the other messages
Other nearby (500 meters) broadcast at the same time.
* Robots have the ability to distribute traffic "will" or the ability to move randomly.
* Each robot has a battery: When the battery consumption depends linearly in any of the following: Amount
Broadcasts, duration of movement (assume a constant speed) and during the operation of the robot.
* Each robot has a solar panel: allowing it to load itself when it's sunny surroundings - so the battery is fully charged in 4 hours of sunlight.
* The basic operation of each robot is: listen, think about where I want to move forward, to transmit relevant information to the rest of the robots: robot knows only the location and direction relative Lenk, its start! (No GPS)
* As a simplifying think about Scene of "Robots as a square of size 1 * 1 km, some of it white - it has a" light "for loading, and can move in it, some of which no gray light, but allows traffic inside, and some black -mcsol You can not enter it.

##The initial state:
![Hello](https://github.com/chenmaman/ex03/blob/master/arena.png)
