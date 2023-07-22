package main

import (
	"context"
	"fmt"
	"net/http"

	pebl "github.com/peblcloud/go"
	"github.com/redis/go-redis/v9"
)


func main() {
	r, _ := pebl.Redis("redis-1")
	rdb := redis.NewClient(&redis.Options{
		Addr: r.Addr,
	})

	svc := http.NewServeMux()
	svc.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		count, _ := rdb.Get(context.Background(), "count").Result()
		res := fmt.Sprintf("current count: %s", count)
		w.Write([]byte(res))
	})

	svc.HandleFunc("/incr", func(w http.ResponseWriter, _ *http.Request) {
		rdb.Incr(context.Background(), "count")
	})

	svc.HandleFunc("/reset", func(w http.ResponseWriter, _ *http.Request) {
		rdb.Set(context.Background(), "count", "0", 0)
	})

	pebl.Service(svc, "your-subdomain.pebl.rocks")
}
