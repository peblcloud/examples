# intro to services

This is the companion project to the
[intro to services](https://docs.pebl.io/guides/go/service) guide.

## running

You can follow the steps in the guide, but a quickstart would be:

  1. start your local cluster with `pebl up`
  2. execute `pebl run` inside this folder
  3. inspect the server with `pebl info`

The info pane (from `pebl info`) will show the endpoint and the local port that
it is currently bound to. You can send requests to it using curl:

```bash
$ curl localhost:55000/
hello world!
$
``` 

Note that you should replace `:55000` with the port that's shown on your info
pane!
