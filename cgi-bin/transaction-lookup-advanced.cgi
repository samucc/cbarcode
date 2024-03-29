#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
import configurables
from datetime import *

form = cgi.FieldStorage()
host=configurables.host()
database=configurables.db()
user = configurables.user()
passwd = configurables.passwd()

itemclass = "%"
t = "%"
items = "%"
uid = "%"

try:
	if form.getvalue("skew"):
		itemclass = form.getvalue("skew")[0]
		t = form.getvalue("skew")[1:9]
	
	if form.getvalue("items"):
		items = "%" + form.getvalue("items") + "%"
	
	if form.getvalue("user"):
		uid = form.getvalue("user").strip("\n")	
	
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	cur.execute("""select * from Transactions where Class LIKE %s AND TID LIKE %s AND UID LIKE %s AND Items LIKE %s""",(itemclass,t,uid,items))
	x = cur.fetchall()
	ms.close()
	
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	
	for n in x:
		print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
		print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
		TID = str(n[1])
		while len(TID) < 8:
			TID = "0" + TID
		print "\t<tr>"
		
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><h1>Transaction: %s</h1></font></td>"%TID
		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		if str(n[0]) == "T" or str(n[0]) == "Set([\'T\'])":
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Transaction Information:</b></font></td>"
		else:
			raise NameError
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
		print "\t\tTransaction Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if str(n[0]) == "Set([\'T\'])":
			print "\t\t%s</td>"%("T"+TID)
			print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%("T"+TID)
			print "<input type=\"hidden\" name=\"type\" value=\"B\">"
		else:
			raise NameError
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tDate:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t%s</td>"%(x[0][2].strftime("%Y-%m-%d %H:%M:%S"))
		UID = str(n[3])
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
		print "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(n[4])
		print "\t</tr>\n"
		print "</tr><tr>"
    		print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
   		print "<select name=\"ht\">\n"
   		print "<option>Full<option>Half"
   		print "</select>\n"
  		print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
		print "</td>"
		print "</table>\n</form>"
		
	print "</BODY>\n</HTML>"
	
	
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