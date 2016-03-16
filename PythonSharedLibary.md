Code example for binding c shared library to python.

```
#!/usr/bin/python
from _ctypes import *
import time
showiframe = dlopen("libshowiframe.so.0.0.0")

print type(showiframe)
try: 
    showSinglePic = dlsym(showiframe, "showSinglePic") 
    finishShowSinglePic = dlsym(showiframe, "finishShowSinglePic") 
except OSError, e:  
    showSinglePic = dlsym(showiframe, "_Z13showSinglePicPKc") 
    finishShowSinglePic = dlsym(showiframe, "_Z19finishShowSinglePicv") 

print "Objects binded"
print [showSinglePic,
	finishShowSinglePic]
print call_function(showSinglePic, ("/boot/bootlogo.mvi", ))

time.sleep(5)

print call_function(finishShowSinglePic, ())

dlclose(showiframe)
```