import os
from .app import app, login_manager
from .models import Post, User
from flask import render_template, send_from_directory


@login_manager.user_loader
def load_user(email):
    return User.objects.first(email)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/")
def blog():
    posts = Post.objects.all()
    return render_template("blog.html", posts=posts)


@app.route("/post/<slug>")
def show_post(slug):
    post = Post.objects.get_or_404(slug=slug)
    return render_template("show_post.html", post=post)


@app.route("/login")
def login():
    return render_template("login.html")
