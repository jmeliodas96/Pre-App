
#!/usr/bin/python
import re

line = "Cats are smarter than dogs";


path        =   "Comio_System_Helper_7.0.0_WD.apk"
path_re     =   re.compile('.[(?y)].+[a-z].+[(0-9)].[(0-9)].[^W]\S')



searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
searchObj2 =re.search(path_re, path)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)

   print '\n'
   print "searchObj2.group(1) : ", searchObj2.group()
else:
   print "Nothing found!!"
