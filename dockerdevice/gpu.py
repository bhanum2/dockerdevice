from cliff.lister import Lister
from pynvml import *
import docker
import os
import collections
import pprint

class GpuList(Lister):
    """List Gpus."""

    def take_action(self, args):
	nvmlInit()
	deviceCount = nvmlDeviceGetCount()
	dict_gpu = {}

	for i in range(deviceCount):
        	handle = nvmlDeviceGetHandleByIndex(i)
		dict_gpu[i] =  nvmlDeviceGetUUID(handle)

	nvmlShutdown()


	docker_obj = docker.from_env()
	containers = docker_obj.containers(all=True)
	info = os.lstat('/dev/nvidia0')
	major, minor = divmod(info.st_rdev, 256)
	dict_containers = collections.defaultdict(list)
	for container in containers:
       		container_id = container['Id']
	        container_name = container['Names'][0]
       		container_name = container_name[1:]

	        sys_file_path = '/sys/fs/cgroup/devices/docker/' + container_id + '/devices.list'
       		file_data =  open(sys_file_path, 'r').read().splitlines()
	        for line in file_data:
 			if str(major) in line:
                       		index = line.split()[1].split(':')[1]
				if index == '255':
                             		 continue
	                        dict_containers[index].append(container_name)


	return (('Index', 'UUID', 'Attached-container' ), ((item, dict_gpu[item], ','.join(dict_containers[str(item)])) for item in dict_gpu ))
