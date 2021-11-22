from __future__ import print_function
import time
from sr.robot import *

"""
Danial Sabzevari-----------Assignment(1)-------------Research Track 1---------November 15, 2021
"""
a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

R = Robot()
""" instance of the class Robot"""


def drive(speed, seconds):
    """
    Function for setting a linear velocity
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Generate the rotation and distance form the Silver Token respect to the robot
    Retuens:
    1)distance respect to the robot
    2)rotation respect to the robot
    """
    dist = 10 # initial value for distance
    rot_y = 360 #initial value for 360 degrees orientation

    for token in R.see(): # R.see() uses the vision library of the robot 
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist = token.dist  # distance from the Silver token respect to the robot can be read from token object
            rot_y = token.rot_y  # rotation of the Silver token respect to the robot can be read from token object
    return dist, rot_y 


def find_golden_token():
    """
    find golden tokens and allocate the rotations to different zones
    ...to detect the distance of golden tokens respect to the robot
    Returns:
    Rotation and distance of all right, left and front side obstacles
    """
    #Initial variables
    right_obs_dis=5
    right_obs_rot=5
    left_obs_dis=5
    left_obs_rot=5
    front_obs_dis=5
    front_obs_rot=5

    
    for token in R.see():
        
        if token.info.marker_type is MARKER_TOKEN_GOLD:
            if 45<token.rot_y<135 and token.dist < right_obs_dis: #define the right side obstacles
                right_obs_dis=(token.dist)
                right_obs_rot=(token.rot_y)
            elif -135<token.rot_y<-45 and token.dist < left_obs_dis: #define the left side obstacles
                left_obs_dis=(token.dist)
                left_obs_rot=(token.rot_y)
            elif -45<token.rot_y<45 and token.dist < front_obs_dis: #define the front side obstacles
                front_obs_dis=(token.dist)
                front_obs_rot=(token.rot_y)
    return right_obs_dis, right_obs_rot, left_obs_dis, left_obs_rot, front_obs_dis, front_obs_rot



def Token_check(dist, rot_y,front_obs_dis,left_obs_dis,right_obs_dis):
    """
    Detect and check whether the golden token is between the robot and silver token. 
    """    
    if dist < 1: 
        if -179.9 < rot_y < -89.9 or 89.9 < rot_y < 179.9: # do not consider the rear side tokens
            Check = False
        elif -89.9 < rot_y < 89.9: # If true, the front side is only activated
            Check = True
    else:
        Check = False
    
    #drive the robot if  golden tokens found in front side 
    #decision between left and right wals
    if Check == False: 
        if abs(front_obs_dis) < 0.9:
            if abs(right_obs_dis) < abs(left_obs_dis):
                turn(-10,0.5)
            elif abs(left_obs_dis) < abs(right_obs_dis):
                turn(10,0.5)
        else:
            drive(30,0.25)






# main loop

while 1:
    right_obs_dis, right_obs_rot, left_obs_dis, left_obs_rot, front_obs_dis, front_obs_rot= find_golden_token()      
    dist, rot_y=find_silver_token()
    Token_check(dist, rot_y,front_obs_dis,left_obs_dis,right_obs_dis)

    if -a_th<= rot_y<=a_th and dist <d_th: # Condition for grabing the silver token if close enough
        print("Found it!") 
        R.grab() # Uses the grab function fron Robot object
        print("Succeed!")
        turn(30, 2)  # turn +180 deg
        R.release() #uses the Release funtion of Robot object
        drive(-20,2) # drive backward to make enough space from the token
        turn(-30, 2) #turn -180 degs to get back to the right angle 
        
        
    elif -a_th<= rot_y<=a_th and dist >d_th: # Go straight if the front angle is between the threshold 
      	print("Keep going...")
        drive(60,0.5)
    elif rot_y < -a_th : # turn left if far from the token
        turn(-5, 0.1)
    elif rot_y > a_th: # turn right if far from token
      	turn(+5, 0.1)
    
