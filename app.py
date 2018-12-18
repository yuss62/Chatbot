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
	
	if 'info' in message['text'].lower() and not sender_is_bot(message):
		reply('ketik perintah-perintah berikut untuk info lebih lanjut "Nim dari 091-099": 1. "Nama#16xxx" 2. "alamat#16xxx" 3. "golongandarah#nimxxx"')
		
	elif 'nama#16097' in message['text'].lower() and not sender_is_bot(message):
		reply('Reyhan Todo')
		
	elif 'nama#16099' in message['text'].lower() and not sender_is_bot(message):
		reply('Revo daniswara')
		
	elif 'nama#16091' in message['text'].lower() and not sender_is_bot(message):
		reply('Oka Wisnu')
		
	elif 'nama#16092' in message['text'].lower() and not sender_is_bot(message):
		reply('Andika verdiana')
		
	elif 'nama#16093' in message['text'].lower() and not sender_is_bot(message):
		reply('Kevin Bakkara')
	
	elif 'nama#16094' in message['text'].lower() and not sender_is_bot(message):
		reply('Dode Yoga')
		
	elif 'nama#16095' in message['text'].lower() and not sender_is_bot(message):
		reply('Veniiy Tallo')
		
	elif 'nama#16096' in message['text'].lower() and not sender_is_bot(message):
		reply('Shereen delia')
		
	elif 'alamat#16097' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. sudirman')
		
	elif 'alamat#16092' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. jati negara')
	
	elif 'alamat#16091' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. Pulau Moyo')
	
	elif 'alamat#16093' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. nuansa udayana')
		
	elif 'alamat#16094' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. benjamin')
		
	elif 'alamat#16095' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. terang bulan')
		
	elif 'alamat#16096' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. pamulang')
		
	elif 'alamat#16098' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. nandena')
	
	elif 'alamat#16099' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. melati')
	
	elif 'alamat#16097' in message['text'].lower() and not sender_is_bot(message):
		reply('Jl. merpati')
	
	elif 'Golongandarah#16091' in message['text'].lower() and not sender_is_bot(message):
		reply('AB')
	
	elif 'golongandarah#16097' in message['text'].lower() and not sender_is_bot(message):
		reply('A')
		
	elif 'golongandarah#16092' in message['text'].lower() and not sender_is_bot(message):
		reply('A')
		
	elif 'golongandarah#16093' in message['text'].lower() and not sender_is_bot(message):
		reply('B')
		
	elif 'golongandarah#16094' in message['text'].lower() and not sender_is_bot(message):
		reply('B')
		
	elif 'golongandarah#16095' in message['text'].lower() and not sender_is_bot(message):
		reply('O')
		
	elif 'golongandarah#16096' in message['text'].lower() and not sender_is_bot(message):
		reply('A')
		
	elif 'golongandarah#16098' in message['text'].lower() and not sender_is_bot(message):
		reply('AB')
	
	elif 'golongandarah#16099' in message['text'].lower() and not sender_is_bot(message):
		reply('O')
	
	elif 'golongandarah#16097' in message['text'].lower() and not sender_is_bot(message):
		reply('B')
	
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
