# intro to redis

This is the companion project to the
[intro to redis](https://docs.pebl.io/guides/python/redis) guide.

## running

You can follow the steps in the guide, but a quickstart would be:

  1. start your local cluster with `pebl up`
  2. execute `pebl run` inside this folder
  3. inspect the workloads with `pebl info`

The info pane (from `pebl info`) will show the endpoint and the local port that
it is currently bound to. You can send requests to the two configured endpoints
at `/` and `/incr`.

```bash
$ curl localhost:55000/
hello, world!
$ curl localhost:55000/incr
{"count": 1}
$ curl localhost:55000/incr
{"count": 2}
$
``` 

Note that you should replace `:55000` with the port that's shown on the info
pane!
