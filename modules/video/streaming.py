import logging
import threading
from time import sleep
from picamera import PiCamera

isStreaming = False

def start():
    logging.debug('Starting streaming')
    global isStreaming
    isStreaming = True
    try:
       threading.Thread(target=doStream).start()
    except:
       logging.error("Error: unable to start thread")


def stop():
    logging.debug('Stopping streaming')
    global isStreaming
    isStreaming = False

def frame():
    logging.debug('Frame from streaming ...')
    return 'foo.jpg'


def doStream():
    global isStreaming
    while isStreaming:
        logging.debug("streaming")
        camera = PiCamera()
        camera.resolution = (600, 400)
        camera.start_preview(fullscreen=False)
        # Camera warm-up time
        sleep(2)
        camera.capture('foo.jpg')
    logging.debug("streaming stopped.")
    camera.stop_preview()
