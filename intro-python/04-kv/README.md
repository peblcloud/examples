# intro to distributed dictionary

This is the companion project to the
[intro to storage](https://docs.pebl.io/guides/python/dictionary) guide.

## running

You can follow the steps in the guide, but a quickstart would be:

  1. start your local cluster with `pebl up`
  2. execute `pebl run` inside this folder
  3. inspect the output with `pebl info`

You can also explore utilizing the CLI to interact with the distributed
dictionary:

```
$ pebl kv set foo "hello world!" --env local
$ pebl kv get foo --env local
$ pebl kv list
```
