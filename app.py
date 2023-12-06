from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
import sys
#sys.path.append('C:/Users/adity/Object-Detection-YOLO/YOLOv5-Flask/yolo/Lib/site-packages/cv2')

app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return

    video = request.files['video']
    video_path = os.path.join(uploads_dir, secure_filename(video.filename))
    video.save(video_path)
    
    # Print the list of files in the uploads directory
    files_in_uploads = os.listdir(uploads_dir)
    print("Files in uploads directory:", files_in_uploads)

    subprocess.run(['python3', 'detect.py', '--source', video_path])

    obj = secure_filename(video.filename)
    return obj

@app.route("/opencam", methods=['GET'])
def opencam():
    print("here")
    subprocess.run(['python3', 'detect.py', '--source', '0'])
    return "done"
    

@app.route('/return-files', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("runs/detect", obj)
    print(loc)
    try:
        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
        # return send_from_directory(loc, obj)
    except Exception as e:
        return str(e)

# @app.route('/display/<filename>')
# def display_video(filename):
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static/video_1.mp4', code=200))