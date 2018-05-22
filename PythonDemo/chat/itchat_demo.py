import itchat

# itchat.get_QR(uuid=itchat.get_QRuuid(), picDir='E:\Program Files\sf-demo\PythonLearn\PythonDemo\chat\pic.jpg')
itchat.auto_login(picDir='pic-1.jpg')

itchat.send('Hello, filehelper', toUserName='filehelper')