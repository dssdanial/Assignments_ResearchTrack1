## Second Assignment- Research Track 2- The University of Genova 
![alt text](https://github.com/dssdanial/Assignments_ResearchTrack1/blob/main/sr/robot.png) 
## Statistical Analysis
This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and exercises have been modified for the Research Track I course.

Here's a brief summary of the report:

The [report](https://github.com/dssdanial/Assignments_ResearchTrack1/blob/Statistics-Analysis/Statistical%20Analysis%20-%20Report%20-%20RT2.pdf) presents a statistical analysis to compare two codes' performance: one developed by him and the other provided by a professor for the same assignment. The task is to evaluate the codes' performance in a specific circuit scenario where silver tokens are positioned either in standard positions or randomly.

Data were collected for both scenarios, and the [analysis](https://github.com/dssdanial/Assignments_ResearchTrack1/blob/Statistics-Analysis/Statistical%20Analysis%20-%20Report%20-%20RT2.pdf.m) was based on two performance factors: 
1. The mean lap time in terms of silver tokens. 
2. The robot's turn decision method depends on the frontal distance from gold tokens, considering silver tokens are placed randomly and standardly in the circuit.

The report describes how the scripts were modified to store data regarding forward distance from gold tokens and lap times. The codes were executed ten times with the robot completing five laps each time. Data was gathered from each run, and then the mean distance from the gold tokens and the average lap time were calculated for each scenario.

To verify if there is a significant difference between the data sets, a T-Test was performed, prefaced by a Lilliefors test to confirm the normal distribution of data samples. Two hypotheses were tested for distances and lap times respectively. For each factor, the null hypothesis assumed no difference between the professor's solution and the student's, while the alternative hypothesis assumed the professor's solution surpasses the student's solution.

In conclusion, the report found that regardless of whether silver tokens were placed systematically or randomly, the professor's solution generally performed better than the student's solution. The professor's solution maintained a greater distance from obstacles and required less time to complete a lap.


