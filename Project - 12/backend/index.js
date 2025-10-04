const io = require("socket.io")(8000, { cors: { origin: "*" } });

const users = {};
const rooms = {};

io.on("connection", (socket) => {
  socket.on("user-joined", (name, room) => {
    users[socket.id] = name;
    rooms[socket.id] = room;
    socket.join(room);
    socket.to(room).emit("new-user-joined", {
      msg: `${name} joined the chat!`,
      type: "other",
    });
  });
  socket.on("send-msg", (msg) => {
    socket
      .to(rooms[socket.id])
      .emit("recv-msg", { msg: `${users[socket.id]}: ${msg}`, type: "other" });
  });
  socket.on("disconnect", (reason) => {
    socket.to(rooms[socket.id]).emit("left-chat", {
      msg: `${users[socket.id]} left the chat!`,
      type: "other",
    });
  });
});
