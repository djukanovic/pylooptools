import os, sys
from setuptools import setup

from distutils.core import setup
from distutils.command.install import install as _install




class install(_install):
	def run(self):
		_install.run(self)
		self.execute(_post_install, (self.install_lib,),msg="Running post install task")

def _post_install(dir):
	runp=os.path.join(dir, 'pylooptools/scripts/')
    	os.system('/usr/bin/env python '+runp +'/compile_looptools '+runp)


setup(name='pylooptools',
      version='0.1',
      description='Python bindings for LoopTools library.',
      url='http://github.com/djukanovic/pylooptools',
      author='Dalibor Djukanovic',
      author_email='d.djukanovic@him.uni-mainz.de',
      license='gpl',
      packages=['pylooptools'],
      cmdclass={'install': install},
      package_data={'pylooptools': ['scripts/*']},
      zip_safe=False)
