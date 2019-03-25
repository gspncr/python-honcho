import psutil
from flask import Flask, jsonify, request
import subprocess
import time
import urllib

app = Flask(__name__)
app.debug = True
#PROCNAME = "Spotify"

@app.route('/processes')
def procsByName():
    listOfProcObjects = []

    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['virtual-memory'] = proc.memory_info().vms / (1024 * 1024)
           pinfo['stop-command'] = request.url_root+'kill/'+pinfo['name']
           pinfo['start-command'] = request.url_root+'startExperimental/'+pinfo['name']
           pinfo['restart-command'] = request.url_root+'bounce/'+pinfo['name']
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['virtual-memory'], reverse=True)
    return jsonify(listOfProcObjects)

@app.route('/startExperimental/<pname>')
def startExperimental(pname):
    try:
        subprocess.call([pname])
    except Exception:
        pass
    try:
        subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/"+pname+".app"])
    except Exception:
        pass
    return jsonify("process started: "+pname)

@app.route('/kill/<pname>')
def kill(pname):
    for proc in psutil.process_iter():
        if proc.name() == pname:
            proc.kill()
            print("done")
    return jsonify("process killed: "+pname)

@app.route('/mac/bounce/<pname>')
def macBounce(pname):
    for proc in psutil.process_iter():
        if proc.name() == pname:
            proc.kill()
    #subprocess.run(["Spotify"])
    time.sleep(5)
    subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/"+pname+".app"])
    return jsonify("process bounced: "+pname)

@app.route('/bounce/<pname>')
def bounce(pname):
    try:
        for proc in psutil.process_iter():
            if proc.name() == pname:
                proc.kill()
        #subprocess.run(["Spotify"])
        time.sleep(5)
        subprocess.call([pname])
    except Exception:
        pass
    try:
        for proc in psutil.process_iter():
            if proc.name() == pname:
                proc.kill()
        #subprocess.run(["Spotify"])
        time.sleep(5)
        subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/"+pname+".app"])
    except Exception:
        pass
    return jsonify("process bounced: "+pname)

@app.route('/start/<pname>')
def start(pname):
    subprocess.call([pname])
    return jsonify("process started: "+pname)

@app.route('/mac/start/<pname>')
def macStart(pname):
    subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/"+pname+".app"])
    return jsonify("process started: "+pname)

app.run(host='0.0.0.0', port=8080)
