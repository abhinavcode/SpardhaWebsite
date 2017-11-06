# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

import MySQLdb
import random
import string
import smtplib
import base64
# Create your views here.

db = MySQLdb.connect("localhost","dbmsuser","password","dbmsproject" );

def send_mail(email,password,loginid):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("spardha.iit.bhu.varanasi@gmail.com", "spardhaiitbhu")
    message = "Your login id for spardha is %s and password is %s" %(loginid,password)
    s.sendmail("spardha.iit.bhu.varanasi@gmail.com", email, message)
    s.quit()



def getteam():
	q="select * from orgteam order by whichteam"
	c=db.cursor()
	c.execute(q)
	return c.fetchall()

def main_page(request):
	name=""	
	if "user" in request.session:
		q="select collegeName from colleges where id=%d" %(request.session["user"])
		cur=db.cursor()
		cur.execute(q)
		p=cur.fetchone()
		name=name+p[0]
	else:
		name="LOGIN"
	
	return render(request,'spardha/index.html',{"login":name})

def team(request):
	name=""	
	if "user" in request.session:
		q="select collegeName from colleges where id=%d" %(request.session["user"])
		cur=db.cursor()
		cur.execute(q)
		p=cur.fetchone()
		name=name+p[0]
	else:
		name="LOGIN"
	return render(request,'spardha/team.html',{"login":name,"ourteam":getteam()})

def getevents():
	q="select distinct(name),img from event"
	cur=db.cursor()
	cur.execute(q)
	p= cur.fetchall()
	print p
	return p

def events(request):
	name=""	
	if "user" in request.session:
		q="select collegeName from colleges where id=%d" %(request.session["user"])
		cur=db.cursor()
		cur.execute(q)
		p=cur.fetchone()
		name=name+p[0]
	else:
		name="LOGIN"
	return render(request,'spardha/events.html',{"login":name,"events":getevents()})




def addfix(team1,team2,eventname,eventfor,location,time,date):
	if team2:
		q="insert into fixture(team1,team2,eventname,event_for,location,time,date) values('%s','%s','%s','%s','%s','%s','%s')" %(team1,team2,eventname,eventfor,location,time,date)
		cur=db.cursor()
		cur.execute(q)
		db.commit()

	else:
		q="insert into fixture(team1,eventname,event_for,location,time,date) values('%s','%s','%s','%s','%s','%s')" %(team1,eventname,eventfor,location,time,date)
		cur=db.cursor()
		cur.execute(q)
		db.commit()



def getregcollegewithevents():
	q1="select name,for_sex from event"
	cur=db.cursor()
	cur.execute(q1)
	e=cur.fetchall()
	print e
	r=[]
	for i in e:
		q="select distinct(c.collegeName),c.id from event_reg er, colleges c, students s where s.regid=er.student_id and s.collegeid= c.id and er.event_name='%s' and er.event_for='%s'" %(i[0],i[1])
		print q		
		cur.execute(q)
		p=cur.fetchall()
		print i
		print p
		x=()
		for u,w in p:
			print "u and w"
			print u
			print w
			x=x+tuple([[u,int(w)]])
		r.append((i[0],i[1],x))
		print r
	print "out of loop"
	l=list(r)
	print l
	#l.pop(0)
	#print l
	
	x= tuple(l)
	print x
	return l

def getfixtures():
	q="select c.collegeName, d.collegeName, f.eventname, f.event_for, f.date,f.id from fixture f, colleges c,colleges d where f.team1=c.id and f.team2=d.id order by eventname, date"
	c=db.cursor()	
	c.execute(q)
	return c.fetchall()

def deletefixture(fid):
	q="delete from fixture where id= %d" %(fid)
	c=db.cursor()
	c.execute(q)

def fixturesandresult(request):
	error=""
	if request.POST.get("del"):
		deletefixture(int(request.POST.get("del")))
	if  request.POST.get("team1"):
		team1=request.POST.get("team1")
		team2=request.POST.get("team2")
		eventname=request.POST.get("eventname")
		eventfor=request.POST.get("sex")
		location=request.POST.get("location")
		time=request.POST.get("time")
		date=request.POST.get("date")

		if(team1==team2):
			error=error+"Wrong selection"
		else:
			addfix(team1,team2,eventname,eventfor,location,time,date)

	if "admin" in request.session:
		return render(request,'spardha/adminfixtures.html',{"events":getregcollegewithevents(),"error":error,"fixtures":getfixtures()})
	else:
		return render(request,'spardha/adminlogin.html',{"loginerror":"Login First"})


def addresult(fixtureid,winner):
	q="insert into result values(%d,%d)" %(fixtureid,winner)
	cur=db.cursor()
	cur.execute(q)
	db.commit()

def getresulteventwise():
	q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname, f.event_for, f.date,r.fixtureid from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner order by eventname, date"
	c=db.cursor()
	c.execute(q)
	return c.fetchall()

def getawaitedresult():
	q="select c.collegeName, d.collegeName, f.eventname, f.event_for, f.date,  c.id, d.id,f.id from fixture f, colleges c, colleges d where c.id=f.team1 and d.id=f.team2 and f.id not in (select fixtureid from result) order by eventname, date"	
	q1="select * from fixture"
	print q	
	c=db.cursor()
	c.execute(q)
	p= c.fetchall()
	print p
	return p

def deleteresult(val):
	q="delete from result where fixtureid= %d" %(val)
	c=db.cursor()
	c.execute(q)
	

def results(request):
	error=""
	if request.POST.get("del"):
		deleteresult(int(request.POST.get("del")))
	if request.POST.get("fixtureid"):
		addresult(int(request.POST.get("fixtureid")),int(request.POST.get("winner")))
	if "admin" in request.session:
		return render(request,'spardha/adminresults.html',{"events":getresulteventwise(),"awaitedresult":getawaitedresult()})
	else:
		return render(request,'spardha/adminlogin.html',{"loginerror":"Login First"})


def register(request):
	cur=db.cursor()
	query="SELECT collegeName, city from colleges"
	cur.execute(query)
	l=cur.fetchall()
	print l 	 
	x=[]	
	for i in l:
		p= i[0]+", "+i[1]
		x.append(p)
	print x
	return render(request,'spardha/reg.html',{"colleges":x})

def regconfirm(request):
	if request.POST.get('inlist',False):
		name=str(request.POST.get("name"))
		email=str(request.POST.get("email"))
		contact=int(request.POST.get("contact"))
		designation=str(request.POST.get("designation"))
		collegeName=str(request.POST.get("college1"))
		city=str(request.POST.get("city"))
		contingentsize=int(request.POST.get("contingentSize"))
		cur=db.cursor()
		query="insert into colleges(collegeName,name,designation,contact,email,city, contigentSize) values ( '%s' , '%s' , '%s' , %d , '%s' , '%s' , %d )" %(collegeName,name,designation,contact,email,city,contingentsize)
		print "query" + query
		cur.execute(query)
		db.commit()
	 	return render(request,'spardha/registration.html',{"msg":"Thank you for registering you will be mailed about your confirmation shortly"})
		
	else:
		collegeName=int(request.POST.get("college"))
		query = "select name, designation ,contact from colleges where id= %d" %(collegeName)
		print query		
		cur=db.cursor()
		cur.execute(query)
		l=cur.fetchall()
		
		s=""
		print l		
		for i in l:
			s="You are already registered. Please contact "+i[0].strip()+","+i[1]+"."
		
		return render(request,'spardha/registration.html',{"msg":s})
	
#		request.sessions["key"]=value;
	

def getAppandPending():
		q1="select collegeName,city,id,contigentSize from colleges where approved=0"
		cur=db.cursor()	
		cur.execute(q1)
		l1=cur.fetchall()

		q2="select collegeName,city,id,contigentSize from colleges where approved=1"		
		cur=db.cursor()	
		cur.execute(q2)
		ap=cur.fetchall()
		return 	{"pencolleges":l1,"appcolleges":ap}

def adminlogin(request):
	if ("admin" in request.session):
 		return HttpResponseRedirect('/admin1')  


	else:		
		return render(request,'spardha/adminlogin.html',{"loginerror":""})


	
def admin(request):
	if not ("admin" in request.session):
		userid=str(request.POST.get("userid"))
		password=str(request.POST.get("password"))
		
#		q1="select collegeName,city,id,contigentSize from colleges where approved=0"
#		cur=db.cursor()	
#		cur.execute(q1)
#		l1=cur.fetchall()
#		q2="select collegeName,city,id,contigentSize from colleges where approved=1"
		
#		cur=db.cursor()	
#		cur.execute(q2)
#		ap=cur.fetchall()
		query = "select * from admin where id= '%s' and password = '%s' " %(userid,password)
		cur=db.cursor()
		cur.execute(query)
		l=cur.fetchall()
		if(l):
			request.session	["admin"]=userid;
			return render(request,'spardha/admin.html',getAppandPending())
		else:
			return render(request,'spardha/adminlogin.html',{"loginerror":"User ID or Password may be incorrect."})

	
	update=(request.POST.getlist("collegepen"))
	if update:
		for i in update:
			print i
			i=int(i)
			q="update colleges set approved=1 where id= %d " %(i)
			cur=db.cursor()
			print q
			cur.execute(q)
			db.commit()
			q2="select email from colleges where id= %d" %(i)
			cur.execute(q2)
			x2=cur.fetchone()
			x=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
			send_mail(x2[0],x,i)
			print x2[0][0], x, i			
			q1="insert into collegelogin values( %d , '%s' )" %(i,x)
			cur.execute(q1)
			db.commit()
			
						
			
			
	return render(request,'spardha/admin.html',getAppandPending())		



def adminlogout(request):
	if  "admin" in request.session:
		del request.session["admin"]
#	return render(request,'spardha/index.html')
	print "admin logout"
 	return HttpResponseRedirect('/')  
	#return redirect("http://127.0.0.1:8000/")
	

def teamlogin(request):
	if ("user" in request.session):
 		return HttpResponseRedirect('/user')  

	else:		
		return render(request,'spardha/teamlogin.html',{"loginerror":""})
def getstudents(userid):
	q="select name,sex,year_of_study,contact,regid from students where collegeid= %d" %(userid)
	cur=db.cursor()
	cur.execute(q)
	p=cur.fetchall()
	return p
def collegename(user):
	q="select collegeName from colleges where id=%d" %(user)
	curr=db.cursor()
	curr.execute(q)
	o=curr.fetchone()
	collegename=o[0]
	return collegename

def deleterec(i):
	print "del called"
	q="delete from students where regid= %d" %(i)
	cur=db.cursor()
	cur=cur.execute(q)
	db.commit()

def addplayer(name,eventname,eventfor,iscaptain):
	q="insert into event_reg values( '%s', '%s', %d , %d )" %(eventname,eventfor,name,iscaptain)
	cur=db.cursor()
	cur=cur.execute(q)
	db.commit()
		

def getregstudentwithevents(userid):
	q1="select * from event"
	cur=db.cursor()
	cur.execute(q1)
	e=cur.fetchall()
	print e
	r=[]
	for i in e:
		q="select s.name from event_reg er, students s where s.regid=er.student_id and s.collegeid= %d and er.event_name='%s' and er.event_for='%s'" %(userid,i[0],i[1])
		print q		
		cur.execute(q)
		p=cur.fetchall()
		print i
		print p
		x=()
		for u in p:
			x=x+u
		r.append((i[0],i[1],x))
		print r
	print "out of loop"
	l=list(r)
	print l
	#l.pop(0)
	#print l
	
	x= tuple(l)
	print x
	return l
def allevents():
	q="select distinct(name) from event"
	cur=db.cursor()
	cur.execute(q)
	return cur.fetchall()	
	
def usergames(request):
	error=""	
	if request.POST.get("studentid"):
		x=0
		if (request.POST.get("iscaptain")):
			x=x+1
		name=int(request.POST.get("studentid"))
		eventname=str(request.POST.get("eventname"))
		q="select sex from students where regid= %d " %(name)
		cur=db.cursor()
		cur.execute(q)
		p=cur.fetchone()		
		q1="select for_sex from event where name='%s' " %(eventname)
		cur.execute(q1)
		p1=cur.fetchall()
		print p[0]
		print len(p1)
		q2="select * from event_reg where student_id= %d and event_name='%s'" %(name,eventname)
		cur.execute(q2)
		p2=cur.fetchall()		
		if p[0]=='F' and len(p1)==1:
			
			error=error+"Not valid selection."
		elif len(p2)!=0:
			error=error+"Player already added in this game."
		else:
			addplayer(int(request.POST.get("studentid")),str(request.POST.get("eventname")),str(p[0]),x)
	if "user" in request.session:
		userid=request.session["user"]
		return render(request,'spardha/usergames.html',{"events": getregstudentwithevents(userid),"collegename":collegename(userid),"students": getstudents(userid),"allevents":allevents(),"errorform":error})
#		return render(request,'spardha/usergames.html',{"collegename":collegename(userid)})
	else:	
 		return HttpResponseRedirect('/teamlogin')  

def user(request):
	error=""
	if request.POST.get("del"):
		print "function will be called"
		deleterec(int(request.POST.get("del")))
	if request.POST.get("name"):	
		cou="select contigentSize from colleges where id= %d" %(request.session["user"])
		print cou
		cur=db.cursor()
		cur.execute(cou)
		p=cur.fetchone()
		print p[0]		
		x="select count(*) from students where collegeid= %d" %(request.session["user"])
		cur.execute(x)
		o=cur.fetchone()
		print o[0]
		if p[0]>o[0]:
			name=str(request.POST.get("name"))
			sex=str(request.POST.get("sex"))
			number=int(request.POST.get("contact"))
			year=int(request.POST.get("year"))
			q="insert into students(name,sex,year_of_study,contact,collegeid) values('%s','%s',%d,%d,%d)" %(name,sex,year,number,request.session["user"])
			cur=db.cursor()
			cur.execute(q)
			db.commit()
		else:
			error=error+"You have already added all the students."

	if not ("user" in request.session):
		userid=int(request.POST.get("userid"))
		password=str(request.POST.get("password"))
		query = "select * from collegelogin where id= %d and password = '%s' " %(userid,password)
		cur=db.cursor()
		cur.execute(query)
		l=cur.fetchall()
		
		if(l):
			request.session	["user"]=userid;
			
			return render(request,'spardha/user.html',{"students": getstudents(userid),"error":error,"collegename":collegename(userid)})
		else:
			return render(request,'spardha/teamlogin.html',{"loginerror":"User ID or Password may be incorrect."})

	else:
		return render(request,'spardha/user.html',{"students": getstudents(request.session["user"]),"error":error,"collegename":collegename(request.session["user"]	)})
	


	

def userlogout(request):
	if  "user" in request.session:
		del request.session["user"]
#	return render(request,'spardha/index.html')
	print "user logout"
 	return HttpResponseRedirect('/')  
	#return redirect("http://127.0.0.1:8000/")


def teamreq():
		q="select name from teams"
		cur=db.cursor()
		cur.execute(q)
		l=cur.fetchall()
		x=[]
		if l:
			for i in l:
				x.append(i[0])
 
		return x
def inspost(post):
	q="insert into teams values( '%s' )" %(post)
	cur=db.cursor()
	print q
	cur.execute(q)
	db.commit()

def addteammember():
	#img=request.POST.get("pic")
	#name=request.POST.get("name")
	#contact=request.POST.get("contact")
	#post=request.POST.get("posts")
	#team=request.POST.get("team")
	#image=open(str(img),'rb')
	q="insert into orgteam values (%d,'%s','%s','%s','%s')" %(int(contact),str(name),str(post),str(team),image)
	cur=db.cursor()
	cur.execute(q)
	db.commit()


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo



def ourteam(request):
	if "admin" in request.session:	
		
		print "ourteam"	

		if (request.POST.get("post")):
			#print str(post)		
			inspost(str((request.POST.get("post"))))
		if request.POST.get("posts"):
			img=request.FILES["pic"]
			x=img.read()
			imgenc=base64.encodestring(x)
			name=request.POST.get("name")
			contact=request.POST.get("contact")
			posts=request.POST.get("posts")
			team=request.POST.get("team")
			print type(img)
			#image=open((img),'rb')
			q="insert into orgteam values (%d,'%s','%s','%s','%s')" %(int(contact),str(name),str(posts),str(team),imgenc)
			cur=db.cursor()
			cur.execute(q)
			db.commit()

	#		addteammember()				
		return render(request,'spardha/adminteam.html',{"teams":teamreq(),"ourteam":getteam()})
				
								
	else:
		return HttpResponseRedirect('/adminlogin')  

def getmaleevents():
	q="select name,img from event where for_sex='M' order by name"
	cur=db.cursor()
	cur.execute(q)
	return cur.fetchall()

def getfemaleevents():
	q="select name,img from event where for_sex='F' order by name"
	cur=db.cursor()
	cur.execute(q)
	return cur.fetchall()

def addevent(name,for_sex,imgEnc):
	print "add event"
	q="insert into event values('%s','%s','%s')"%(name,for_sex,imgEnc)
	print q	
	cur=db.cursor()
	cur.execute(q)
	db.commit()

def adminevents(request):

		
	if  request.POST.get("eventname"):
		eventfor=str(request.POST.get("eventfor"))
		x=request.FILES["pic"]
		img=x.read()
		imgEnc=base64.encodestring(img)

		if eventfor=="Both":
			addevent(str(request.POST.get("eventname")),"F",imgEnc)
			addevent(str(request.POST.get("eventname")),"M",imgEnc)
		else:
			addevent(str(request.POST.get("eventname")),eventfor,imgEnc)
			
	if "admin" in request.session:	
		return render(request,'spardha/adminevents.html',{"teams":teamreq(),"male":getmaleevents(),"female":getfemaleevents()})
	else:
		return HttpResponseRedirect('/adminlogin')  


def getcaptains(userid):
	q="select s.name, s.contact, er.event_name,er.event_for from students s , event_reg er where er.student_id =s.regid and er.isCaptain=1 and s.collegeid=%d" %(userid)
	c=db.cursor()
	c.execute(q)
	return c.fetchall()

def collegedesc(request,num=1):
	print num
	if "admin" in request.session:
		return render(request,'spardha/collegedesc.html',{"events": getregstudentwithevents(int(num)),"collegename":collegename(int(num)),"captains":getcaptains(int(num))})
	
	else:
		return HttpResponseRedirect('/adminlogin',)  


