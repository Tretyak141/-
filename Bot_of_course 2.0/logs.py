def check(chat_id):
    file = open(f'logs/{chat_id}.txt')
    info = file.readline()
    file.close()
    file = open(f'logs{chat_id}.txt','w+')
    file.seek(0)
    file.close()
    return info

def write(chat_id,text):
    file = open(f'logs/{chat_id}.txt','w+')
    file.write(text)
    file.close()