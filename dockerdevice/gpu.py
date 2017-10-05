from cliff.lister import Lister
from pynvml import *

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
        return (('Index', 'UUID'  ), ((item, dict_gpu[item]) for item in dict_gpu ))
