import * as pebl from "pebl";
import * as http from "http";

const listener = function (req, res) {
  res.writeHead(200);
  res.end("hello, world!\n");
};

const server = http.createServer(listener);
pebl.service(server, "your-subdomain.pebl.rocks");
