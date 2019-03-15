import psutil
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True
#PROCNAME = "Spotify"

@app.route('/kill/<pname>')
def kill(pname):
    for proc in psutil.process_iter():
        if proc.name() == pname:
            proc.kill()
            print("done")
    return jsonify("process killed: "+pname)

app.run(host='0.0.0.0', port=8080)
