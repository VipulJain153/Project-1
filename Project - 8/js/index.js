let typed = new Typed('#welcome', {
    strings: ['Mini Postman'],
    typeSpeed: 50,
    loop:true
  });

let requestTypes = Array.from(document.getElementsByClassName("request")); 
let request;
let form = document.forms[1];
const POST = document.getElementById("POST");
const GET = document.getElementById("GET");
let JSONelem = document.getElementById("JSON");
let response = document.getElementById("response");
JSONelem.style.visibility = "hidden"
response.style.visibility = "hidden"
let str;

POST.addEventListener('click', (e) => {
    JSONelem.style.visibility = "visible"
}); 
GET.addEventListener('click', (e) => {
    JSONelem.style.visibility = "hidden"
}); 

form.addEventListener('submit', e => {
    e.preventDefault();
    let val = document.getElementById("JSON").value;
    let link = document.getElementById("link").value;
    requestTypes.forEach(e => {
        if (e.checked) {request = e.value;};
    });
    if (request=="GET"){
        GETREQUEST(link)
    } else {
        POSTREQUEST(JSON.parse(val),link)
    }
});

function POSTREQUEST(params,link){
    response.style.visibility = "visible"
    const xhr = new XMLHttpRequest();
    xhr.open("POST", link);
    xhr.getResponseHeader("Content-Type","application/json")
    xhr.onprogress = ()=>response.innerText = "Loading...."
    // xhr.onreadystatechange  = ()=>console.log('the state is',xhr.readyState)
    xhr.onload = function(){           
        str = `${this.responseText} status:${this.status}`       
        response.innerText = str
    }
    xhr.onerror = function(){
        str = `${this.responseText} status:${this.status}`   
        response.innerText = str
    }
    xhr.send(params); 
}
function GETREQUEST(link){
    response.style.visibility = "visible"
    const xhr = new XMLHttpRequest();
    xhr.open("GET", link);
    // xhr.onreadystatechange  = ()=>console.log('the state is',xhr.readyState)
    xhr.onprogress = ()=>response.innerText = "Loading...."
    xhr.onload = function(){  
        str = `${this.responseText} status:${this.status}`   
        response.innerText = str
    }
    xhr.onerror = function(){
        str = `${this.responseText} status:${this.status}`   
        response.innerText = str
    }
    xhr.send();
}

