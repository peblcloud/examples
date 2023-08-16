package main

import (
	pebl "github.com/peblcloud/go"
)

func main() {
	pebl.Subscribe("topic", func(s string) {
		println(s)
	})

	pebl.Publish("topic", "some data for topic!")
}
