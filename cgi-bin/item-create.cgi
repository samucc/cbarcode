#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb

import configurables

form = cgi.FieldStorage()


host=configurables.host()
database=configurables.db()
user = configurables.user()
passwd = configurables.passwd()

itemclass = ""
desc = ""
owner = ""
status = ""

try:
	if not form.getvalue("class"):
		raise NameError
	else:
		if form.getvalue("class") == "Item":
			itemclass = "I"
		else:
			itemclass = "S"
	if not form.getvalue("desc"):
		raise NameError
	else:
		desc = form.getvalue("desc")
	if not form.getvalue("status"):
		raise NameError
	else:
		status = form.getvalue("status")
	if form.getvalue("owner"):
		owner = form.getvalue("owner")

	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	
	cur.execute("""INSERT INTO Items (Class,Description,Owner,Status) VALUES (%s,%s,%s,%s)""",(itemclass,desc,owner,status))
	cur.execute("""select * from Items where Class=%s AND Description=%s AND Owner=%s AND Status=%s""",(itemclass,desc,owner,status))
	x = cur.fetchall()
	ms.close()
	
	IID = str(x[0][1])
	while len(IID) < 8:
		IID = "0" + IID
	
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
	print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"

	print "\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	if str(x[0][0]) == "S" or str(x[0][0]) == "Set([\'S\'])":
		print "\t\t<font color=\"#FFFFFF\"><center><h1>Service Successfully Added!</h1></center></font></td>"
	else:
		print "\t\t<font color=\"#FFFFFF\"><center><h1>Item Successfully Added!</h1></center></font></td>"
	print "\t</tr>\n\t<tr>"
		
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	if str(x[0][0]) == "Set([\'S\'])" or str(x[0][0]) == "S":
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Service Information:</b></font></td>"
	else:
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Item Information:</b></font></td>"
	print "\t</tr>\n\t<tr>"
	
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
	print "\t\tItem Identificaiton Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if str(x[0][0]) == "Set([\'S\'])":
		print "\t\t%s</td>"%("S"+IID)
		print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%("S"+IID)
		
	elif str(x[0][0]) == "Set([\'I\'])":
		print "\t\t%s</td>"%("I"+IID)
		print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%("I"+IID)
	else:
		print "\t\t%s</td>"%(x[0][0]+IID)
	print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tDescription:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][2])
	
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tOwner:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if x[0][3] =="":
		print "\t\t(none provided)</td>"
	else:
		print "\t\t%s</td>"%(x[0][3])
	
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
		print "\t\t%s</td>"%(x[0][4])
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
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<h1>An Error Was Encountered.</h1>"
	print "Please check to see if the for was correctly filled out.<br>"
	print "If this problem continues, please contact your administrator."
	print "</BODY>\n</HTML>"      ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����        