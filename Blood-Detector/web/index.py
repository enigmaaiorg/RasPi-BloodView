from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import sys
import time

path_blood_det_py = "./../"
sys.path.append(path_blood_det_py)
from blood_detection import detection

app = Flask(__name__)

UPLOAD_FOLDER = os.path.abspath("./static/inference/input")
OUTPUT_FOLDER = os.path.abspath("./static/inference/output")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER
ALLOWED_EXTENSIONS = set(["mp4", "jpg", "png", "jpeg"])

def allowed_file(filename):
    
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


fileNameInput = ""
boolI = False
boolV = False
finished = False 
time_total, counter = 0, 0
@app.route("/", methods = ["GET", "POST"])
def home():

    global fileNameInput, boolI, boolV, time_total, finished, counter
    filename = fileNameInput
    boolImage = boolI
    boolVideo = boolV
    t_t = time_total
    list_files_out = os.listdir(app.config["OUTPUT_FOLDER"])
    finished= True if counter != 0 and filename in list_files_out else False

    if request.method == "POST":
        

        if "ourfile" in request.files:
            f = request.files["ourfile"]
            
            if f.filename == "":
                return "No se ha seleccionado ningún archivo NADA"
            
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                filenameAbsolute = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                f.save(filenameAbsolute)
                fileNameInput = filename

                boolI = True if filename.split(".")[-1] in ("jpg", "png", "jpeg") else False
                boolImage = boolI
                boolV = True if filename.split(".")[-1] in ("mp4") else False
                boolVideo = boolV

# -----------------------------------------------------------------------------------
# Predict model 
        
        if "predictRequest" in request.form:
            
            start = time.time()
            fnsd = detection(filename)
            done = time.time()

            elapsed = done - start
            if fnsd == 0:
                counter += 1
                finished, time_total = True, round(float(str(elapsed).split(" ")[0]), 3)
            else:
                finished, time_total = False, round(float(str(elapsed).split(" ")[0]), 3)
            #finished = False     

#-------------------------------------------------------------------------------------
        return redirect("/#about")

# Directory input and output cleaned

    files_uploaded = [f_ for f_ in os.listdir(app.config["UPLOAD_FOLDER"])]
    if len(files_uploaded) > 20:
        for file in files_uploaded:
            if file not in ('test_video.mp4', 'test_image.jpg'):
                os.remove(os.path.join(app.config["UPLOAD_FOLDER"], file))
        print("")
        print("Directory input cleaned!")
        print("")
    
    files_predicted = [f_ for f_ in os.listdir(app.config["OUTPUT_FOLDER"])]
    
    if len(files_predicted) > 22:
        for file in files_predicted:
            if file not in ('test_video.mp4', 'test_image.jpg'):
                os.remove(os.path.join(app.config["OUTPUT_FOLDER"], file))
        print("")
        print("Directory output cleaned!")
        print("")

#-------------------------------------------------------------------------------------

    context = {'mediaFileName': filename, 'boolVideo': boolVideo, 
                'boolImage': boolImage, 'time': t_t, 'finished': finished}

    return render_template("index.html", context = context)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)