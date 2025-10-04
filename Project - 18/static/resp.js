burger = document.querySelector(".burger")
navbar = document.querySelector("#navbar")
navlist = document.querySelector(".navlist")
rightNav = document.querySelector(".right-nav")
burger.onclick = ()=> {
    burger.classList.toggle("change")
    navbar.classList.toggle("hresp")
    navlist.classList.toggle("vresp")
    rightNav.classList.toggle("vresp")
}
