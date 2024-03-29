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

m_name = ""
prefix = ""
suffix = ""
h_ph = ""
c_ph = ""
w_ph = ""
email = ""
address = ""
t = datetime.today()
t = t.strftime( "%Y-%m-%d %H:%M:%S" )
t2 = "3001-00-00 00:00:00"

try:
	if form.getvalue("prefix"):
		prefix = form.getvalue("prefix")
	if not form.getvalue("f_name"):
		raise NameError
	if form.getvalue("m_name"):
		m_name = form.getvalue("m_name")
	if not form.getvalue("l_name"):
		raise NameError
	if form.getvalue("suffix"):
		suffix = form.getvalue("suffix")
	if form.getvalue("h_ph"):
		h_ph = form.getvalue("h_ph")
	if form.getvalue("c_ph"):
		c_ph = form.getvalue("c_ph")
	if form.getvalue("w_ph"):
		w_ph = form.getvalue("w_ph")
	if form.getvalue("email"):
		email = form.getvalue("email")
	if form.getvalue("address"):
		address = form.getvalue("address")
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	
	cur.execute("""INSERT INTO Users (Prefix,F_Name,M_Name,L_Name,Postfix,H_PH,C_PH,W_PH,Email,Address,Modify,Expire,Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"Active")""",(prefix,form.getvalue("f_name"),m_name,form.getvalue("l_name"),suffix,h_ph,c_ph,w_ph,email,address,t,t))
	cur.execute("""select * from Users where Prefix=%s AND F_Name=%s AND M_Name=%s AND L_Name=%s AND Postfix=%s AND H_PH=%s AND C_PH=%s AND W_PH=%s AND Email=%s AND Address=%s AND Modify=%s""",(prefix,form.getvalue("f_name"),m_name,form.getvalue("l_name"),suffix,h_ph,c_ph,w_ph,email,address,t))
	x = cur.fetchall()
	ms.close()
	
	UID = str(x[0][0])
	while len(UID) < 9:
		UID = "0" + UID
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
	print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
	print "\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	print "\t\t<font color=\"#FFFFFF\"><center><h1>User Successfully Added!</h1></center></font></td>"
	print "\t</tr>\n\t<tr>"

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
	print "</BODY>\n</HTML>"
	      ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                          