from flask import Flask
app = Flask(__name__)

@app.route("/")

def say_hello():
    return "Hello from flask123123123"

if __name__ == "__main__":
    app.run(debug=True)

