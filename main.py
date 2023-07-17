from flask import Flask, render_template
myflaskapp = Flask(__name__)

@myflaskapp.route('/')
def hello_world():
  return render_template("index.html")

@myflaskapp.route('/python')
def python():
  return render_template("python.html")

@myflaskapp.route('/ios')
def ios():
  return render_template("ios.html")

@myflaskapp.route('/resume')
def resume():
  return render_template("resume.html") 

@myflaskapp.route('/android')
def android():
  return render_template("android.html")

if __name__ == "__main__":
    myflaskapp.run(host='0.0.0.0', port=8080)
