from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def hellow():
    return "Hellow World!"

app.run()