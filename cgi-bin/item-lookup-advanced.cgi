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

iid = "%"
itemclass = "%"
owner = "%"
desc = "%"
status = "%"

try:
	if form.getvalue("skew"):
		itemclass = form.getvalue("skew")[0]
		iid = form.getvalue("skew")[1:9]
		
	if form.getvalue("class"):
		if form.getvalue("class") == "Any":
			itemclass = "%"
		if form.getvalue("class") == "Item":
			itemclass = "I"
		if form.getvalue("class") == "Service":
			itemclass = "S"
	
	if form.getvalue("desc"):
		desc = "%" + form.getvalue("desc") + "%"
	
	if form.getvalue("owner"):
		owner = "%" + form.getvalue("owner") + "%"
	
	if form.getvalue("status"):
		status = form.getvalue("status")
	
	if form.getvalue("status") == "Any":
		status = "%"
	
	ms = MySQLdb.connect(host,user,passwd,database)
	
	cur = ms.cursor()
	
	cur.execute("""SELECT * FROM Items WHERE Class LIKE %s AND IID LIKE %s AND Description LIKE %s AND Owner LIKE %s AND Status LIKE %s""",(itemclass,iid,desc,owner,status))
	
	x = cur.fetchall()
	ms.close()
	
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	
	
	if len(x) == 0:
		print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
		print "\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><center><h1>Sorry.  No Records Found.</h1></center></font></td>"
		print "\t</tr>\n\t<tr>"
		print "\n</table>\n"
	
	else:	
		for g in x:	
			IID = str(g[1])
			while len(IID) < 8:
				IID = "0" + IID
			
			if str(g[0]) == "Set([\'I\'])":
				IID = "I" + IID
			elif str(g[0]) == "Set([\'S\'])":
				IID = "S" + IID
			else:
				IID = str(g[0]) + IID
			print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
			print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
			print "\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			if IID[0] =="I":
				print "\t\t<font color=\"#FFFFFF\"><h1>Item: %s</h1></font></td>"%(IID)
			else:
				print "\t\t<font color=\"#FFFFFF\"><h1>Service: %s</h1></font></td>"%(IID)
			print "\t</tr>\n\t<tr>"

			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			
			if IID[0] =="I":
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Item Information:</b></font></td>"
			else:
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Service Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
			print "\t\tItem ID:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(IID)
			print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(IID)
			print "<input type=\"hidden\" name=\"type\" value=\"B\">"
			
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tDescription:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print  "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(g[2])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tOwner:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print  "\t\t<textarea cols=30 rows =1>%s</textarea></td>"%(g[3])
				
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tCurrent Status:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	
			if str(g[4]) == "Set([\'Active\'])":
				print "\t\tActive</td>"
			elif str(g[4]) == "Set([\'Expired\'])":
				print "\t\tExpired</td>"
			elif str(g[4]) == "Set([\'Suspended\'])":
				print "\t\tSuspended</td>"
			elif str(g[4]) == "Set([\'Deleted\'])":
				print "\t\tDeleted</td>"
			else:
				print "\t\t%s</td>"%(str(g[4]))
			print "</tr><tr>"
    			print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
   		 	print "<select name=\"ht\">\n"
   		 	print "<option>Full<option>Half"
   		 	print "</select>\n"
  		  	print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
			print "</td>"
			print "\t</tr>\n</table>\n</form>\n<br>\n"
	
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
	print "</BODY>\n</HTML>"
	      ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                          