from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def root():
        return "Hello Napier"




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
    #Chapter 7
    #HTML Templates using Jinja2
    