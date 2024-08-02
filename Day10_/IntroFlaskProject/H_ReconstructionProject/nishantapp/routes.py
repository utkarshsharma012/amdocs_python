from flask import render_template,redirect,url_for
from nishantapp.forms import RegistrationForm
from nishantapp import app

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


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()# object of form
    if form.validate_on_submit():
        print(form.username.data,form.email.data,form.password.data)
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)
