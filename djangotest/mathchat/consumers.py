from channels import Group
from models import ChatRoom, Message

def ws_connect(message):
    message.reply_channel.send({
        'accept': True
    })
    Group(message.content['path'][1:]).add(message.reply_channel)
    print message.content['path']

def ws_disconnect(message):
    Group('mathchat').discard(message.reply_channel)
    print "disconnected"

def ws_message(message):
    r = ChatRoom.objects.get(name=message.content['path'][1:])
    m = Message(body=message.content['text'], room=r)
    m.save()
    Group(message.content['path'][1:]).send({
        'text': message.content['text']
    })

