from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Your Full Name"  # Replace with your full name
    username = getpass.getuser()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Run `top` command
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: {name}
    user: {username}
    Server Time (IST): {ist_time}
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
