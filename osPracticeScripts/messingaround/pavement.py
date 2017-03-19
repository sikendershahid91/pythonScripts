#!/usr/bin/python 

from paver.easy import *
import paver.doctools
import os 
import glob
import shutil

@task
def run():
	sh('pwd')
	pass

@task
@needs(['run'])
def default():
	pass
