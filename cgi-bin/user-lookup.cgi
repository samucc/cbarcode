#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from datetime import *
import MySQLdb

import configurables

form = cgi.FieldStorage()


host=configurables.host()
database=configurables.db()
user = configurables.user()
passwd = configurables.passwd()

try:
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	cur.execute("""select * from Users where UID=%s""",(form.getvalue("skew")))
	x = cur.fetchall()
	ms.close()

	UID = str(x[0][0])
	#if len(UID) < 9:
	while len(UID) < 9:
		UID = "0" + UID 
	if str(x) == "()":
		raise NameError
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE>" + UID +"</TITLE>\n"
	print "</HEAD>\n<BODY>"
	
# New	
	print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
	print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
	print "\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Personal Information:</b></font></td>"
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
	print "\t\tPrefix:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][1] =="":
		print "\t\t&nbsp;</td>"
	else:
		print "\t\t%s</td>"%(x[0][1])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tFirst Name:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][2])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tMiddle Name:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][3] =="":
		print "\t\t&nbsp;</td>"
	else:
		print "\t\t%s</td>"%(x[0][3])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tLast Name:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][4])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tSuffix:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][5] =="":
		print "\t\t&nbsp;</td>"
	else:
		print "\t\t%s</td>"%(x[0][5])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Contact Information:</b></font></td>"
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tHome Phone Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][6] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][6])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tCell Phone Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][7] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][7])
		
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tWork Phone Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][8] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][8])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tEmail Address:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][9] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][9])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tPostal Address:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][10] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][10])
		
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Account Information:</b></font></td>"
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tUser ID Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(UID)
	
	print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(UID)
	print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tLast Modified:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][11].strftime("%Y-%m-%d %H:%M:%S"))
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tExpiration:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][12].strftime("%Y-%m-%d %H:%M:%S"))
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tCurrent Status:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	
	if str(x[0][13]) == "Set([\'Active\'])":
		print "\t\tActive</td>"
	elif str(x[0][13]) == "Set([\'Expired\'])":
		print "\t\tExpired</td>"
	elif str(x[0][13]) == "Set([\'Suspended\'])":
		print "\t\tSuspended</td>"
	elif str(x[0][13]) == "Set([\'Deleted\'])":
		print "\t\tDeleted</td>"
	else:
		print "\t\t%s</td>"%(str(x[0][13]))
	
	print "</tr><tr>"
    	print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
    	print "<select name=\"ht\">\n"
    	print "<option>Full<option>Half"
    	print "</select>\n"
    	print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
	print "</td>"
	
	print "\t</tr>\n</table>\n</FORM>\n</BODY>\n</HTML>"
	
except:
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>"
	print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE> UID not found!</TITLE>\n"
	print "<BODY>"  
	print "<h1>Error: User Not Found!</h1>"
	print "Sorry, but the User ID is invalid."
	print "</BODY>\n</HTML>"         ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����        