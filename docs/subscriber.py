#!/usr/bin/env python

import zmq
import json

def handle(msg):
    print
    print "Action: %s" % msg["action"]
    print "Device: %s" % msg["device"]
    print "Time: %s" % msg["time"]
    if msg.has_key("method"):
        print "Method: %s" % msg["method"]
    if msg.has_key("url"):
        print "URL: %s" % msg["url"]
    if msg.has_key("command"):
        print "Command: %s" % msg["command"]
    if msg.has_key("status"):
        print "Status: %s" % msg["status"]
    if msg.has_key("text"):
        for v in msg["text"]:
            print "Text: %s" % v
    if msg.has_key("payload"):
        print "Payload: <present>"
    if msg.has_key("body"):
        print "Body: <present>"
    if msg.has_key("from"):
        print "From: %s" % msg["from"]
    if msg.has_key("to"):
        for v in msg["to"]:
            print "To: %s" % v
    if msg.has_key("header"):
        for k in msg["header"]:
            print "%s: %s" % (k, msg["header"][k])
    if msg.has_key("type"):
        print "Type: %s" % msg["type"]
    if msg.has_key("queries"):
        for v in msg["queries"]:
            print "Query: %s" % v
    if msg.has_key("answers"):
        for v in msg["answers"]:
            if v.has_key("name"):
                print "Answer name: %s" % v["name"]
            if v.has_key("address"):
                print "Answer address: %s" % v["address"]

ctxt = zmq.Context()
skt = ctxt.socket(zmq.SUB)
skt.connect("tcp://localhost:5555")
skt.setsockopt(zmq.SUBSCRIBE, "")

while True:
    msg = skt.recv()
    handle(json.loads(msg))

