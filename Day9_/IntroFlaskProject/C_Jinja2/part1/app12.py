from flask import Flask,render_template

app=Flask(__name__)#wsgi_app_object=Flask('modulename')

# url
@app.route('/')
@app.route('/home')
def home():
    fruits=["Apple",'Mango','Banana1','Grape']# List
    return render_template('home.html',fruits=fruits,title='Home')

#http://127.0.0.1:5000/about
#render the html page from about and invalid_url method's ?
@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.errorhandler(404)
def invalid_url(e):
    return render_template('404.html',title='Invalid')

if __name__ == '__main__':
    app.run(debug=True)
