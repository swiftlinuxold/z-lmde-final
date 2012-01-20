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
is_chroot = os.path.exists('/home/mint')
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
os.system('bleachbit --sysinfo') # Creates /root/.config/bleachbit/bleachbit.ini

# bleachbit.ini: BleachBit settings
# Removes languages other than English and removes log files
src = dir_develop + '/remove-languages/root_config_bleachbit/bleachbit.ini'
dest = '/root/.config/bleachbit/bleachbit.ini'
shutil.copy (src, dest)

os.system ('bleachbit --preset -d') # Executes BleachBit with the /root/.config/bleachbit/bleachbit.ini settings

# Delete all languages other than English and template from /usr/share/linuxmint/locale
def elim_dir (dir_to_elim): 
    if (os.path.exists(dir_to_elim)):
        shutil.rmtree (dir_to_elim)
		
print "Deleting languages other than English from /usr/share/linuxmint/locale"
elim_dir ("af")
elim_dir ("am")		
elim_dir ("ar")
elim_dir ("ast")
elim_dir ("ban")
elim_dir ("be")
elim_dir ("ber")
elim_dir ("bg")

elim_dir ("bn")
elim_dir ("bs")
elim_dir ("ca")
elim_dir ("ckb")
elim_dir ("cs")
elim_dir ("csb")
elim_dir ("cv")
elim_dir ("cy")

elim_dir ("da")
elim_dir ("de")
elim_dir ("el")
elim_dir ("eo")

elim_dir ("es")
elim_dir ("et")
elim_dir ("eu")
elim_dir ("fa")
elim_dir ("fi")
elim_dir ("fo")
elim_dir ("fr")
elim_dir ("ga")

elim_dir ("gaa")
elim_dir ("gl")
elim_dir ("gv")
elim_dir ("he")
elim_dir ("hi")
elim_dir ("hr")
elim_dir ("hu")
elim_dir ("hy")

elim_dir ("ia")
elim_dir ("id")
elim_dir ("is")
elim_dir ("it")
elim_dir ("ja")
elim_dir ("jv")
elim_dir ("kab")
elim_dir ("kk")

elim_dir ("km")
elim_dir ("kn")
elim_dir ("ko")
elim_dir ("lb")
elim_dir ("lt")
elim_dir ("lv")
elim_dir ("mk")
elim_dir ("ml")

elim_dir ("mr")
elim_dir ("ms")
elim_dir ("nb")
elim_dir ("nds")
elim_dir ("ne")
elim_dir ("nl")
elim_dir ("nn")
elim_dir ("oc")

elim_dir ("pa")
elim_dir ("pap")
elim_dir ("pl")
elim_dir ("pt")
elim_dir ("pt_BR")
elim_dir ("pt_PT")
elim_dir ("ro")
elim_dir ("ru")

elim_dir ("sco")
elim_dir ("si")
elim_dir ("sk")
elim_dir ("sl")
elim_dir ("sn")
elim_dir ("sq")
elim_dir ("sr")
elim_dir ("sr@latin")

elim_dir ("sv")
elim_dir ("ta")
elim_dir ("te")
elim_dir ("th")
elim_dir ("tl")
elim_dir ("tr")
elim_dir ("uk")

elim_dir ("ur")
elim_dir ("vi")
elim_dir ("zh_CN")
elim_dir ("zh_HK")
elim_dir ("zh_TW")

# Remove packages mentioned in locales

print "FINISHED REMOVING LANGUAGES"
print "==========================="
