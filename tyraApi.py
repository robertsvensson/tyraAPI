from flask import Flask, request
from flask_restful import Resource, Api, abort
import time

app = Flask(__name__)
api = Api(app)

def getDate():
    timestamp = time.strftime("%H:%M:%S")
    return timestamp

def hello():
    return 'greetings professor Falken. How about a nice game of chess?'
    #https://youtu.be/D-9l5jSDL50

def getIceCreamForCurrentAuthLevel(authLevel):
    authLevel = int(authLevel)
    if authLevel is 1:
        return 'Chocolate'
    elif authLevel is 2:
        return 'Vanilla'
    else:
        return 'Strawberry'

def getServerResponseJSON(username,authLevel):
    timestamp = getDate()
    icecream = getIceCreamForCurrentAuthLevel(authLevel)
    return {'username':username,'authLevel':authLevel,'responseTime':timestamp,'iceCream':icecream}

def errorMessage():
    abort(404, message="{'Error':'In correct request'}")

class DefaultResponse(Resource):

    def get(self):
        username = request.args.get('username')
        authLevel = request.args.get('authLevel')
        if username is None:
            return errorMessage()
        elif authLevel is None:
            return errorMessage()
        else:
            return getServerResponseJSON(username,authLevel)

api.add_resource(DefaultResponse, '/')

if __name__ == '__main__':
    app.run(debug=True)
