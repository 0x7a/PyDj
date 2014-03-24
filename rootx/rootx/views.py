from django.http import *
from django.template import Template,Context
from django.shortcuts import render_to_response
from django.template import RequestContext
import socket
import urllib
import base64
from xml.dom.minidom import parse, parseString
import urllib2

sites = []
def reverse(xx):
        sites[:] = []
        top = 50
        skip = 0
        account_key ="6XgKqcpSQqUPnODbSdOK9sOy30ng0ilUci99d5pol8I"
        ip = socket.gethostbyname(str(xx))
        while skip < 200:
            url = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Web?Query='ip:%s'&$top=%s&$skip=%s&$format=Atom"%(ip,top,skip)
            request = urllib2.Request(url)
            auth = base64.encodestring("%s:%s" % (account_key, account_key)).replace("\n", "")
            request.add_header("Authorization", "Basic %s" % auth)
            res = urllib2.urlopen(request)
            data = res.read()
            xmldoc = parseString(data)
            site_list = xmldoc.getElementsByTagName('d:Url')
            for site in site_list:
                domain = site.childNodes[0].nodeValue
                domain = domain.split("/")[2]
                if domain not in sites:
                    sites.append(domain)
            skip += 50
def reversex(request):
    if request.method=="POST":
        adi = request.POST.get('reverse')
        reverse(adi)
        ke = sites
        return render_to_response("index3.html",locals())

    else:
        return render_to_response('index3.html',context_instance = RequestContext(request))
