"""
Kram
"""

# from tinydb import TinyDB
import requests
import threading
import server
import webbrowser
import json

EXPERIMENT_NAME = ""
run = 0
root = "http://localhost:5000"

def init(name):
    """
    Initialize the experiment
    """
    
    global EXPERIMENT_NAME
    EXPERIMENT_NAME = name
    t = threading.Thread(target=server.run_server, args=())
    t.start()
    
    # Wait till server is on
    # while True:
    #     try:
    #         requests.get(root)
    #         break
    #     except requests.exceptions.ConnectionError:
    #         print "test"
    #         continue
        
    webbrowser.open(root)

def end():
    """
    Signals the end of experiment
    """

    end_data = {
        "x": "end"
    }
     
    t = threading.Thread(
        target=requests.get,
        args=(
            root + "/push",
            {"data": json.dumps(end_data)}
        )
    )
    
    t.start()

def shutdown():
    """
    Shutdown server
    """

    requests.get(root + "/stop")
    

class kram(object):
    """
    Decorator class
    """
    
    def __init__(self):
        """
        Initialize experiment and store
        """
        
        self.experiment = EXPERIMENT_NAME
        # Create a db with name of the experiment
        # self.db = TinyDB(self.experiment + ".json")
        # Live flag tells kram to live plot the output (currently assuming single output)
        self.live = True

    def __call__(self, func):
        """
        Call function and log results
        """

        def krammed(*args, **kwargs):
            global run
            output = func(*args, **kwargs)

            data = {
                "in": args,
                "out": output
            }

            # table = self.db.table(func.__name__)
            # table.insert(data)

            if self.live:
                # Call plotting routine

                plot_data = {
                    "x": run,
                    "y": data["out"],
                    "func": func.__name__,
                    "title": EXPERIMENT_NAME
                }
                
                self.push(json.dumps(plot_data))
                
                run += 1
            
        return krammed

    def push(self, data):
        
        # Start a new thread for updating
        t = threading.Thread(
            target=requests.get,
            args=(
                root + "/push",
                {"data": data}
            )
        )
        
        t.start()
