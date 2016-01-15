from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_view("index.html", phrase="Hello", times=5)
app.run(debug=True)
@app.route('/base')
def base('/base):
  return render_app("base.html", phrase="Hello", times=5)
app.run(debug=True)
@app.route('/admin')
def admin('/admin):
  return render_app("base.html", phrase="Hello", times=5)
app.run(debug=True)