import { React, useState, useRef, useEffect } from "react";
import Message from "./Message";
import { io } from "socket.io-client";
import sound from "../assets/ping.mp3";

const socket = io("http://localhost:8000");
const pingSound = new Audio(sound);

function JoinForm() {
  const [joined, setJoined] = useState(false);
  const [room, setRoom] = useState("");
  const [name, setName] = useState("");
  const [msgs, setMsgs] = useState([]);
  const nameInput = useRef(null);
  const roomInput = useRef(null);
  const MessageInput = useRef(null);

  useEffect(() => {
    if (joined == true) {
      socket.emit("user-joined", name, room);
    }
  }, [joined]);

  socket.on("new-user-joined", (msg) => {
    setMsgs((prevMgs) => [...prevMgs, msg]);
    setMsgs((arr) => [...new Set(arr)]);
    pingSound.play();
  });

  socket.on("recv-msg", (msg) => {
    setMsgs((prevMgs) => [...prevMgs, msg]);
    setMsgs((arr) => [...new Set(arr)]);
    pingSound.play();
  });

  socket.on("left-chat", (msg) => {
    setMsgs((prevMgs) => [...prevMgs, msg]);
    setMsgs((arr) => [...new Set(arr)]);
    pingSound.play();
  });

  return (
    <>
      {!joined ? (
        <>
          <div className="container grid-cols-1 bg-slate-700 h-96 p-24 pt-46 pb-96">
            <form
              action=""
              className="grid justify-center items-center flex-col mb-64"
            >
              <div>
                <label
                  htmlFor="name"
                  className="text-white font-bold font-mono text-2xl m-4"
                >
                  Name:
                </label>
                <input
                  ref={nameInput}
                  type="text"
                  id="name"
                  autoComplete="false"
                  className="text-mono rounded border-teal-600 border-t-2 border-b-2 border-l-2 border-r-2 p-2"
                />
              </div>
              <br />
              <div>
                <label
                  htmlFor="room"
                  className="text-white font-bold font-mono text-2xl m-4"
                >
                  Room:
                </label>
                <input
                  ref={roomInput}
                  type="text"
                  id="room"
                  autoComplete="false"
                  className="text-mono rounded border-teal-600 border-t-2 border-b-2 border-l-2 border-r-2 p-2"
                />
              </div>

              <button
                className="justify-self-end bg-red-600 p-4 rounded-3xl text-white text-xl m-8 translate-x-9 hover:bg-red-400 transition-all duration-1000 ease-in"
                onClick={(e) => {
                  e.preventDefault();
                  if (
                    roomInput.current.value !== "" &&
                    nameInput.current.value !== ""
                  ) {
                    setName((prev) => nameInput.current.value);
                    setRoom((prev) => roomInput.current.value);
                    setJoined(true);
                  }
                }}
              >
                Join
              </button>
            </form>
          </div>
        </>
      ) : (
        <>
          <div className="container grid-cols-1 bg-slate-700 h-96 p-24 pt-46 pb-12 ">
            <div className="container p-16 border-black border-t-2 border-b-2 border-l-2 border-r-2 rounded-2xl h-64 overflow-auto">
              <div className="rounded-2xl bg-slate-400 clear-both text-white p-2 m-2 float-left max-w-lg break-all ">
                Hello Sir, You Joined the Room "{room}" with the name "{name}".
              </div>
              <Message msgs={msgs}></Message>
            </div>
          </div>
          <div className="container grid-cols-1 bg-slate-700 p-4">
            <form action="" className="grid">
              <input
                ref={MessageInput}
                type="text"
                className="text-mono rounded border-teal-600 border-t-2 border-b-2 border-l-2 border-r-2 p-2 w-full"
              />
              <button
                type="submit"
                className="bg-red-600 p-4 rounded-3xl text-white text-xl m-8 hover:bg-red-400 transition-all duration-1000 ease-in"
                onClick={(e) => {
                  e.preventDefault();
                  if (MessageInput.current.value !== "") {
                    socket.emit("send-msg", MessageInput.current.value);
                    let MyMsg = MessageInput.current.value;
                    MyMsg = { msg: MyMsg };
                    MyMsg.type = "me";
                    setMsgs((prevMsgs) => [...prevMsgs, MyMsg]);
                    MessageInput.current.value = "";
                  }
                }}
              >
                Send
              </button>
            </form>
          </div>
        </>
      )}
    </>
  );
}

export default JoinForm;
