# dockerdevice
Attach devices to docker containers at run time
# Nvidia Gpu devices
list Nvidia gpu devices and containers attached to it
```

#dockerdevice gpu-list
+-------+------------------------------------------+-----------------------------+
| Index | UUID                                     | Attached-container          |
+-------+------------------------------------------+-----------------------------+
|     0 | GPU-3435825e-aedc-4a48-d3d8-a4128200cb93 | nvidia-gpu0-0,nvidia-gpu0-1 |
|     1 | GPU-bbe78470-6bb4-1d90-92f9-b99265f7f3e0 | nvidia-gpu1-0               |
|     2 | GPU-9960fbf6-16ed-3414-e4d1-756b91528e2e | nvidia-gpu2-0               |
|     3 | GPU-d57f1920-923d-5855-8235-283f92226939 | mygpu,nvidia-gpu3-0         |
+-------+------------------------------------------+-----------------------------+
#

```
Add gpu device id 2 to running container mygpu
```
#dockerdevice gpu-add --gpu 2 --container mygpu
OK
#
```
Remove gpu device id 2 from a running container mygpu
```
#dockerdevice gpu-remove --gpu 2 --container mygpu
OK
#
```
