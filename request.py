from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def hello():
    #print the request to the terminal
    print ( request.method , request.path , request.form )
    return "Hello Napier2"

@app.route('/static-example/img')
def static_example_img():
    #print the request to the terminal
    print ( request.method , request.path , request.form )
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start + url + end, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)