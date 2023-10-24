from flask import Flask
import configparser

app = Flask(__name__)

def init(app):
    config = configparser.ConfigParser()
    try:
        print("INIT FUNCTION")
        config_location = "etc/defaults.cfg"
        config.read(config_location)
        
        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
        
    except Exception as e:
        print ("Could not read configs from: ", config_location)
        print ("Error details: ", e)

@app.route('/')
def root():
    return "Hello Napier from the configuration testing app"

@app.route('/config/')
def config():
    s = []
    s.append('debug:' + str(app.config['DEBUG']))
    s.append('port:' + str(app.config['port']))
    s.append('url:' + str(app.config['url']))
    s.append('ip_address:' + str(app.config['ip_address']))
    
    return ', '.join(s)

if __name__ == '__main__':
    init(app)
    app.run(
        host=app.config['ip_address'], 
        port=int(app.config['port'])
    )
