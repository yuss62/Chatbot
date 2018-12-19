# IMPORTS
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)
bot_id = "dac6f9fe24fe7ffa8ab566d96d"

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
	# 'message' is an object that represents a single GroupMe message.
	message = request.get_json()
	
	if 'iyah kenapa?' in message['text'].lower() and not sender_is_bot(message):
		reply('kamu kok udah beda yaa kak')
		
	elif 'beda apanya?' in message['text'].lower() and not sender_is_bot(message):
		reply('yah beda, kk udah gk hub aku lagi :(   kk udah punya yg baru yak?')
		
	elif 'Hmmm napa nanya gitu?' in message['text'].lower() and not sender_is_bot(message):
		reply('kak, ade udah g ada kesempatan lagi yaa?')
	
	elif 'kesempatan apa lagi dek?' in message['text'].lower() and not sender_is_bot(message):
		reply('yah, balik kyak dulu lagi :(')
	
	return "ok", 200
	
		
################################################################################

# Kirim Pesan ke grup
def reply(msg):
	url = 'https://api.groupme.com/v3/bots/post'
	data = {
		'bot_id'		: 'dac6f9fe24fe7ffa8ab566d96d',
		'text'			: msg
	}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

# Kirim pesan dengan gambar
def reply_with_image(msg, imgURL):
	url = 'https://api.groupme.com/v3/bots/post'
	urlOnGroupMeService = upload_image_to_groupme(imgURL)
	data = {
		'bot_id'		: dac6f9fe24fe7ffa8ab566d96d,
		'text'			: msg,
		'picture_url'		: urlOnGroupMeService
	}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()
	
# Upload gambar dan return URL
def upload_image_to_groupme(imgURL):
	imgRequest = requests.get(imgURL, stream=True)
	filename = 'temp.png'
	postImage = None
	if imgRequest.status_code == 200:
		# Save Gambar
		with open(filename, 'wb') as image:
			for chunk in imgRequest:
				image.write(chunk)
		# Send Gambar
		headers = {'content-type': 'application/json'}
		url = 'https://image.groupme.com/pictures'
		files = {'file': open(filename, 'rb')}
		payload = {'access_token': 'Brb6ldlszy4XejtdecLmthBxp0kw2BlzdwrxMQqX'}
		r = requests.post(url, files=files, params=payload)
		imageurl = r.json()['payload']['url']
		os.remove(filename)
		return imageurl

# Validasi pesan BOT
def sender_is_bot(message):
	return message['sender_type'] == "bot"
