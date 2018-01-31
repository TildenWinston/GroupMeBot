# from urllib import request, parse
import urllib
import re
# import os
from http.server import BaseHTTPRequestHandler, HTTPServer


# POST request does not want to work in browser. Works fine on desktop.
# Currently dictionaries are getting muddled and layered.
# Sample JSON:
# {"attachments":[],"avatar_url":"https://i.groupme.com/306x310.jpeg.6b5f401f889a4e86a4b19d0ebc9aa8df","created_at":1516143471,"group_id":"37357804","id":"151614347176916995","name":"bot1test","sender_id":"576261","sender_type":"bot","source_guid":"9aa21970dd3e0135606e22000b2304c6","system":false,"text":"{\"attachments\":[],\"avatar_url\":\"https://i.groupme.com/2002x3000.jpeg.1580176b8b064345bae61459d322dc05\",\"created_at\":1516143471,\"group_id\":\"37357804\",\"id\":\"151614347107242869\",\"name\":\"Tilden Winston\",\"sender_id\":\"38756513\",\"sender_type\":\"user\",\"source_guid\":\"90d48c63-a89c-4aaf-9f8d-9daedf4f7766\",\"system\":false,\"text\":\"test\",\"user_id\":\"38756513\"}","user_id":"576261"}


def handler(event, context):
    #Base States:
    botid = ""

    # botid = os.environ['botid']
    botname = ""
    # botname = os.environ['botname']
    # print((type(botname))
    # print(botname)
    # botname = str(botname)
    # print((type(botname))

    trigger1 = 0
    trigger2 = 0
    findingstotal = 0
    responsetext = "error"
    #responsetext1 = "trigger1 is good."
    responsetext1 = ""
    trigger2text = ""

    print(type(event))
    events = event
    print(str(events))
    groupmejson = events['body']
    print(type(groupmejson))
    print(str(groupmejson))
    print(type(groupmejson))
    # groupmejson = dict(groupmejson)

    #Name finding regex: (?<=(name\": \")).*?(?=(\",\"sender_id\": \"\d{8}))
    try:
        nameregex = re.compile(r"((?<=(name\":\")).*?(?=(\",\"sender_id\":\"\d)))") #(r"((?<=(name\": \")).*?(?=(\",\"sender_id\": \"\d{8})))")
        print(nameregex)
        names = []
        names = nameregex.findall(groupmejson)
        print(names[0])
        name = names[0][0]

    except:
        nameregex = re.compile(r"((?<=(name\': \')).*?(?=(\', \'sender_id\': \'\d{8})))")
        print(nameregex)
        names = []
        names = nameregex.findall(groupmejson)
        print(names)
        name = names[0][0]

    # We don't want to reply to ourselves!
    if name != botname:
        stuff = event
        # print(str(stuff))

        try:
            searchtext = groupmejson.lower()
            print(searchtext)
            trigger = "basic"
            triggerregex = re.compile(r"(!trigger1)")  # (r"((?<=(name\": \")).*?(?=(\",\"sender_id\": \"\d{8})))")
            print(triggerregex)
            triggers = []
            triggers = triggerregex.findall(searchtext)
            if len(triggers) > 0:
                print(triggers[0])
                trigger = triggers[0]
            if trigger == "!trigger1":
                trigger1 = 1
                print("trigger1 = 1")

            triggerregex = re.compile(r"(trigger2)")  # (r"((?<=(name\": \")).*?(?=(\",\"sender_id\": \"\d{8})))")
            print(triggerregex)
            triggers = []
            triggers = triggerregex.findall(searchtext)
            if len(triggers) > 0:
                print("printing triggers in trigger2")
                print(triggers)
                trigger = triggers[0]
            if trigger == "trigger2":
                trigger2 = 1
                print("trigger2 = 1")


        except:
            stuff = "basic stuff \n second line"
            print("error at line 87")
            responsetext = "error"


        if trigger1 == 1:
            responsetext = responsetext1


        elif trigger2 == 1:
            responsetext = trigger2text


        # data = urllib.parse.urlencode({'bot_id': '', 'text': responsetext1}).encode()
        # print(str(data))
        # req = urllib.request.Request("https://api.groupme.com/v3/bots/post?",
        #                              data)  # this will make the method "POST"
        # print(req)
        # resp = urllib.request.urlopen(req)

        findingstotal = trigger1 + trigger2
        print("findings total:" + str(findingstotal))

        if findingstotal > 0:
            try:
                data = urllib.parse.urlencode({'bot_id': botid, 'text': responsetext}).encode()
                print(str(data))
                req = urllib.request.Request("https://api.groupme.com/v3/bots/post?",
                                             data)  # this will make the method "POST"
                print(req)
                resp = urllib.request.urlopen(req)


            except:
                # https://api.groupme.com/v3/bots/post?bot_id=id&text=Hello+world
                resp = urllib.request.urlopen("https://api.groupme.com/v3/bots/post?bot_id=" + botid + "&text=Hello+world")


        print("past the post attempt")

    return {"message": "Hello, World!"}


def post_handler(event, context):
    print("this is post_handler")

    return{"message": "This is post_handler"}