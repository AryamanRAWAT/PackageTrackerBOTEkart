import traceback
from django.shortcuts import render
import json
from Bot.cred import *
import telegram
from telegram import InputFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Bot.models import UserInfo
from Bot import track_send
# Create your views here.

global Bot 
global TOKEN
TOKEN = bot_token
Bot = telegram.Bot(token=TOKEN)
@csrf_exempt
def home(request):
    try:
        body = json.loads(request.body)
        print(body)

        # sticker_file_id = '108412073.tgs'
        # sticker_info = Bot.get_file(file_id=sticker_file_id)
        # file_identifier = sticker_info.file_id
        
        reply_text = f"Hi {body.get('message').get('from').get('first_name')}!\n<b>Welcome to OrderTrackingBoB!</b>\n\nTo track your package, please include <b>track</b> in your message and end the message with the tracking id provided by <b>Ekart</b>.\nFor example: <b>hello track 'tracking id'</b>.\n\n For listing of your history type <b>/history</b>.\n\n For deleting a particular entry type <b>delete</b>.\n\n To delete your entire history type <b>/del_all.</b>"
        user_text = body.get('message').get('text')
        chat_id = body.get('message').get('from').get('id')
        m_reply_id = body.get('message').get('message_id')

        lst = user_text.split(' ')
        tracking_id = lst[-1]
        
        if 'track' in user_text.lower():
        
            user_obj = UserInfo(
                chat_id = chat_id,
                first_name = body.get('message').get('from').get('first_name'),
                last_name = body.get('message').get('from').get('last_name'),
                tracking_id = tracking_id
            )
            try:
                user_obj.save()
                

            except:
                reply_text = 'You are already subscribed to this tracking id!'
                # sticker_file_id = 'no_no_pika.tgs'
        # if '/start' in user_text.lower():
            reply_text = track_send.processed_data(tracking_id)

        if 'history' in user_text.lower():
            chat_id = chat_id
            reply_text = track_send.get_history(chat_id)

        if '/delete' in user_text.lower():
            try:
                entry_to_be_del = int(user_text[-1]) - 1
                chat_id = chat_id
                if not entry_to_be_del < 0:    
                    reply_text = track_send.del_history(chat_id, entry_to_be_del)
                else:
                    reply_text = 'Invalid input.\nPlease provide a number listed in the history.'
            except ValueError:
                reply_text = 'Invalid input.\nPlease provide an integer at the end of the \delete command.'

        if '/del_all' in user_text.lower():
            chat_id = chat_id
            reply_text = track_send.del_all(chat_id)

        print('----------->',reply_text)
        # Bot.send_sticker(chat_id=chat_id, sticker=InputFile(file_identifier))
        Bot.send_message(chat_id=chat_id, text=reply_text, reply_to_message_id=m_reply_id, parse_mode=telegram.ParseMode.HTML)

    except:    
        print(traceback.format_exc())
        # sticker_file_id = 'shocked_pika.tgs'
        # sticker_info = Bot.get_file(file_id=sticker_file_id)
        # file_identifier = sticker_info.file_id
        # Bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)
        Bot.send_message(chat_id=chat_id, text='error')
        

    return HttpResponse('hi')
    


def set_webhook(request):
   s = Bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   print(s)
   if s:
       return HttpResponse("webhook setup ok")
   else:
       return HttpResponse("webhook setup failed")