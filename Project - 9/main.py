from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
import os, cv2,numpy as np
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/imgs"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        for i in os.listdir(app.config['UPLOAD_FOLDER']):
            os.remove(f"{app.config['UPLOAD_FOLDER']}/{i}")
        option = request.form["Option"]  
        file = request.files["photoFile"]
        if file.filename != "":
            path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
            file.save(path)
            img = cv2.imread(path)
            match option:
                case "gray":
                    print("g")
                    cv2.imwrite(f"{app.config['UPLOAD_FOLDER']}/1.png",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
                case "Erode":
                    print("e")
                    cv2.imwrite(f"{app.config['UPLOAD_FOLDER']}/1.png",cv2.erode(img,np.ones((5,5))))
                case "Dilate":
                    print("d")
                    cv2.imwrite(f"{app.config['UPLOAD_FOLDER']}/1.png",cv2.dilate(img,np.ones((5,5))))
                case "blur":
                    print("b")
                    cv2.imwrite(f"{app.config['UPLOAD_FOLDER']}/1.png",cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT))
            return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5500,host='127.0.0.1')