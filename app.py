@echo off 
from flask import Flask, render_template, request, redirect, url_for 
 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 
 
@app.route('/contact', methods=['GET', 'POST']) 
def contact(): 
    if request.method == 'POST': 
        message = request.form['message'] 
        return render_template('contact.html', confirmation="Message received: " + message) 
    return render_template('contact.html') 
 
if __name__ == '__main__': 
    import os 
    port = int(os.environ.get("PORT", 8000)) 
    app.run(host="0.0.0.0", port=port, debug=True) 
