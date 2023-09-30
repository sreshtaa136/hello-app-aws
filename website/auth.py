from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import dynamo_db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

# defining routes
@auth.route('/', methods=['GET', 'POST'])
def login():

    if (request.method == 'POST'):

        email = request.form.get('email')           
        password = request.form.get('password')
        curr_user = dynamo_db.get_user(email)

        if (curr_user != None):
            if check_password_hash(curr_user.password, password):
                # taking user to home page
                return redirect(url_for('views.home', user=email))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    
        return render_template("login.html") 

    return render_template("login.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if (request.method == 'POST'):  

        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = dynamo_db.get_user(email)

        if (user != None):
            flash('Email already exists.', category='error')
        elif(len(email) < 6 and ('@' not in email) and (".com" not in email)):
            flash('Email must be valid', category='error')
        elif(len(firstName) < 2):
            flash('Firstname must be at least 2 characters long', category='error')
        elif(len(password1) < 8):
            flash('Password must be at least 8 characters long', category='error')
        elif(password1 != password2):
            flash('Your passwords donot match! Try again', category='error')
        else:
            password = generate_password_hash(password1, method='sha256')
            dynamo_db.create_user_item(email, firstName, password)
            # taking user to home page
            return redirect(url_for('views.home', user=email))
            
        return render_template("sign_up.html")

    return render_template("sign_up.html")


@auth.route('/logout')
def logout():
    # taking user to login page
    return redirect(url_for('auth.login'))
    