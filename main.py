#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/usr/lib/live-installer')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================
import shutil

print "========================"
print "BEGIN REMOVING LANGUAGES"
os.system('apt-get install -y bleachbit') # Add BleachBit

# bleachbit.ini: BleachBit settings
# Removes languages other than English and removes log files
src = dir_develop + '/remove-languages/root_config_bleachbit/bleachbit.ini'
dest = '/root/.config/bleachbit'
shutil.copy (src, dest)

os.system ('bleachbit --preset -d') # Executes BleachBit


print "FINISHED REMOVING LANGUAGES"
print "==========================="
