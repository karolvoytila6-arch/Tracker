from datetime import datetime
import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Բեռնվում է...</title>
</head>
<body style="background-color: #121212; color: #ffffff; text-align: center; padding-top: 100px; font-family: sans-serif;">
    <h2>Բեռնվում է, խնդրում ենք սպասել...</h2>
    <p>Կայքը պատրաստվում է ցուցադրման:</p>
</body>
</html>
"""

@app.route("/")
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{time_now}] IP: {ip} | Device: {user_agent}\n--------------------------------------------------\n"
    print(log_entry)
    
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
