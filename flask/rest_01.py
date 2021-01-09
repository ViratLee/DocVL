from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hi')
@app.route('/hello')
def hello():
    return 'Hello, World'
# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)