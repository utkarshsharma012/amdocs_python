from flask import Flask

app=Flask(__name__)#wsgi_app_object=Flask('modulename')

# url
@app.route('/')
@app.route('/home')
def home():
    return "This is home Page!"

#http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return '<h1>This is about page!</h1>'

@app.errorhandler(404)
def invalid_url(e):
    return "<em>This is Invalid URL!</em>"

if __name__ == '__main__':
    app.run(debug=True)
