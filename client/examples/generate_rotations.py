import sys, atexit, argparse, json, time
sys.path.append('..')
from unrealcv import client

trajectory = []

angles = [0.0, 120.0, 240.0]
import json; camera_trajectory = json.load(open('camera_traj.json'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='angles.json')
    args = parser.parse_args()

    for [loc, rot] in camera_trajectory:
        # Set position of the first camera
        #client.request('vset /camera/0/location {x} {y} {z}'.format(**loc))
        #client.request('vset /camera/0/rotation {pitch} {yaw} {roll}'.format(**rot))

        #rot = [float(v) for v in client.request('vget /camera/0/rotation').split(' ')]
        #loc = [float(v) for v in client.request('vget /camera/0/location').split(' ')]

        for a in angles:
            for b in angles:
                for c in angles:
                    rot = {'yaw': float(a), 'pitch': float(b), 'roll':float(c)}
                    trajectory.append(dict(rotation = rot, location = loc))
    if len(trajectory) != 0:
        with open(args.filename, 'w') as f:
            json.dump(trajectory, f, indent = 4)