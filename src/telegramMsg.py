import telepot
    
def message(msg):
    token = telepot.Bot("5020758984:AAEYj7Gr-RToHA_ys81qYIAj6_DKobaA-ro")
    chat_id = '472673848'
    token.sendMessage(chat_id,msg)
    
