// Variables

const fetchBtn = document.getElementById("fetchBtn");

// Classes and Functions

class POSTMAN {

    constructor () {
        this.GET = this.getStatus("GET").checked;
        this.POST = this.getStatus("POST").checked;
        this.url = this.getStatus("link").value;
        this.response = this.getStatus("response");
        if (this.POST) {
            this.JSON = JSON.parse(this.getStatus("JSON").value);
            this.post(this.url, this.JSON);
        } else {
            this.get(this.url);
        };
    };

    getStatus (id) {
        return document.getElementById(id);
    };

    display(data) {
        this.response.innerText = data;
    }

    async post(url, json) {
        try {
            const response = await fetch(url,json);
            const data = await response.json();
            if (data!==undefined){
                this.display(JSON.stringify(data));
            } else {
                this.display("Loading...");
            };
        } catch(err) {
            this.display(`An Error Occurred: ${err}`);
        };
    }

    async get(url) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            if (data!==undefined){
                this.display(JSON.stringify(data));
            } else {
                this.display("Loading...");
            };
        } catch(err) {
            this.display(`An Error Occurred: ${err}`);
        };
    }

}

// Events

fetchBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const PostMan = new POSTMAN();
});