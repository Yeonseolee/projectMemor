import io
import socket
import struct
import time
import picamera
import json

client_socket = socket.socket()
client_socket.connect(('192.168.0.23', 8000))
print("starting")

connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_preview()
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            if time.time() - start > 3:
                break
            stream.seek(0)
            stream.truncate()
        connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()