import socket
from config import TWITCH_TOKEN

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'kysti4ekn'  # например, kyst
token = TWITCH_TOKEN
channel = '#kysti4ekn'  # или другой канал

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

print(f"✅ Подключено к {channel}")
def get_chat():
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))


    if 'PRIVMSG' in resp:
        parts = resp.split('!', 1)
        user = parts[0][1:]
        message = resp.split('PRIVMSG', 1)[1].split(':', 1)[1]
        twitch_message = f"{user}: {message.strip()}"
        return twitch_message
