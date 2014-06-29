import os
from .app import app, login_manager
from .models import Post, User
from flask import render_template, send_from_directory, redirect, request, flash
from flask.ext.mongoengine.wtf import model_form
from flask.ext.scrypt import generate_random_salt, generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(email):
    return User.objects.first(email)

@app.context_processor
def instance_things():
    return dict(isinstance=isinstance, tuple=tuple, list=list)


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


@app.route("/about")
def about_me():
    post = Post.objects.get_or_404(slug="about_me")
    return render_template("show_post.html", post=post)


@app.route("/login", methods=('GET', 'POST'))
def login():
    form = model_form(User, exclude=("salt", "email"))(request.form)  # <- two hours wasted right here!
    if form.validate_on_submit():
        try:
            user = User.objects.get(username=form.username.data)
        except User.DoesNotExist as e:
            flash(("Login Error", "User not found or wrong password"), "danger")
        except User.MultipleObjectsReturned as e:
            flash(("DB Error", str(e)), "danger")
        else:
            password = form.password.data
            if check_password_hash(password, user.password.encode(), user.salt.encode()):
                flash("You are now logged in", "success")
                return redirect('/')
            else:
                flash(("Login Error", "User not found or wrong password"), "danger")
    if form.errors:
        flash(form.errors, "danger")
    form.password.data=""
    return render_template("login.html", form=form)
