from posts import get_all_post_names
# import Flask class from flask  package
from flask import Flask, render_template
# create an instance of Flask class by providing the application module as parameter
app = Flask(__name__)


@app.route('/')
def home():
    post_names = get_all_post_names()
    return render_template('index.html', post_names=post_names)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts/<string:post_name>')
def show_post(post_name):
    return render_template(f'posts/{post_name}')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404