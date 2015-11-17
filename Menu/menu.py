#
#
#

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
