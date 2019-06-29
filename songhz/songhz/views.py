# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from network.models import Host,Ip
from toolbox.ansible_api import MyRunner
from toolbox.tool import Network
import json


# Create your views here.


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'hello.html', context)

def test(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'index.html', context)
def table(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'tables.html', context)

def calendar(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'calendar.html', context)

def buttons(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'buttons.html', context)

def interface(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'interface.html', context)

def editors(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'editors.html', context)

def stats(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'stats.html', context)

def form(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'form.html', context)

def home(request):
    context = {}
    ansible = MyRunner('config/hosts')
    ansible.run('all', 'shell', "hostname")
    # 结果
    result = ansible.get_result()

    #print json.dumps(result,indent=4)
    hostlist=[]
    print(type(result))
    print result['success'].keys()
    for host in result['success'].keys():
        res = result['success'][host]['stdout']
        hostlist.append((host,res))
        isexist = Host.objects.filter(ip=host)
        if(len(isexist)>=1):
            continue
        test1 = Host(hostname=res, ip=host)
        test1.save()

    #print(a)
    context['result'] = hostlist
    return render(request, 'hello.html', context)

def gethost(request):
    context = {}
    hostlist = Host.objects.all()
    host_list = []
    for host in hostlist:
        host_list.append((host.hostname,host.ip))
    context['result'] = json.dumps(host_list)
    return render(request, 'hello.html', context)

def getip(request):
    context = {}
    hostlist = Ip.objects.all()
    host_list = []
    for host in hostlist:
        host_list.append((host.ip,host.status,host.comment))
    context['result'] = json.dumps(host_list)
    return render(request, 'hello.html', context)
#扫描可用IP
def scan(request):
    context= {}
    net = "192.168.31.0/24"
    network = Network(net);
    hosts_up_list = network.get_hosts_up()
    for host in hosts_up_list:
        isexist = Ip.objects.filter(ip=host)
        if(len(isexist)>0):
            if  isexist[0].status=='used':
                continue
            else:
                Ip.objects.filter(ip=host).update(status='used')

def form(request):
    context          = {}
    context['hello'] = 'Hello World!aaaa'
    return render(request, 'form.html', context)

def home(request):
    context = {}
    ansible = MyRunner('config/hosts')
    ansible.run('all', 'shell', "hostname")
    # 结果
    result = ansible.get_result()

    #print json.dumps(result,indent=4)
    hostlist=[]
    #print result['success'].keys()
    for host in result['success'].keys():
        res = result['success'][host]['stdout']
        hostlist.append((host,res))
        isexist = Host.objects.filter(ip=host)
        if(len(isexist)>=1):
            continue
        test1 = Host(hostname=res, ip=host)
        test1.save()

    #print(a)
    context['result'] = hostlist
    return render(request, 'hello.html', context)

def gethost(request):
    context = {}
    hostlist = Host.objects.all()
    host_list = []
    for host in hostlist:
        host_list.append((host.hostname,host.ip))
    context['result'] = json.dumps(host_list)
    return render(request, 'hello.html', context)

def getip(request):
    context = {}
    hostlist = Ip.objects.all()
    host_list = []
    for host in hostlist:
        host_list.append((host.ip,host.status,host.comment))
    context['result'] = json.dumps(host_list)
    return render(request, 'hello.html', context)
#扫描可用IP
def scan(request):
    context= {}
    net = "10.1.1.0/24"
    network = Network(net);
    hosts_up_list = network.get_hosts_up()
    for host in hosts_up_list:
        isexist = Ip.objects.filter(ip=host)
        if(len(isexist)>0):
            if  isexist[0].status=='used':
                continue
            else:
                Ip.objects.filter(ip=host).update(status='used')
        ip = Ip(ip=host,status='used',comment='nothing')
        ip.save()
    update_ip()
    context['hello']=hosts_up_list
    context['ssh_hosts']=network.get_hosts_ssh()
    return render(request, 'hello.html', context)
#更新数据库
def update_ip():
    host_list = Host.objects.all()
    for host in host_list:
        is_record = Ip.objects.filter(ip=host.ip)
        if (len(is_record) > 0):
            comment = host.hostname
            Ip.objects.filter(ip=host.ip).update(status='used',comment=comment)
    pass

def index(request):
    context  = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)
