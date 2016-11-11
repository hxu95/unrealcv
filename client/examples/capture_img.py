# This is a 10 lines python example to show how to generate an image dataset with image, depth and object_mask.
# Read https://unrealcv.github.io/tutorial/getting_started.html before trying this script
# Note: if you need high-accuracy depth, please use `vget /camera/0/depth depth.exr`
#import json; camera_trajectory = json.load(open('camera_traj.json'))
import json; camera_trajectory = json.load(open('angles.json'))

from unrealcv import client
client.connect()
# Get object information
obj_info = client.request('vget /objects')
i = 0
for entry in camera_trajectory:

    # Set position of the first camera
    #print entry
    #print entry['location']
    #print entry['rotation']
    client.request('vset /camera/0/location {x} {y} {z}'.format(**entry['location']))
    client.request('vset /camera/0/rotation {pitch} {yaw} {roll}'.format(**entry['rotation']))
    # Get image and ground truth
    #modes = ['lit', 'depth', 'object_mask']

    #[im, dep, obj] = [client.request('vget /camera/0/%s' % m) for m in modes]
    #locstring = 'loc_{x}_{y}_{z}'.format(**entry['location'])
    #rotstring = 'rot_{pitch}_{yaw}_{roll}'.format(**entry['rotation'])
    #filename = locstring + "_" + rotstring
    #print filename

    #testing
    f = 'file' + str(i) + '.png'

    im = client.request('vget /camera/0/lit %s' % f)
    #print ['%s is saved to %s' % (k, v) for (k,v) in zip(modes, [im, dep, obj])]
    print ['%s is saved to %s' %(f, im)]
    i = i + 1
