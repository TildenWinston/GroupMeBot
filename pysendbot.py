from urllib import request, parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging




def input ():

    botid = ""
    text = ""

    data = parse.urlencode({'bot_id': botid, 'text': text}).encode()
    req =  request.Request("https://api.groupme.com/v3/bots/post?", data=data) # this will make the method "POST"
    resp = request.urlopen(req)
    print("past the post attempt")
    print (data)



input()
