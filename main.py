from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/python')
def python():
  return render_template("python.html")

@app.route('/ios')
def ios():
  return render_template("ios.html")

@app.route('/resume')
def resume():
  return render_template("resume.html") 

@app.route('/android')
def android():
  return render_template("android.html")

app.run(host='0.0.0.0', port=8080)
