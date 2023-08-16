import pebl

def log(s):
    print(s)

pebl.subscribe("topic", log)

pebl.publish("topic", "some data for subscription!")
