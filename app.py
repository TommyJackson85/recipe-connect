import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hell world .. again"

if __name__ == "__name__":
    app.run(host=os.getenv('IP'),
        port=int(os.getenv('PORT')),
        debug=True)
