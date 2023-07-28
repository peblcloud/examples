package main

import (
	pebl "github.com/peblcloud/go"
)

func main() {
	v, ok, _ := pebl.KVGet("foo")
	println("value:", v)
	println("found:", ok)

	pebl.KVSet("foo", "bar")

	v, ok, _ = pebl.KVGet("foo")
	println("value:", v)
	println("found:", ok)
}
