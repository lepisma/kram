# Plotting server for kram

import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue

from flask import Flask, Response, request, render_template


class SSE(object):

    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data : "data",
            self.event : "event",
            self.id : "id"
        }

    def encode(self):
        if not self.data:
            return ""
        lines = ["%s: %s" % (v, k) 
                 for k, v in self.desc_map.iteritems() if k]
        
        return "%s\n\n" % "\n".join(lines)

app = Flask(__name__)
subscriptions = []


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/push")
def publish():
    msg = request.args.get("data")
    def notify():
        for sub in subscriptions[:]:
            sub.put(msg)
    
    gevent.spawn(notify)
    
    return "ok"

@app.route("/subscribe")
def subscribe():
    def gen():
        q = Queue()
        subscriptions.append(q)
        try:
            while True:
                result = q.get()
                ev = SSE(str(result))
                yield ev.encode()
        except GeneratorExit:
            subscriptions.remove(q)

    return Response(gen(), mimetype="text/event-stream")

def run_server():
    server = WSGIServer(("", 5000), app)

    @app.route("/stop")
    def stop():
        server.stop()
        return "ok"

    try:
        server.serve_forever()

    except KeyboardInterrupt: 
        server.stop()
