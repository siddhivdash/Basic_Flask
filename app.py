from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")  #the route helps to reach out the particular function,/ or anyname we can give to the route
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/Hello_world1")  
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/Hello_world2")  
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    return "this is my function to run app"

@app.route("/test2")
def test2():
    data = request.args.get('x') #it asks to pass the argument only then we can access the route
    return "this is a data input from my url {}".format(data)
#x is the key and {} is the space for the key, if we have not enterend the key
#it will show NONE, Otherwise the valid keyword to enter the key is /test2?x=sidd
#in this way we can give our own input


if __name__=="__main__":
    app.run(host="0.0.0.0")

#Here we are implementing REST service, as... we are implementing html as well as we are using python to execute 
#Single / means home route, if more functions then give names to it

