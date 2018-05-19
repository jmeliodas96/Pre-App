
#!/usr/bin/python
import re

# line = "Cats are smarter than dogs";

line = """?xml version='1.0' encoding='UTF-8'?><S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"><S:Body><ns2:getResponse xmlns:ns2="http://WebService/"><return><adj_file>false</adj_file><content_notification_url></content_notification_url><content_notification_url_en></content_notification_url_en><content_notification_url_pt></content_notification_url_pt><createdat/><date>2018-04-16 16:20:10.766</date><filename>http://updates.overtheairupdates.com/zips/N1if45kSYMDzdTBaoGw9QsWXbKu8VgxIy3rULHOpEl2jZeqcnR.zip</filename><flag>false</flag><icon_apk_f></icon_apk_f><icon_apk_i></icon_apk_i><icon_carrier_f></icon_carrier_f><icon_carrier_i></icon_carrier_i><icon_notification_url></icon_notification_url><id>2077</id><lastupdate><nanos>766000000</nanos></lastupdate><link_notification_url></link_notification_url><minbattery>10</minbattery><new_name>undefined</new_name><old_name>undefined</old_name><ota_message></ota_message><pop_descripcion></pop_descripcion><pop_intro></pop_intro><pop_message></pop_message><pop_titulo></pop_titulo><shortcut>false</shortcut><shortcut_add>undefined</shortcut_add><shortcut_remove>undefined</shortcut_remove><sizedecompressed>0.0</sizedecompressed><sizefilezip>12.0</sizefilezip><sizeinstalled>0.0</sizeinstalled><title_notification_url></title_notification_url><title_notification_url_en></title_notification_url_en><title_notification_url_pt></title_notification_url_pt><type>1</type><unpackages>undefined</unpackages><updatedat/><urlIcon1></urlIcon1><urlIcon2></urlIcon2></return></ns2:getResponse></S:Body></S:Envelope>"""


# path        =   "Comio_System_Helper_7.0.0_WD.apk"
# path_re     =   re.compile('.[(?y)].+[a-z].+[(0-9)].[(0-9)].[^W]\S')
id_re   =   re.compile('[(?<)].[a-z].[0-9].[0-9].[<].[a-z].[>]')
date_re   =   re.compile('[<].[a-z].[date].[0-9].[0-9].[-][0-9].[-].[0-9].[0-9][0-9].[0-9].[:].[0-9].[0-9].[6][<].[a-z].[date].[>]')



# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
searchObj2  =   re.search(id_re, line)
searchObj3  =   re.search(date_re, line)
#
if searchObj2:
#    # print "searchObj.group() : ", searchObj.group()
#    # print "searchObj.group(1) : ", searchObj.group(1)
#    # print "searchObj.group(2) : ", searchObj.group(2)
#
   print '\n'
   print "searchObj2.group(1) : ", searchObj2.group()


if searchObj3:

    print "searchObj3.group(1) : ", searchObj3.group()
    content = searchObj3.group()
    # print content
    print len(content)

else:
   print "Nothing found!!"
