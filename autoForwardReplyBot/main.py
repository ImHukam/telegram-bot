from ast import Try
from turtle import fd
import telebot
from telebot import types
 
API = ""
print(API)
bot = telebot.TeleBot(API, parse_mode=None)

@bot.message_handler(commands=['start', 'restart'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to Polygon Support! type /commands or /buttons for support options")

@bot.message_handler(commands=['commands'])
def send_commands(message):
    print(message)
    bot.send_message(message.chat.id, "commands: \n /FAQs \n /support <your query> \n /help \n /developer_help\n /buttons \n /restart")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "visit https://polygon.technology/contact-us for more details")

@bot.message_handler(commands=['developer_help'])
def send_developer_help(message):
	bot.send_message(message.chat.id, "visit our developer page https://polygon.technology/developers")

@bot.message_handler(commands=['FAQs'])
def send_faqs(message):
	bot.send_message(message.chat.id, "polygon FAQs: https://docs.polygon.technology/docs/home/faq")

@bot.message_handler(commands=['close'])
def send_clsoe(message):
    markup = types.ReplyKeyboardRemove(selective = False)
    bot.send_message(message.chat.id, "button closed, go to /commands for more support", reply_markup=markup)
    
@bot.message_handler(commands=['buttons'])
def send_buttons(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1= types.KeyboardButton("/FAQs")
    btn2= types.KeyboardButton("/commands")
    btn3= types.KeyboardButton("/help")
    btn4= types.KeyboardButton("/developer_help")
    btn5= types.KeyboardButton("/restart")
    btn6= types.KeyboardButton("/close")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, "choose from these options", reply_markup=markup)

@bot.message_handler(func = lambda msg:'@Polygon_Support_TestBot' in msg.text)
def send_support(message):
    try:
        if(message.chat.id == 'here chat id'):
            groupid= 1
        elif(message.chat.id == 'here chat id'):
            groupid= 2

        if(message.chat.id == 'here chat id' or message.chat.id == 'here chat id'):
            msgid= message.message_id
            name= message.from_user.first_name + " " + message.from_user.last_name + " ( @" + message.from_user.username + " )"
            groupname= message.chat.title + " ( @" + message.chat.username +" )"
            msgtext= (message.text).replace('@Polygon_Support_TestBot','')

            msg= "\nUserInfo"+ "\nfrom- " + str(groupname) + "\nname- " + name + "\nmsgid- "+str(msgid)+"\ngroupid- #" + str(groupid)
            forward_msg= "Query: "+ msgtext + "\n" + msg
            bot.send_message('here chat id', forward_msg)
            bot.reply_to(message,"Query sents to polygon team,wait for response!!")
            # time.sleep(5)
            # bot.delete_message(cid,msgid+1)
        else:
            bot.reply_to(message, "ask query on polygon community group : @Polygon_test")
    except:
        bot.reply_to(message, "failed to send")

@bot.message_handler(func = lambda msg:'#replyid' in msg.text)
def send_setid(message):
    global msgid
    try:
        if message.from_user.id == 'here user id':
            msgtext= (message.text).lstrip('#replyid ')
            msgid = int(msgtext)
            bot.reply_to(message, "MessageId set for reply: " + str(msgid))
        else:
            bot.reply_to(message, "only admin have right to set messageId")
    except:
        bot.reply_to(message,"wrong input!! please try in right way #replyid <msgid>")

@bot.message_handler(func = lambda msg:'#reply' in msg.text)
def send_reply(message):
    global msgid
    if('#1' in message.text):
        groupid= 'here chat id'
        msgtext= (message.text).lstrip("#reply #1 ")
    elif('#2' in message.text):
        groupid= 'here chat id'
        msgtext= (message.text).lstrip("#reply #2 ")
    try:
        if message.from_user.id == 'here user id':
            global msgid
            replytext= "Reply from polygon team:\n\n" + msgtext
            bot.send_message(groupid,replytext,reply_to_message_id=msgid)
            bot.reply_to(message, "Reply sent, messageId: " + str(msgid))
        else:
            bot.reply_to(message, "only admin have right to reply")  
    except: 
        bot.reply_to(message, "Failed to reply!!")

@bot.message_handler(func=lambda msg: '/' in msg.text)
def repeat(message):
    bot.send_message(message.chat.id, "send right /commands")

bot.polling()

