import os
from helper import Helper
from config_env import config_env

path_project = config_env()['PATH_PROJECT']

def create_express(name_project):
    Helper.create_folder(name_project)
    os.chdir(f'{path_project}/{name_project}')
    os.system('npm init')
    os.system('npm install express joi')
    os.mkdir('src')
    os.chdir('src')
    Helper.create_many_folders(['controller', 'test', 'common', 'service', 'repository', 'routes'])
