from flask import Flask, redirect, render_template, request, url_for
from detect import run
import cv2


# Flask Logic

app = Flask(__name__)
#Bootstrap(app)

#create route for Homepage

@app.route("/", methods=['GET', 'POST'])
def index():
    
    return render_template("bootstrap_main_homepage.html")

#create Route for Text translation
@app.route('/translation', methods=['POST', 'GET'])
def my_form_post():

    if request.method == "POST":
  
        param1 = request.form['translation']

        words = ["Hello", "Yes", "No", "Thank you", "I love you", "My", "Name is", "You", "are beautiful"]
        if param1 in words:
            return render_template('bootstrap_main_texttranslator.html', result = param1)
        else:
            param1 = param1.upper()
            letters = [char for char in param1]
            return render_template('bootstrap_main_texttranslator.html', result = letters)

    
    else:
        return render_template('bootstrap_main_texttranslator.html')

#create route for video translation

@app.route('/video', methods=['GET', 'POST'])
def my_video(): 
    if request.method == 'GET':
        return render_template('bootstrap_main_video.html')
    

@app.route('/show_video')
def show_video():
    run(weights= r"runs\train\exp\weights\version6.pt", imgsz=(416, 416), conf_thres=0.1, dnn=True, source=0)

def stop_video():
    if cv2.waitKey(1) == ord('q'):  # q to quit
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app.run(debug=True, port= 2412)