import os
import sys
import urllib
import subprocess

os.system("clear")

print "  _           _        _ _ _               _   _                _     _ _   "
print " (_)         | |      | | (_)             | | | |              | |   (_) |  "
print "  _ _ __  ___| |_ __ _| | |_ _ __   __ _  | |_| |__   ___   ___| |__  _| |_ "
print " | | '_ \/ __| __/ _` | | | | '_ \ / _` | | __| '_ \ / _ \ / __| '_ \| | __|"
print " | | | | \__ \ || (_| | | | | | | | (_| | | |_| | | |  __/ \__ \ | | | | |_ "
print " |_|_| |_|___/\__\__,_|_|_|_|_| |_|\__, |  \__|_| |_|\___| |___/_| |_|_|\__|"
print "                                    __/ |                                   "
print "                                   |___/                                    "

def download(file_url,local_filename):
	web_file = urllib.urlopen(file_url)
	local_file = open(local_filename, 'w')
	local_file.write(web_file.read())
	web_file.close()
	local_file.close()

def get_windows_pip_path():
	python_dir = sys.executable
	split = python_dir.split("\\")
	pip_path = ""
	for i in range(0,len(split)-1):
		pip_path = "%s/%s" %(pip_path,split[i])
	pip_path = "%s/Scripts/pip" %pip_path[1:]

	return pip_path

def pip_install_module(module_name):
	pip_path = "pip"
	DEVNULL = open(os.devnull,'wb')
	new_installation = True

	try:
		subprocess.call(["pip"], stdout=DEVNULL) #if pip boi is installed already than u STUPIDDD
	except OSError as e:
		if(sys.platform[:3] == "win"):
			pip_path = get_windows_pip_path()
			try:
				subprocess.call([pip_path],stdout=DEVNULL)
				new_installation = False
				print "[+] Found Windows pip at '%s'" %pip_path
			except:
				pass

		if(new_installation):
			print "[!] pip is not installed wtffffff."

			if(os.path.isfile("get-pip.py") is False):
				print "[*] Downloading get-pip.py.."
				download("https://bootstrap.pypa.io/get-pip.py","get-pip.py")
			else:
				print "[+] get-pip-py found in the current directory."

	    	os.system("python get-pip.py")

	    	try:
	    		subprocess.call(["pip"],stdout=DEVNULL)
	    	except:
	    		if(sys.platform[:3] == "win"):
		    		python_dir = sys.executable # "C:\\Python27\\python.exe"
		    		split = python_dir.split("\\")
		    		pip_path = ""
		    		for i in range(0,len(split)-1): # lets avoid python.exe bc shitz dangerous
		    			pip_path = "%s/%s" %(pip_path,split[i])

		    		pip_path = "%s/Scripts/pip" %pip_path[1:]

	if(new_installation):
		try:
			os.remove("get-pip.py")
		except:
			pass

	os.system("%s install --upgrade pip" %pip_path)
	print "\n[*] Installing module like a boooosssss '%s'" %module_name
	os.system("%s install %s" %(pip_path,module_name))

