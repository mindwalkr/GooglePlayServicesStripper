#/usr/bin/python
#
# Strips the Google Play Services JAR archive and removes the folders that are specified below.
# This should lower the methods count of the final DEX file and should lower the chance of hitting
# the (dreaded) 64K methods limit.
#

import os
import glob
import shutil
import subprocess
import time

# modify this var to point to your android home location
GOOGLE_PLAY_SERVICES_LOCATION = 'C:\\apps\\android-studio\\sdk\\extras\\google\\google_play_services\\libproject\\google-play-services_lib\\libs'


configuration = {
    'actions'       : True,
    'analytics'     : True,
    'appindexing'   : False,
    'appstate'      : True,
    'auth'          : True,
    'cast'          : False,
    'common'        : True,         # probably always need this
    'drive'         : False,
    'dynamic'       : True,
    'games'         : False,
    'gcm'           : True,
    'identity'      : True,
    'internal'      : True,         # probably always need this
    'location'      : True,
    'maps'          : False,
    'panorama'      : False,
    'plus'          : True,
    'security'      : False,
    'tagmanager'    : True,
    'wallet'        : False,
    'wearable'      : False
}

# some vars, you probably don't need to change
PLAY_SERVICES_FILENAME='google-play-services.jar'
PLAY_SERVICES_TEMP_DIR='google-play-services-temp'
PLAY_SERVICES_NESTED_PATH='com' + os.sep + 'google' + os.sep + 'android' + os.sep + 'gms'
PLAY_SERVICES_OUTPUT_FILE='google-play-services-STRIPPED.jar'

# ---------------------------------------------------------------------------
# YOU SHOULD NOT NEED TO TOUCH ANYTHING BELOW THIS LINE
# ---------------------------------------------------------------------------

# remove temp directory contents if it exists, then remake it as needed
if os.path.exists(PLAY_SERVICES_TEMP_DIR):
    if os.path.isdir(PLAY_SERVICES_TEMP_DIR):
        shutil.rmtree(PLAY_SERVICES_TEMP_DIR)
        time.sleep(1)                           # delete+create after too quickly = crash on win7
    else:
        os.remove(PLAY_SERVICES_TEMP_DIR)       # why is this a file ?
        
os.makedirs(PLAY_SERVICES_TEMP_DIR)
    
# copy google play services library
shutil.copy2(GOOGLE_PLAY_SERVICES_LOCATION + os.sep + PLAY_SERVICES_FILENAME, PLAY_SERVICES_TEMP_DIR + os.sep)

# explode the file
original_directory = os.getcwd()
os.chdir(PLAY_SERVICES_TEMP_DIR)
subprocess.call(['jar', 'xf', PLAY_SERVICES_FILENAME])

# remove those pieces we don't want
working_path = os.getcwd() + os.sep + PLAY_SERVICES_NESTED_PATH
for directory in os.listdir(working_path):
    if configuration.has_key(directory) and not configuration[directory]:
        shutil.rmtree(working_path + os.sep + directory)

# implode stripped file
subprocess.call(['jar', 'cf', PLAY_SERVICES_OUTPUT_FILE, 'com'+os.sep])

# copy it to the root dir
shutil.copy2(PLAY_SERVICES_OUTPUT_FILE, '..'+os.sep)

# cleanup
os.chdir(original_directory)
shutil.rmtree(PLAY_SERVICES_TEMP_DIR)
