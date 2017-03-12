#!/usr/bin/env python

import sys
import os
import readline
import json
import copy

PLATFORM = platform.system()
APP_PATH = None
CONFIG_PATH = None


def main():
    print ("Config ST")

    APP_PATH = 'sublime'
    CONFIG_PATH = os.path.expanduser('~') + '/.config/sublime-text-3'

    config(CONFIG_PATH)
    config_projects(CONFIG_PATH)
    sys.exit(0)

def install():
    exec sudo apt-get install sublime-text

def config_projects():

    session_path = CONFIG_PATH + "/Local/Session.sublime_session"
    name = project_path.split('/')[-1]

    sublime_project = {"folders: []}
    sublime_workspace_path = project_path ..

    with open(sublime_project_path, 'w') as project:
        project.write(json.dumps(sublime_project)
    with open sublime_workspace_path, 'w') as workspace:
        workspace.write(json.dumps({})

    # Create new Session File
    sublime_session = {"workspaces": {"recent_workspaces": [] }}
    sublime_session["workspaces"]["recent_workspaces"].append(sublime_workspace_path)
    with open(sublime_session_path, 'w') as session:
        session.write(json.dumps(sublime_session)



def config():

    prompt = raw_input("Overwrite?").lower()

    if ['y', 'yes'] in prompt:
        mkdir(CONFIG_PATH)
        mkdir(PACKAGES)
        mkdir(SETTINGS)

        install(PACKAGE_CONTROL)

        copy(themes)
        copy(usersetting)

        print "Subl updated Config"

    else:
        print "Config has not change"




def install_package_control():
    loc = CONFIG_PATH + '/Installed Packages/Package Control.sublime-package'
    url = 'https://packagecontrol.io/Package%20Control.sublime-package'

    curl -O url
    unzip Package\ Control.sublime-package.zip
    mv Package\ Control.sublime-package loc


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Cancelled Operation')
        sys.exit()
