# chat

A simple Flask application for sending and receiving messages.

## wsgi_run

This pebl method creates an external endpoint, serving the provided Flask
application at `hey.pebl.rocks`. The pebl platform automatically handles load
balancing and autoscaling.

With pebl, there is no need to manually manage re-using or releasing the process
back to a managing server like gunicorn. Each request is provided a unique
process. This allows interesting uses like the `after` argument, which runs
after the entire response has been sent to the client.


## sleep 

Using the `after` handler, we show a unique way of implementing delayed
messages. The `sleep` call signals to pebl that the process can be unscheduled
for the requested duration. This allows better usage of resources than using
standard `time.sleep` method.
