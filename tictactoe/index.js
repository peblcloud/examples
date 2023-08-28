import { Server } from "socket.io";
import * as pebl from "pebl";
import { createClient } from "redis";
import { createServer } from "http";
import express from "express";
import { randomBytes } from "crypto";
import path from "path";
import { createAdapter } from "@socket.io/redis-adapter";

const __dirname = path.resolve();

const app = express();

app.get("/create", function (req, res) {
  const payload = {
    id: randomBytes(2).toString("hex"),
  };
  res.send(payload);
});

app.get("/*", function (req, res) {
  res.sendFile("site/index.html", { root: __dirname });
});

const server = createServer(app);

const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

const redisInfo = await pebl.redis("redis");
const redisURL = `redis://${redisInfo.host}:${redisInfo.port}`;

const pubClient = createClient({ url: redisURL });
const subClient = pubClient.duplicate();

io.adapter(createAdapter(pubClient, subClient));

const client = createClient({
  url: redisURL,
});
client.on("error", (err) => console.log("Redis Client Error", err));

io.on("connection", (socket) => {
  socket.on("join", (room) => {
    socket.join(room);
    client.hGetAll(room).then((values) => socket.emit("state", values));
  });

  socket.on("become", (room, player) => {
    // tell the other connection
    socket.to(room).emit("player", player);
  });

  socket.on("play", (room, player, move) => {
    console.log(room, player, move);

    // sanity check the inputs
    if (player !== "0" && player !== "1") {
      return;
    }

    const idx = parseInt(move);
    if (idx === undefined || idx < 0 || idx > 8) {
      return;
    }

    client
      .hGetAll(room)
      .then((values) => {
        if (Object.keys(values).length % 2 !== parseInt(player)) {
          throw Error("out of order");
        }
      })
      .then(() => client.hSetNX(room, move, player))
      .then(() => client.hGetAll(room))
      .then((values) => io.to(room).emit("state", values))
      .catch((err) => {
        console.log("error during play event:", err.toString());
        return;
      });
  });

  socket.on("reset", (room) => {
    client
      .del(room)
      .then(() => io.to(room).emit("state", {}))
      .catch((err) => {
        console.log("error during reset event:", err.toString());
        return;
      });
  });
});

await client
  .connect()
  .then(() => pubClient.connect())
  .then(() => subClient.connect())
  .then(() => pebl.service(server, "ttt.pebl.rocks"));

await client
  .disconnect()
  .then(() => pubClient.disconnect())
  .then(() => subClient.disconnect());

io.close();
