from flask import Flask, send_file
import logging
from modules.video import streaming

app = Flask(__name__)

@app.route('/video/streaming/<command>')
def streaming_api(command):
    if(command == 'start'):
        logging.debug("start")
        streaming.start()
    elif (command == 'stop'):
        logging.debug("stop")
        streaming.stop()
    elif(command == 'frame'):
        logging.debug("frame")
        return send_file(streaming.frame(), mimetype='image/jpeg')
    
    return 'ok'
