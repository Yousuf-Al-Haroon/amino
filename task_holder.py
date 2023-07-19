from send_message import send_message
from login import login

from fancy_text import fancy as fan
import mishkal.tashkeel as tashkeel

vocalizer = tashkeel.TashkeelClass()
def tashkeel(text):
    return vocalizer.tashkeel(text)

def fancy(text):
    s = "    "
    return str(fan.box(text) + s + fan.bold(text) + s + fan.light(text) + s + fan.sorcerer(text))


client = login()

@client.event("on_text_message")
def task_holder(data):
    community_id = data.json.get("ndcId")
    chat_id = data.json.get("chatMessage", {}).get("threadId")
    message_id = data.json.get("chatMessage", {}).get("messageId")
    nickname = data.json.get("chatMessage", {}).get("author", {}).get("nickname")
    user_id = data.json.get("chatMessage", {}).get("author", {}).get("uid")
    message_content = data.json.get("chatMessage", {}).get("content")
    content = message_content.replace(message_content.split(":")[0], "")[1:]
    try:
        if message_content.startswith("زخرفة:"):
            send_message(community_id, chat_id, fancy(content), replyTo=message_id)
        elif message_content.startswith("تشكيل:"):
            send_message(community_id, chat_id, tashkeel(content), replyTo=message_id)
    except Exception as e:
        print(e)

client.launch()