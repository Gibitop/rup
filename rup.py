#!/usr/bin/python3

project_name = ''
remote_path = ''
local_path = ''
launch_paramters = []

from os.path import isdir
if not isdir(remote_path):
    print('Could not get to remote path\nExiting...')
    exit(-1)

from shutil import rmtree as rmdir
from shutil import copytree as cpdir
from os import mkdir
from os.path import getmtime as mtime
from subprocess import run
from time import sleep

time = -1


def main():
    print('Welocome to RUP')
    global local_path, remote_path
    local_path += '/' + project_name + '/'
    remote_path += '/'
    while True:
        if (check()):
            launch()
        sleep(1)


def check():
    global time
    ret = False
    if isdir(remote_path):
        new_time = mtime(remote_path)
        if not time == -1:
            if new_time > time:
                ret = True
        time = new_time
        return ret
    else:
        print('Disconected from remote\nExiting...')
        exit(-2)


def launch():
    global remote_path, local_path
    rp = remote_path
    lp = local_path
    full_installation = True

    if isdir(lp):
        full_installation = False
        print('Partial installation mode.')
        rp += '/' + project_name
        lp += '/' + project_name
        if isdir(lp):
            rmdir(lp)
            print('Deleting last installation...')
        print('Downloading the project name directory...')

    if full_installation:
        print('Full installation mode.')
        print('Downloading whole project...')
    cpdir(rp, lp)

    if full_installation:
        print('Modifying .sh file...')
        with open(lp + '/' + project_name + '.sh', 'a', encoding='utf8') as file:
            file.write(' ' + ' '.join(launch_paramters))

    print('Running the game...')
    if not full_installation:
        lp += '/../'
    run([lp + '/' + project_name + '.sh'])
    print('\Game closed.')


if __name__ == "__main__":
    main()
