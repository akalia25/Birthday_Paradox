# The Birthday Paradox

## About
The birthday paradox has always been an interesting probability problem that defines what is the probability in a group of n people that two individuals will share the same birthday. What I wanted to do was extend this probability problem and cover additional scenarios. The scenarios covered in this in program include:

### 1. The probability that in a group ALL individuals share the same birthday.
To formulate this, the probability function is as follows:

![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/all_same.png)

To get this formulation we take the probability that all of you share the same birthday (1/365) and raise it to the exponent of the number of people in the group.


### 2. The probability that NO ONE in the group share the same birthday.
To formulate this, the probability function is as follows:

![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/no_same_bday.png)

To get this formulation we take the probability that everyone in the group is born on a different day. The first person has 365/365 days to choose from, the second has 364/365, the third has 363/365 and so on and so forth until all n individuals have a different birthday.


### 3. The probability that any TWO people(does not neccsarily have to be you) will share a birthday in the group.
To formulate this, the probability function is as follows:

![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/one_other_bday.png)

To get this formulation, we take the compliment of probability that was calculated above, that no one shares a birthday. To get the compliment we do 1 subtract probability that everyone in the group is born on a different day.


### 4. The probability that YOU as an individual share the same birthday as someone in the group.
To formulate this, the probability function is as follows:

![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/one_other_bday.png)

To get this formulation, we take the probability that everyone in the group has a different birthday than you(364/365) raised to the exponent of n number of people in the group. Once we get this probability we take the compliment of this probability to determine the probability that someone shares the same birthday as you. To get the compliment we do 1 subtract the probability that everyone has a different birthday.


## How To Run
Effort has been made to not use any external libraries, so that this program will run independently on the native Python3 environment.
To run this program, simply download the .py file and execute it using python3.

### Sample exection is shown below:

![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/sample_output_1.png)
![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/sample_output_2.png)
![alt text](https://github.com/akalia25/Birthday_Probability/blob/master/Screenshots/sample_output_3.png)


## Closing Remarks
Hope you enjoyed this neat little tool that helps with determine different probabilities based on the group size, maybe use this at your next party and see what how many of you share the same birthday :D :P 
