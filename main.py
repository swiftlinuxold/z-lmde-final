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
elim_dir ("/usr/share/linuxmint/locale/af")
elim_dir ("/usr/share/linuxmint/locale/am")		
elim_dir ("/usr/share/linuxmint/locale/ar")
elim_dir ("/usr/share/linuxmint/locale/ast")
elim_dir ("/usr/share/linuxmint/locale/ban")
elim_dir ("/usr/share/linuxmint/locale/be")
elim_dir ("/usr/share/linuxmint/locale/ber")
elim_dir ("/usr/share/linuxmint/locale/bg")

elim_dir ("/usr/share/linuxmint/locale/bn")
elim_dir ("/usr/share/linuxmint/locale/bs")
elim_dir ("/usr/share/linuxmint/locale/ca")
elim_dir ("/usr/share/linuxmint/locale/ckb")
elim_dir ("/usr/share/linuxmint/locale/cs")
elim_dir ("/usr/share/linuxmint/locale/csb")
elim_dir ("/usr/share/linuxmint/locale/cv")
elim_dir ("/usr/share/linuxmint/locale/cy")

elim_dir ("/usr/share/linuxmint/locale/da")
elim_dir ("/usr/share/linuxmint/locale/de")
elim_dir ("/usr/share/linuxmint/locale/el")
elim_dir ("/usr/share/linuxmint/locale/eo")

elim_dir ("/usr/share/linuxmint/locale/es")
elim_dir ("/usr/share/linuxmint/locale/et")
elim_dir ("/usr/share/linuxmint/locale/eu")
elim_dir ("/usr/share/linuxmint/locale/fa")
elim_dir ("/usr/share/linuxmint/locale/fi")
elim_dir ("/usr/share/linuxmint/locale/fo")
elim_dir ("/usr/share/linuxmint/locale/fr")
elim_dir ("/usr/share/linuxmint/locale/ga")

elim_dir ("/usr/share/linuxmint/locale/gaa")
elim_dir ("/usr/share/linuxmint/locale/gl")
elim_dir ("/usr/share/linuxmint/locale/gv")
elim_dir ("/usr/share/linuxmint/locale/he")
elim_dir ("/usr/share/linuxmint/locale/hi")
elim_dir ("/usr/share/linuxmint/locale/hr")
elim_dir ("/usr/share/linuxmint/locale/hu")
elim_dir ("/usr/share/linuxmint/locale/hy")

elim_dir ("/usr/share/linuxmint/locale/ia")
elim_dir ("/usr/share/linuxmint/locale/id")
elim_dir ("/usr/share/linuxmint/locale/is")
elim_dir ("/usr/share/linuxmint/locale/it")
elim_dir ("/usr/share/linuxmint/locale/ja")
elim_dir ("/usr/share/linuxmint/locale/jv")
elim_dir ("/usr/share/linuxmint/locale/kab")
elim_dir ("/usr/share/linuxmint/locale/kk")

elim_dir ("/usr/share/linuxmint/locale/km")
elim_dir ("/usr/share/linuxmint/locale/kn")
elim_dir ("/usr/share/linuxmint/locale/ko")
elim_dir ("/usr/share/linuxmint/locale/lb")
elim_dir ("/usr/share/linuxmint/locale/lt")
elim_dir ("/usr/share/linuxmint/locale/lv")
elim_dir ("/usr/share/linuxmint/locale/mk")
elim_dir ("/usr/share/linuxmint/locale/ml")

elim_dir ("/usr/share/linuxmint/locale/mr")
elim_dir ("/usr/share/linuxmint/locale/ms")
elim_dir ("/usr/share/linuxmint/locale/nb")
elim_dir ("/usr/share/linuxmint/locale/nds")
elim_dir ("/usr/share/linuxmint/locale/ne")
elim_dir ("/usr/share/linuxmint/locale/nl")
elim_dir ("/usr/share/linuxmint/locale/nn")
elim_dir ("/usr/share/linuxmint/locale/oc")

elim_dir ("/usr/share/linuxmint/locale/pa")
elim_dir ("/usr/share/linuxmint/locale/pap")
elim_dir ("/usr/share/linuxmint/locale/pl")
elim_dir ("/usr/share/linuxmint/locale/pt")
elim_dir ("/usr/share/linuxmint/locale/pt_BR")
elim_dir ("/usr/share/linuxmint/locale/pt_PT")
elim_dir ("/usr/share/linuxmint/locale/ro")
elim_dir ("/usr/share/linuxmint/locale/ru")

elim_dir ("/usr/share/linuxmint/locale/sco")
elim_dir ("/usr/share/linuxmint/locale/si")
elim_dir ("/usr/share/linuxmint/locale/sk")
elim_dir ("/usr/share/linuxmint/locale/sl")
elim_dir ("/usr/share/linuxmint/locale/sn")
elim_dir ("/usr/share/linuxmint/locale/sq")
elim_dir ("/usr/share/linuxmint/locale/sr")
elim_dir ("/usr/share/linuxmint/locale/sr@latin")

elim_dir ("/usr/share/linuxmint/locale/sv")
elim_dir ("/usr/share/linuxmint/locale/ta")
elim_dir ("/usr/share/linuxmint/locale/te")
elim_dir ("/usr/share/linuxmint/locale/th")
elim_dir ("/usr/share/linuxmint/locale/tl")
elim_dir ("/usr/share/linuxmint/locale/tr")
elim_dir ("/usr/share/linuxmint/locale/uk")

elim_dir ("/usr/share/linuxmint/locale/ur")
elim_dir ("/usr/share/linuxmint/locale/vi")
elim_dir ("/usr/share/linuxmint/locale/zh_CN")
elim_dir ("/usr/share/linuxmint/locale/zh_HK")
elim_dir ("/usr/share/linuxmint/locale/zh_TW")

# The following directories should be DELETED:
# /home/(username)/.config/chromium 
# /home/(username)/.mozilla
# /home/(username)/.opera
print "Deleting selected directories and files in /home"
elim_dir ("/home/" + uname + "/.config/chromium")
elim_dir ("/home/" + uname + "/.mozilla")
elim_dir ("/home/" + uname + "/.opera")

# The following file should be deleted: /home/(username)/.linuxmint/mintMenu/apt.cache
os.remove ("/home/" + uname + "/.linuxmint/mintMenu/apt.cache")




print "FINISHED REMOVING LANGUAGES"
print "==========================="
