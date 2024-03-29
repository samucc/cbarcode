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
itemclass = "T"
t = datetime.today()
t = t.strftime( "%Y-%m-%d %H:%M:%S" )
try:
	if not form.getvalue("user"):
		raise NameError
	if len(form.getvalue("user")) < 9:
		raise NameError
	if not form.getvalue("items"):
		raise NameError
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	cur.execute("""INSERT INTO Transactions (Class, Date, UID, Items) VALUES (%s,%s,%s,%s)""",(itemclass,t,form.getvalue("user"),form.getvalue("items")))
	cur.execute("""select * from Transactions where Class=%s AND Date=%s AND UID=%s AND Items=%s""",(itemclass,t,form.getvalue("user"),form.getvalue("items")))
	x = cur.fetchall()
	ms.close()
	TID = str(x[0][1])
	while len(TID) < 8:
		TID = "0" + TID
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
	print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
	print "\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	if str(x[0][0]) == "T" or str(x[0][0]) == "Set([\'T\'])":
		print "\t\t<font color=\"#FFFFFF\"><center><h1>Transaction Successfully Completed!</h1></center></font></td>"
	else:
		raise NameError
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
	if str(x[0][0]) == "T" or str(x[0][0]) == "Set([\'T\'])":
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Transaction Information:</b></font></td>"
	else:
		raise NameError
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
	print "\t\tTransaction Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	if str(x[0][0]) == "Set([\'T\'])":
		print "\t\t%s</td>"%("T"+TID)
		print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%("T" + TID)
		print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	else:
		raise NameError
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tDate:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(x[0][2].strftime("%Y-%m-%d %H:%M:%S"))
	UID = str(x[0][3])
	while len(UID) < 9:
		UID = "0" + UID
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tUser Identification Number:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t%s</td>"%(UID)
	print "\t</tr>\n\t<tr>"
	print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
	print "\t\tItems:</td>"
	print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	print "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(x[0][4])
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