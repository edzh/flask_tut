from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [ #array of fake posts
      {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
      },
      {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool!'
      }
    ]
    return render_template('index.html', user=user, posts=posts)
