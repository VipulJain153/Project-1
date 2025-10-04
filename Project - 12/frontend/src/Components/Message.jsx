import React from "react";

const Message = ({ msgs }) => {
  return (
    <>
      {msgs.map((msg, index) => {
        if (msg.type === "me") {
          return (
            <div
              key={index}
              className="rounded-2xl bg-slate-400 clear-both text-white p-2 m-2 float-right max-w-lg break-all "
            >
              You: {msg.msg}
            </div>
          );
        } else {
          return (
            <div
            key={index}
            className="rounded-2xl bg-slate-400 clear-both text-white p-2 m-2 float-left max-w-lg break-all "
            >
              {msg.msg}
            </div>
          );
        }
      })}
    </>
  );
};

export default Message;
