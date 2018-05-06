
#!/usr/bin/python
import re

phone   =   "2004-959-559 # This is Phone Number"
path     =   "Comio_System_Helper_7.0.0_WD.apk"

print 'original string : ',path
print '\n'

# Delete Python-style comments
num =   re.sub(r'#.*$', "", phone)

name_re = re.compile('.[(?y)].+[a-z].+[(0-9)].[(0-9)].[^W]\S')

# name_search = name_re.search(path)
#
# if name_search:
#     content = path
# print content

apk =   re.sub(name_re,"System_Helper",path)
print ' string modified : '
print "Phone Num    : ", num
print "APK          : ", apk
print '\n'

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
apk = re.sub(r'', "", path)

print "Phone Num            : ", num
print "Apk name directory   : ", apk
