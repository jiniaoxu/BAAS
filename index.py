from flask import Flask
from Auth.AuthMiddleware import AuthMiddleware

from Routes.Auth.login import login
from Routes.Auth.signup import signup
from Routes.insert import insert
from Routes.update import update
from Routes.updateById import updateByID



app=Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

@app.route('/')
def index():
	return 'hello'

app.route('/login', methods=['GET', 'POST'])(login)
app.route('/signup', methods=['GET', 'POST'])(signup)
app.route('/insert', methods=['PUT'])(insert)
app.route('/update', methods=['PATCH'])(update)
app.route('/insert', methods=['PATCH'])(updateByID)


app.run(host='localhost',debug=True)