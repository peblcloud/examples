package main

import (
	"net/http"

	pebl "github.com/peblcloud/go"
)

func main() {
	svc := http.NewServeMux()
	svc.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		w.Write([]byte("hello world!\n"))
	})

	pebl.Service(svc, "hey.pebl.rocks")
}
