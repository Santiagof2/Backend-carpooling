
def is_valid_message(message):
    if(not message['room']): return False
    if(not message['message']): return False
    if(not message['id_user']): return False
    return True
