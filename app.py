from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "kjGHg%$$#GHCHFDGFBSM"
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template("session.html")

def messgate_recieved():
    print("Message was received!")

@socketio.on("my event")
def handle_my_custom_event(json, methods=["GET", "POST"]):
    print("received my event" + str(json))
    socketio.emit("my response", json, callback=messgate_recieved)

if __name__ == '__main__':
    socketio.run(app, debug=True)
