import json
from channels.generic.websocket import WebsocketConsumer

#웹소켓 class instance
class ChatConsumer(WebsocketConsumer):
    #웹소켓에 연결
    def connect(self):
        self.accept()

    # websocket 연결 종료 시 실행
    def disconnect(self, close_code):
        pass

    # client 로부터 메세지를 받을 때 실행
    def receive(self, text_data, bytes_data):
        # return super().receive(text_data=text_data, bytes_data=bytes_data)
        # josn으로 채팅 메시지를 받아요
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
    	
        # 클라이언트로부터 받은 메세지 다시 클라이언트로 보내기
	    #json 객체를 인코딩 해서 보내요
        self.send(text_data=json.dumps({
            'message': message
        }))