import { React } from "react";
import Logo from "/logo.png";

function Header() {
  return (
    <>
      <nav className="flex justify-center items-center bg-slate-800 p-4">
        <img src={Logo} alt="" className="w-24" />
      </nav>
    </>
  );
}

export default Header;
