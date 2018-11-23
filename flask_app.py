# SWAMI KARUPASAMI THUNAI

from flask import Flask, render_template, request
import pusher

app = Flask(__name__)
pusher_client = pusher.Pusher(
      app_id='653385',
      key='35bb38e0c1fb3add1a93',
      secret='b4d5dd71f9e44d8b2770',
      cluster='ap2',
      ssl=True
    )

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/message', methods=['POST'])
def message():
    username = request.form.get('username')
    message = request.form.get('message')
    pusher_client.trigger('metabase', 'new-message', {'username': username, 'message': message})

@app.route('/newuser', methods=['POST'])
def newuser():
    username = request.form.get('username')
    pusher_client.trigger('metabase', 'new-user', {'username': username})

@app.route('/exituser', methods=['POST'])
def exituser():
    username = request.form.get('username')
    pusher_client.trigger('metabase', 'exit-user', {'username': username})
