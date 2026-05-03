'''Consider an intelligent traffic signal. The signal has two states: red and green. The vehicle density in front of the signal is denoted by the variable u. If the vehicle density crosses
a threshold T in either direction, the state of the signal changes. The dynamics of this change is represented in the image given below:
For example, if the signal is currently red, and the vehicle density becomes greater than or equal to the threshold, it is time to turn the signal green. This is denoted by the arrow
from red to green at the bottom of the image. Assume that the signal senses the vehicle density every 30 seconds and updates its state appropriately.


-------------IMAGE---------

Write a class named signal with the following specification:
Attributes

(1) state: string, either "red" or "green; represents the current state of the signal
(2) v: int, represents the vehicle density at the current instant
(3) T: int, threshold for the vehicle density

Methods

self is the first argument of all methods. We will only mention additional arguments, if any.
(1)_init _: constructor; accepts the threshold T as argument; initially the signal is red and the vehicle density is 0.
(2) sense: accept the vehicle density as argument and update the corresponding attribute; assume that this information comes from a sensor.
(3) update: update the state of the signal-attribute depending on the current values of the attributes.

(1) Each test case corresponds to one or more method calls. We will use S to denote the name of the object.
(2) You do not have to accept input from the user or print output to the console. You just have to define the class based on the specification given in the question.




'''