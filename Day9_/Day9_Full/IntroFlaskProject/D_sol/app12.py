from flask import Flask,render_template

app=Flask(__name__)#wsgi_app_object=Flask('modulename')

# url
@app.route('/')
@app.route('/home')
def home():
    posts = [{
    'author': 'Nishant',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 26, 2022'
    },
    {'author': 'Dr Wu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 27, 2022' }
]
    return render_template('home.html',posts=posts,title='Home')

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
