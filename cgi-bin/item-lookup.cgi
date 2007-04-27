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

itemclass = ""
iid = ""

itemclass = form.getvalue("skew")[0]
iid = form.getvalue("skew")[1:9]


try:
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	cur.execute("""select * from Items where Class=%s AND IID=%s""",(itemclass,iid))
	x = cur.fetchall()
	ms.close()
	if str(x) == "()":
		raise NameError
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
	print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
	print "\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	if x[0][0] == "S" or str(x[0][0])=="Set([\'S\'])":
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Service Information:</b></font></td>"
	else:
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Item Information:</b></font></td>"
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
	print "\t\tItem Identificaiton Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(form.getvalue("skew"))
	
	print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(form.getvalue("skew"))
	print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tDescription:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	#print "\t\t%s</td>"%(x[0][2])
	print  "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(x[0][2])
	
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tOwner:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][3] =="":
		print "\t\t(none provided)</td>"
	else:
		#print "\t\t%s</td>"%(x[0][3])
		print  "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(x[0][3])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tStatus:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"

	if str(x[0][4]) == "Set([\'Active\'])":
		print "\t\tActive</td>"
	elif str(x[0][4]) == "Set([\'Inactive\'])":
		print "\t\tInactive</td>"
	elif str(x[0][4]) == "Set([\'Expired\'])":
		print "\t\tExpired</td>"
	else:
		print "\t\t%s</td>"%(str(x[0][4]))
	
	print "</tr><tr>"
    	print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
   	print "<select name=\"ht\">\n"
   	print "<option>Full<option>Half"
   	print "</select>\n"
  	print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
	print "</td>"
	print "\t</tr>\n</table>\n</form>\n</BODY>\n</HTML>"
	
except:
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>"
	print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE> IID not found!</TITLE>\n"
	print "<BODY>"  
	print "<h1>Error: Item Not Found!</h1>"
	print "Sorry, but the Item ID is invalid."
	print "</BODY>\n</HTML>"         ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����        