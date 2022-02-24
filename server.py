from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your mad your dogwater whats that your dogwater i told you i got EZ dubs too easy, cani get a sheesh sheesh"
  
def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()