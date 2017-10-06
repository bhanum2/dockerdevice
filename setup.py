from setuptools import setup, find_packages

PROJECT = 'dockerdevice'
VERSION = '2017.10.5'

setup(name=PROJECT,
      version=VERSION,
      description='docker device',
      url='https://github.com/bhanum2/dockerdevice',
      author='bhanum2',
      install_requires=['cliff'],
      maintainer='bhanum2',
      maintainer_email='no-reply@gmail.com',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,

      entry_points={
        'console_scripts': [
            'dockerdevice = dockerdevice.main:main'
        ],
        'dockerdevice.client': [
	    'gpu-list = dockerdevice.gpu:GpuList',
	    'gpu-remove = dockerdevice.gpu:GpuRemove',
	    'gpu-add = dockerdevice.gpu:GpuAdd'
        ],
	},

      zip_safe=False,
      platforms=['Any'],
)
