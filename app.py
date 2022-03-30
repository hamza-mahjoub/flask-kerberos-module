#!/usr/bin/env python3
 
from flask import Flask, render_template, request, Response
from flask_kerberos import init_kerberos
from flask_kerberos import requires_authentication
from flask_bootstrap import Bootstrap

import os

DEBUG=True

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/home')
@requires_authentication
def home(user):
  concaten = ""
  liste = []
  for parent, dnames, fnames in os.walk("files/"):
    for fname in fnames:
      filename = os.path.join(parent, fname)
      liste.append(filename)   
  return render_template('fichiers.html', liste=liste, user=user)


@app.route('/<path:path>')
@requires_authentication
def get_file(user,path,*args, **kwargs):
  contenu = []
  with open(path) as f:
    for line in f:
      contenu.append(line)
  return render_template('contenu.html', contenu=contenu, user=user) 

@app.route('/addline/<path:path>',methods=['POST'])
@requires_authentication
def add_line(user,path,*args, **kwargs):
  data = request.json
  print(data)
  contenu = []
  f = open(path,"r+")
  for line in f:
     contenu.append(line)
  for obj in data:
     f.write(obj['message']+'\n')
     contenu.append(obj['message']+'\n')
  return render_template('contenu.html', contenu=contenu, user=user) 
 
@app.route('/deleteline/<path:path>',methods=['POST'])
@requires_authentication
def delete_line(user,path,*args, **kwargs):
  data = request.json
  contenu = []
  with open(path,"r") as f:
    for line in f:
      contenu.append(line)
   
  if (data['line'] < 0 or data['line'] >= len(contenu)):
    return Response("precondition failed: can't delete this line !!!", status=412)
 
  with open(path,"w") as f:
      i = 0
      for line in contenu:
        if i != data['line']:
           f.write(line)
        i = i+1
  contenu = []
  with open(path,"r") as f:
    for line in f:
      contenu.append(line)
  return render_template('contenu.html', contenu=contenu, user=user) 

@app.route('/test/home')
def test_home():
  user = "hamza"
  concaten = ""
  liste = []
  for parent, dnames, fnames in os.walk("files/"):
    for fname in fnames:
      filename = os.path.join(parent, fname)
      liste.append(filename)   
  return render_template('fichiers.html', liste=liste, user=user)
  
@app.route('/test/<path:path>')
def test_get_file(path,*args, **kwargs):
  user = "hamza"
  contenu = []
  with open(path) as f:
    for line in f:
      contenu.append(line)
  return render_template('contenu.html', contenu=contenu, user=user) 

if __name__ == '__main__':
	init_kerberos(app,service='host',hostname='server.example.tn')
	app.run(host='0.0.0.0',port=8080)
