import sys, atexit, argparse, json, time, random
sys.path.append('..')
from unrealcv import client

trajectory = []

#realistic rendering
# [min, max]
x_range = [-200, 140]
y_range = [-300, 400]
z_range = [0, 90]



#camera field of view = 90

# roll = axis through object
# yaw = vertical axis -> left and right rotation
# pitch = horizontal axis -> up and down rotation
# https://sidvind.com/wiki/Yaw,_pitch,_roll_camera
yaw_angles = [0.0, 90.0, 180.0, 270.0]

# 0, 30 up and down
pitch_angles = [0.0, 30.0, -30.0]

# no roll
roll_angle = 0.0

#input for (x,y,z)
import json; camera_trajectory = json.load(open('camera_traj.json'))

imgs = 0

#number of (x, y, z) coordinates to take
n = 25

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    #output = angles.json
    parser.add_argument('--filename', default='angles.json')
    args = parser.parse_args()

    for i in range(0, n):
    #for [loc, rot] in camera_trajectory:
        # Set position of the first camera
        #client.request('vset /camera/0/location {x} {y} {z}'.format(**loc))
        #client.request('vset /camera/0/rotation {pitch} {yaw} {roll}'.format(**rot))

        #rot = [float(v) for v in client.request('vget /camera/0/rotation').split(' ')]
        #loc = [float(v) for v in client.request('vget /camera/0/location').split(' ')]

        #choose a random float in the range
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        z = random.uniform(z_range[0], z_range[1])

        for a in yaw_angles:
            for b in pitch_angles:
                rot = {'yaw': float(a), 'pitch': float(b), 'roll':float(roll_angle)}
                loc = {'x': float(x), 'y': float(y), 'z':float(z)}
                trajectory.append(dict(rotation = rot, location = loc))
                imgs = imgs+ 1

    if len(trajectory) != 0:
        with open(args.filename, 'w') as f:
            json.dump(trajectory, f, indent = 4)
            print imgs