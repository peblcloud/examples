# intro to redis

This is the companion project to the
[intro to redis](https://docs.pebl.io/guides/go/redis) guide.

## running

You can follow the steps in the guide, but a quickstart would be:

  1. start your local cluster with `pebl up`
  2. execute `pebl run` inside this folder
  3. inspect the server with `pebl info`

The info pane (from `pebl info`) will show the endpoint and the local port that
it is currently bound to. You can send requests to it using curl:

```bash
$ curl localhost:55000/incr
$ curl localhost:55000/
current count: 1
$ curl localhost:55000/reset
$ curl localhost:55000/
current count: 0
$
```

Note that you should replace `:55000` with the port that's shown on your info
pane.

You can also use `redis-cli` to connect to the redis instance. Make sure to
use the `-p` flag to provide the locally bound port:

```bash
$ redis-cli -p 12345
```
