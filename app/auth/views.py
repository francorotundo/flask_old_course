from . import auth
from flask import redirect, render_template, request, session, url_for, flash
from app.forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito')
        
        return redirect(url_for('index'))
    
    return render_template('login.html', **context)