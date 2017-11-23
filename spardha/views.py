# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.db import connection
import json
from django.http import HttpResponse
from django.core import serializers
import MySQLdb
import random
import string
import smtplib
import base64
import hashlib
# Create your views here.

host="abhinavcode.mysql.pythonanywhere-services.com"
user="abhinavcode"
passwd="abc123abc"
d="abhinavcode$spardha"

def send_mail(email,password,loginid):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("spardha.iit.bhu.varanasi@gmail.com", "spardhaiitbhu")
    message = "Your login id for spardha is %s and password is %s" %(loginid,password)
    s.sendmail("spardha.iit.bhu.varanasi@gmail.com", email, message)
    s.quit()



def getteam():
   # db=MySQLdb.connect(host,user,passwd,d)
    q="select * from orgteam order by whichteam"
    c=connection.cursor()
    c.execute(q)
    x=c.fetchall()
    c.close()
    return x

def main_page(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    name=""
    if "user" in request.session:
        q="select collegeName from colleges where id=%d" %(request.session["user"])
        cur=connection.cursor()
        cur.execute(q)
        p=cur.fetchone()
        cur.close()
        name=name+p[0]
    else:
        name="LOGIN"
    #db.close()

    return render(request,'spardha/index.html',{"login":name})

def team(request):
#    db=MySQLdb.connect(host,user,passwd,d)
    name=""
    if "user" in request.session:
        q="select collegeName from colleges where id=%d" %(request.session["user"])
        cur=connection.cursor()
        cur.execute(q)
        p=cur.fetchone()
        cur.close()
        name=name+p[0]
    else:
        name="LOGIN"
#    db.close()
    return render(request,'spardha/team.html',{"login":name,"ourteam":getteam()})

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError(
            "Unserializable object {} of type {}".format(obj, type(obj))
        )

def badsc(request):
 #   db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Badminton' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def badres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Badminton' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def cricsc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Cricket' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def cricres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Cricket' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def footballsc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Football' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def footballres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Football' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")


def athleticssc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Athletics' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def athleticsres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Athletics' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")



def volleyballsc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Volleyball' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def volleyballres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Volleyball' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")



def chesssc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Chess' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def chessres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Chess' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")



def basketballsc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Basketball' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def basketballres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Basketball' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")




def handballsc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Handball' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def handballres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Handball' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")


def hockeysc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Hockey' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def hockeyres(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Hockey' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")


def khokhosc(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName,d.collegeName,f.location,f.date,f.time from fixture f, colleges c, colleges d where eventname='Kho Kho' and c.id=f.team1 and d.id=f.team2"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        f='{ "eventname":"", "team1":"%s","team2":"%s","location":"%s","date":"%s","time":"%s"}' %(x[0],x[1],x[2],x[3],x[4])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
    #db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")

def khokhores(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname,f.event_for, f.date from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner and f.eventname='Kho Kho' order by date"
    c=connection.cursor()
    c.execute(q)
    p=c.fetchall()
    s=""
    for x in p:
        l=x[3]+", "+x[4]+", "+str(x[5])
        f='{ "eventname":"%s", "team1":"%s","team2":"%s","winner":"%s"}' %(l,x[0],x[1],x[2])
        s=s+f+","
    v="["+s[:-1]+"]"
	#o=tuple(v)
	#json_data=json.dumps(o)
#    db.close()
    c.close()
    return HttpResponse(v, content_type="application/json")




def getevents():
 #   db=MySQLdb.connect(host,user,passwd,d)

    q="select distinct(name),img,contact from event"
    cur=connection.cursor()
    cur.execute(q)
    p= cur.fetchall()
#    db.close()
    cur.close()
    return p

def events(request):
 #   db=MySQLdb.connect(host,user,passwd,d)
    name=""
    if "user" in request.session:
        q="select collegeName from colleges where id=%d" %(request.session["user"])
        cur=connection.cursor()
        cur.execute(q)
        p=cur.fetchone()
        cur.close()
        name=name+p[0]
    else:
        name="LOGIN"
#    db.close()
    return render(request,'spardha/events.html',{"login":name,"events":getevents()})




def addfix(team1,team2,eventname,eventfor,location,time,date):
  #  db=MySQLdb.connect(host,user,passwd,d)
    if team2:
        q="insert into fixture(team1,team2,eventname,event_for,location,time,date) values('%s','%s','%s','%s','%s','%s','%s')" %(team1,team2,eventname,eventfor,location,time,date)
        cur=connection.cursor()
        cur.execute(q)
        connection.commit()
        cur.close()
    else:
	    q="insert into fixture(team1,eventname,event_for,location,time,date) values('%s','%s','%s','%s','%s','%s')" %(team1,eventname,eventfor,location,time,date)
	    cur=connection.cursor()
	    cur.execute(q)
	    connection.commit()
	    cur.close()
#    db.close()


def getregcollegewithevents():
  #  db=MySQLdb.connect(host,user,passwd,d)
    q1="select name,for_sex from event"
    cur=connection.cursor()
    cur.execute(q1)
    e=cur.fetchall()
    r=[]
    for i in e:
        q="select distinct(c.collegeName),c.id from event_reg er, colleges c, students s where s.regid=er.student_id and s.collegeid= c.id and er.event_name='%s' and er.event_for='%s'" %(i[0],i[1])
        cur.execute(q)
        p=cur.fetchall()
        x=()
        for u,w in p:
            x=x+tuple([[u,int(w)]])
        r.append((i[0],i[1],x))
    l=list(r)
	#l.pop(0)
	#print l
    x= tuple(l)
 #   db.close()
    cur.close()
    return l

def getfixtures():
#    db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName, d.collegeName, f.eventname, f.event_for, f.date,f.id from fixture f, colleges c,colleges d where f.team1=c.id and f.team2=d.id order by eventname, date"
    c=connection.cursor()
    c.execute(q)
    #db.close()
    x=c.fetchall()
    c.close()
    return x

def deletefixture(fid):
#    db=MySQLdb.connect(host,user,passwd,d)
    q="delete from fixture where id= %d" %(fid)
    c=connection.cursor()
    c.execute(q)
 #   db.close()
    c.close()

def fixturesandresult(request):
    #db=MySQLdb.connect(host,user,passwd,d)
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
    d#b.close()


def addresult(fixtureid,winner):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="insert into result values(%d,%d)" %(fixtureid,winner)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()

    cur.close()
#    db.close()

def getresulteventwise():
  #  db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName  , d.collegeName  , e.collegeName, f.eventname, f.event_for, f.date,r.fixtureid from fixture f, result r, colleges c, colleges d, colleges e where f.id=r.fixtureid and c.id=f.team1 and d.id=f.team2 and e.id=r.winner order by eventname, date"
    c=connection.cursor()
    c.execute(q)

 #   db.close()

    x= c.fetchall()
    c.close()
    return x

def getawaitedresult():
#    db=MySQLdb.connect(host,user,passwd,d)
    q="select c.collegeName, d.collegeName, f.eventname, f.event_for, f.date,  c.id, d.id,f.id from fixture f, colleges c, colleges d where c.id=f.team1 and d.id=f.team2 and f.id not in (select fixtureid from result) order by eventname, date"
    c=connection.cursor()
    c.execute(q)
    p= c.fetchall()

    c.close()
    #db.close()

    return p

def deleteresult(val):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="delete from result where fixtureid= %d" %(val)
    c=connection.cursor()
    c.execute(q)

    c.close()
    #db.close()


def results(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if request.POST.get("del"):
    	deleteresult(int(request.POST.get("del")))
    if request.POST.get("fixtureid"):
    	addresult(int(request.POST.get("fixtureid")),int(request.POST.get("winner")))
    if "admin" in request.session:
    	return render(request,'spardha/adminresults.html',{"events":getresulteventwise(),"awaitedresult":getawaitedresult()})
    else:
    	return render(request,'spardha/adminlogin.html',{"loginerror":"Login First"})
    #db.close()


def register(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    cur=connection.cursor()
    query="SELECT collegeName, city from colleges"
    cur.execute(query)
    l=cur.fetchall()

    cur.close()
    #db.close()

    x=[]
    for i in l:
    	p= i[0]+", "+i[1]
    	x.append(p)
    return render(request,'spardha/reg.html',{"colleges":x})

def regconfirm(request):
    s=""

    #db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if request.POST.get('inlist',False):
        name=str(request.POST.get("name"))
        email=str(request.POST.get("email"))
        contact=int(request.POST.get("contact"))

        designation=str(request.POST.get("designation"))
        collegeName=str(request.POST.get("college1"))
        city=str(request.POST.get("city"))
        contingentsize=int(request.POST.get("contingentSize"))

        cur=connection.cursor()
        query="insert into colleges(collegeName,name,designation,contact,email,city, contigentSize) values ( '%s' , '%s' , '%s' , %d , '%s' , '%s' , %d )" %(collegeName,name,designation,contact,email,city,contingentsize)
        cur.execute(query)
        connection.commit()
        cur.close()
        return render(request,'spardha/registration.html',{"msg":"Thank you for registering you will be mailed about your confirmation shortly"})
    else:
	    collegeName=int(request.POST.get("college"))
	    query = "select name, designation ,contact from colleges where id= %d" %(collegeName)
	    cur=connection.cursor()
	    cur.execute(query)
	    l=cur.fetchall()
	    cur.close()
	    for i in l:
	        s="You are already registered. Please contact "+i[0].strip()+","+i[1]+"."

#    db.close()

    return render(request,'spardha/registration.html',{"msg":s})

#		request.sessions["key"]=value;


def getAppandPending():
#        db=MySQLdb.connect(host,user,passwd,d)

        q1="select collegeName,city,id,contigentSize from colleges where approved=0"
        cur=connection.cursor()
        cur.execute(q1)
        l1=cur.fetchall()
        cur.close()
        q2="select collegeName,city,id,contigentSize from colleges where approved=1"
        cur=connection.cursor()
        cur.execute(q2)
        ap=cur.fetchall()

        cur.close()
#        db.close()

        return 	{"pencolleges":l1,"appcolleges":ap}

def adminlogin(request):
	if ("admin" in request.session):
	    return HttpResponseRedirect('/admin1')
	else:
	    return render(request,'spardha/adminlogin.html',{"loginerror":""})



def admin(request):
 #   db=MySQLdb.connect(host,user,passwd,d)
    if not ("admin" in request.session):
        userid=str(request.POST.get("userid"))
        password=str(request.POST.get("password"))
        password=hashlib.sha256(password).hexdigest()

#		q1="select collegeName,city,id,contigentSize from colleges where approved=0"
#		cur=db.cursor()
#		cur.execute(q1)
#		l1=cur.fetchall()
#		q2="select collegeName,city,id,contigentSize from colleges where approved=1"

#		cur=db.cursor()
#		cur.execute(q2)
#		ap=cur.fetchall()
        query = "select * from admin where id= '%s' and password = '%s' " %(userid,password)
        cur=connection.cursor()
        cur.execute(query)
        l=cur.fetchall()
        cur.close()
        if(l):
            request.session["admin"]=userid;
            return render(request,'spardha/admin.html',getAppandPending())
        else:
            return render(request,'spardha/adminlogin.html',{"loginerror":"User ID or Password may be incorrect."})

    update=(request.POST.getlist("collegepen"))
    if update:
        for i in update:
            i=int(i)
            q="update colleges set approved=1 where id= %d " %(i)
            cur=connection.cursor()
            cur.execute(q)
            connection.commit()
            q2="select email from colleges where id= %d" %(i)
            cur.execute(q2)
            x2=cur.fetchone()
            x=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            send_mail(x2[0],x,i)
            x=hashlib.sha256(x).hexdigest()
            q1="insert into collegelogin values( %d , '%s' )" %(i,x)
            cur.execute(q1)
            connection.commit()
            cur.close()

   # db.close()

    return render(request,'spardha/admin.html',getAppandPending())



def adminlogout(request):
   # db=MySQLdb.connect(host,user,passwd,d)
    if  "admin" in request.session:
        del request.session["admin"]
#	return render(request,'spardha/index.html')
   # db.close()

    return HttpResponseRedirect('/')
	#return redirect("http://127.0.0.1:8000/")


def teamlogin(request):

    if ("user" in request.session):
        return HttpResponseRedirect('/user')
    else:
        return render(request,'spardha/teamlogin.html',{"loginerror":""})
def getstudents(userid):
   # db=MySQLdb.connect(host,user,passwd,d)
    q="select name,sex,year_of_study,contact,regid from students where collegeid= %d" %(userid)
    cur=connection.cursor()
    cur.execute(q)
    p=cur.fetchall()
    cur.close()
    #db.close()
    return p
def collegename(u):
    #db=MySQLdb.connect(host,user,passwd,d)
    q="select collegeName from colleges where id=%d" %(u)
    curr=connection.cursor()
    curr.execute(q)
    o=curr.fetchone()
    collegename=o[0]
    curr.close()
   # db.close()
    return collegename

def deleterec(i):
   # db=MySQLdb.connect(host,user,passwd,d)
    q="delete from students where regid= %d" %(i)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()
    cur.close()
    #db.close()



def addplayer(name,eventname,eventfor,iscaptain):
    #db=MySQLdb.connect(host,user,passwd,d)
    q='insert into event_reg values( "%s", "%s", %d , %d )' %(eventname,eventfor,name,iscaptain)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()
    cur.close()
    #db.close()


def getregstudentwithevents(userid):
    #db=MySQLdb.connect(host,user,passwd,d)
    q1="select * from event"
    cur=connection.cursor()
    cur.execute(q1)
    e=cur.fetchall()
    r=[]
    for i in e:
        q="select s.name from event_reg er, students s where s.regid=er.student_id and s.collegeid= %d and er.event_name='%s' and er.event_for='%s'" %(userid,i[0],i[1])
        cur.execute(q)
        p=cur.fetchall()
        x=()
        for u in p:
            x=x+u
        if(len(x)!=0):
            r.append((i[0],i[1],x))
    l=list(r)
	#l.pop(0)
	#print l
    x= tuple(l)
    cur.close()
   # db.close()

    return l
def allevents():
   # db=MySQLdb.connect(host,user,passwd,d)
    q="select distinct(name) from event"
    cur=connection.cursor()
    cur.execute(q)
    #db.close()

    x= cur.fetchall()
    cur.close()
    return x

def usergames(request):
   # db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if request.POST.get("studentid"):
        x=0
        if (request.POST.get("iscaptain")):
            x=x+1
        name=int(request.POST.get("studentid"))
        eventname=str(request.POST.get("eventname"))
        q="select sex from students where regid= %d " %(name)
        cur=connection.cursor()
        cur.execute(q)
        p=cur.fetchone()
        q1="select for_sex from event where name='%s' " %(eventname)
        cur.execute(q1)
        p1=cur.fetchall()
        q2="select * from event_reg where student_id= %d and event_name='%s'" %(name,eventname)
        cur.execute(q2)
        p2=cur.fetchall()
        cur.close()
        if p[0]=='F' and len(p1)==1:
            error=error+"Not valid selection."
        elif len(p2)!=0:
            error=error+"Player already added in this game."
        else:
            addplayer(int(request.POST.get("studentid")),str(request.POST.get("eventname")),str(p[0]),x)
  #  db.close()

    if "user" in request.session:
        userid=request.session["user"]
        return render(request,'spardha/usergames.html',{"events": getregstudentwithevents(userid),"collegename":collegename(userid),"students": getstudents(userid),"allevents":allevents(),"errorform":error})
#		return render(request,'spardha/usergames.html',{"collegename":collegename(userid)})
    else:
        return HttpResponseRedirect('/teamlogin')

def user1(request):
    #db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if request.POST.get("del"):
        deleterec(int(request.POST.get("del")))
    if request.POST.get("name"):
        cou="select contigentSize from colleges where id= %d" %(request.session["user"])
        cur=connection.cursor()
        cur.execute(cou)
        p=cur.fetchone()
        x="select count(*) from students where collegeid= %d" %(request.session["user"])
        cur.execute(x)
        o=cur.fetchone()
        cur.close()
        if p[0]>o[0]:
            name=str(request.POST.get("name"))
            sex=str(request.POST.get("sex"))
            contact=request.POST.get("contact")
            year=int(request.POST.get("year"))

            if not ((contact).isdigit() and len(str(contact))==10):
                    error=error+"Enter correct number"
            else:
                number=int(request.POST.get("contact"))
                q="insert into students(name,sex,year_of_study,contact,collegeid) values('%s','%s',%d,%d,%d)" %(name,sex,year,number,request.session["user"])
                cur=connection.cursor()
                cur.execute(q)
                connection.commit()
                cur.close()
        else:
            error=error+"You have already added all the students."

    if not ("user" in request.session):
        userid=(request.POST.get("userid"))
        if not ((userid).isdigit()):
            return render(request,'spardha/teamlogin.html',{"loginerror":"User ID or Password may be incorrect."})
        userid=int(userid)
        password=str(request.POST.get("password"))
        password=hashlib.sha256(password).hexdigest()
        query = "select * from collegelogin where id= %d and password = '%s' " %(userid,password)
        cur=connection.cursor()
        cur.execute(query)
        l=cur.fetchall()
        cur.close()
       # db.close()

        if(l):
            request.session	["user"]=userid;
            return render(request,'spardha/user.html',{"students": getstudents(userid),"error":error,"collegename":collegename(userid)})
        else:
            return render(request,'spardha/teamlogin.html',{"loginerror":"User ID or Password may be incorrect."})
    else:
        #db.close()

        return render(request,'spardha/user.html',{"students": getstudents(request.session["user"]),"error":error,"collegename":collegename(request.session["user"]	)})





def userlogout(request):


    if  "user" in request.session:
        del request.session["user"]
#	return render(request,'spardha/index.html')
    return HttpResponseRedirect('/')
	#return redirect("http://127.0.0.1:8000/")


def teamreq():
       # db=MySQLdb.connect(host,user,passwd,d)
        q="select name from teams"
        cur=connection.cursor()
        cur.execute(q)
        l=cur.fetchall()
        x=[]
        if l:
            for i in l:
                x.append(i[0])
        cur.close()
       # db.close()
        return x
def inspost(post):
   # db=MySQLdb.connect(host,user,passwd,d)
    q="insert into teams values( '%s' )" %(post)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()
    cur.close()
   # db.close()

def addteammember():
	#img=request.POST.get("pic")
	#name=request.POST.get("name")
	#contact=request.POST.get("contact")
	#post=request.POST.get("posts")
	#team=request.POST.get("team")
	#image=open(str(img),'rb')
    #db=MySQLdb.connect(host,user,passwd,d)
    q="insert into orgteam values (%d,'%s','%s','%s','%s')" %(int(contact),str(name),str(post),str(team),image)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()
    cur.close()
   # db.close()


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo



def ourteam(request):
   # db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if "admin" in request.session:
        if (request.POST.get("post")):
            inspost(str((request.POST.get("post"))))
        if request.POST.get("posts"):
            img=request.FILES["pic"]
            x=img.read()
            imgenc=base64.encodestring(x)
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            if not ((contact).isdigit() and len(str(contact))==10):
                error=error+"Enter correct number"
            else:
                posts=request.POST.get("posts")
                team=request.POST.get("team")
                q="insert into orgteam values (%d,'%s','%s','%s','%s')" %(int(contact),str(name),str(posts),str(team),imgenc)
                cur=connection.cursor()
                cur.execute(q)
                connection.commit()
                cur.close()
           # db.close()

	#		addteammember()
        return render(request,'spardha/adminteam.html',{"teams":teamreq(),"ourteam":getteam(),"error":error})
    else:
#        db.close()
        return HttpResponseRedirect('/adminlogin')

def getmaleevents():
   # db=MySQLdb.connect(host,user,passwd,d)
    q="select name,img from event where for_sex='M' order by name"
    cur=connection.cursor()
    cur.execute(q)
    x= cur.fetchall()
    cur.close()
    return x

def getfemaleevents():
 #   db=MySQLdb.connect(host,user,passwd,d)
    q="select name,img from event where for_sex='F' order by name"
    cur=connection.cursor()
    cur.execute(q)
 #   db.close()

    x= cur.fetchall()
    cur.close()
    return x

def addevent(name,for_sex,imgEnc,con):
  #  db=MySQLdb.connect(host,user,passwd,d)
    q="insert into event values('%s','%s','%s',%d)"%(name,for_sex,imgEnc,con)
    cur=connection.cursor()
    cur.execute(q)
    connection.commit()
    cur.close()
   # db.close()

def adminevents(request):
   # db=MySQLdb.connect(host,user,passwd,d)
    error=""
    if  request.POST.get("eventname"):
        contact=(request.POST.get("contact"))
        if not ((contact).isdigit() and len(str(contact))==10):
                error="Enter correct number"
        else:
            eventfor=str(request.POST.get("eventfor"))
            x=request.FILES["pic"]
            img=x.read()
            imgEnc=base64.encodestring(img)
            if eventfor=="Both":
                addevent(str(request.POST.get("eventname")),"F",imgEnc,int(request.POST.get("contact")))
                addevent(str(request.POST.get("eventname")),"M",imgEnc,int(request.POST.get("contact")))
            else:
                addevent(str(request.POST.get("eventname")),eventfor,imgEnc,int(request.POST.get("contact")))
    #db.close()

    if "admin" in request.session:
        return render(request,'spardha/adminevents.html',{"teams":teamreq(),"male":getmaleevents(),"female":getfemaleevents(),"error":error})
    else:
        return HttpResponseRedirect('/adminlogin')


def getcaptains(userid):
   # db=MySQLdb.connect(host,user,passwd,d)
    q="select s.name, s.contact, er.event_name,er.event_for from students s , event_reg er where er.student_id =s.regid and er.isCaptain=1 and s.collegeid=%d" %(userid)
    c=connection.cursor()
    c.execute(q)
   # db.close()
    x= c.fetchall()
    c.close()
    return x

def collegedesc(request,num=1):
    if "admin" in request.session:
        return render(request,'spardha/collegedesc.html',{"events": getregstudentwithevents(int(num)),"collegename":collegename(int(num)),"captains":getcaptains(int(num))})
    else:
        return HttpResponseRedirect('/adminlogin',)


