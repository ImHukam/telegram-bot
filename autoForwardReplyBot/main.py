from ast import Try
from distutils.log import error
from operator import indexOf
from turtle import fd
import telebot
from telebot import types
 
API = 'BotFather API'
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
        if(message.chat.id == 'chat id' or message.chat.id == 'chat id'):
            msgid= message.message_id
            name= message.from_user.first_name + " " + message.from_user.last_name + " ( @" + message.from_user.username + " )"
            groupname= message.chat.title + " ( @" + message.chat.username +" )"
            msgtext= (message.text).replace('@Polygon_Support_TestBot','')

            msg= "\nUserInfo"+ "\nfrom: " + str(groupname) + "\nname: " + name + "\nmsgid: "+str(msgid)+"\ngroupid: " + str(message.chat.id)
            forward_msg= "Query: "+ msgtext + "\n" + msg
            bot.send_message('receiver group chat id', forward_msg)
            bot.reply_to(message,"Query sents to polygon team,wait for response!!")
            # time.sleep(5)
            # bot.delete_message(cid,msgid+1)
        else:
            bot.reply_to(message, "ask query on polygon community group : @Polygon_test")
    except:
        bot.reply_to(message, "failed to send")


@bot.message_handler(func=lambda msg: '' in  msg.text)
def send_reply_(message):
    try:
        if(message.reply_to_message and message.chat.id == 'chat id'):
            msg= message.reply_to_message.text

            # to get msgid from message
            msgIndex= msg.index('msgid')
            msgIndex=msgIndex+7
            msgid= str()
            while msg[msgIndex] != '\n':
                msgid= msgid+msg[msgIndex]
                msgIndex = msgIndex+1
        
            # to get groupid from message
            groupIndex = msg.index('groupid')
            groupIndex = groupIndex + 9
            groupId= str()
            while groupIndex<len(msg):
                groupId = groupId+msg[groupIndex]
                groupIndex = groupIndex +1

            replytext= "Reply from polygon team:\n\n" + message.text
            bot.send_message(groupId,replytext,reply_to_message_id=msgid)
            bot.reply_to(message, "Reply sent")
    except Exception as e:
        bot.reply_to(message, "Error: " + str(e))


@bot.message_handler(func=lambda msg: '/' in msg.text)
def repeat(message):
    bot.send_message(message.chat.id, "send right /commands")

bot.polling()

