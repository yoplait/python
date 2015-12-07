
import sys
import os
import platform


print "Your systems is :"
print os.name
print platform.system()
print platform.release()

from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
   # linux
   print "linux"
elif _platform == "darwin":
   # MAC OS X
   print "Mac"
elif _platform == "win32":
   # Windows
   print "Win"


def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))