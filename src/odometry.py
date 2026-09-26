#this is first shot of odometry script

import math

def pose_change(x,y,theta,ds_l,ds_r,track_width):
    #shifting of center
    ds = (ds_l+ds_r)/2

    #change of orientation
    d_theta = (ds_r-ds_l)/track_width

    #middle value of theta

    theta_mid = theta + d_theta/2

    #calculation of position coordinates
    x1 = x +ds*math.cos(theta_mid)
    y1 = y +ds*math.sin(theta_mid)
    theta1 = theta + d_theta

    return x1,y1,theta1

position = [

]
pose = pose_change(0,0,0,0.05,0.052,0.5)

for i in range(100):
    pose = pose_change(pose[0],pose[1],pose[2],0.05,0.052,0.5)
    print(pose)
    position.append(pose)

print(position)













#x1,y1,theta1 = pose_change(0,0,0,0.1,0.12,0.5)
#print(x1,y1,theta1)
#x1,y1,theta1 = pose_change(0,0,0,0.12,0.1,0.5)
#print(x1,y1,theta1)
#x1,y1,theta1 = pose_change(0,0,0,-0.1,0.1,0.5)
#print(x1,y1,theta1)
#x1,y1,theta1 = pose_change(0,0,0,0.1,0.12,0.5)
#print(x1,y1,theta1)
#x1,y1,theta1 = pose_change(0,0,2.1,0.1,0.1,0.5)
#print(x1,y1,theta1)