from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
# Blueprint = way to organise files
from website.models import User 
from .models import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        rollno = request.form.get('rollno')
        password = request.form.get('password')
        
        user = User.query.filter_by(rollno = rollno).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully !!', category='success')
                login_user(user, remember=True) # remember user untill he clears his browsing history or clears his session, or the server stops
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, Try again !!', category='error')
        else:
            flash('Roll No. isn\'t registered !! Need to signup.', category='error')
                
        
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    # print("inside Sign-up---------------------")
    if request.method == 'POST':
        form = request.form
        rollno = form.get('rollno')
        name = form.get('name')
        phoneno = form.get('phoneno')
        password1 = form.get('password1')
        password2 = form.get('password2')

        user = User.query.filter_by(rollno = rollno).first()
        
        if user:
            flash('This Roll Number already exists. Can\'t sign in', category='error')
        elif len(rollno) < 4:
            flash('The Roll No. length should be greater than 3', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(phoneno)!=10:
            flash(f'Phone No. can\'t be of {len(phoneno)} digits. It should contain 10 digits.', category='error')
        else:
            new_user = User(rollno = rollno, name = name, phoneno = phoneno, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category='success')
            # login_user(new_user, remember=True)
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user = current_user)