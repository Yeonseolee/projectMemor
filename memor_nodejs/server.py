import io
import os
import socket
import struct
from PIL import Image
from datetime import datetime

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')
photo_su = 0
try:
    while True:
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        image_stream.seek(0)

        image = Image.open(image_stream)
        #image.show()
        print('Image is %d%d' % image.size)
        image.verify()
        print('Image is verified')
        nowDate = datetime.now()
        print(nowDate)
        image.save(nowDate.strftime(str(photo_su)+'_'+"%Y-%m-%d_%H_%M_%S") + ".PNG")
        print('Image is saved')
        photo_su += 1
finally:
    connection.close()
    server_socket.close()