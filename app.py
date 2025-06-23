from flask import Flask, make_response, redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(
    __name__,
    template_folder='./templates', 
    static_folder='./static'
    )

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'MI CLAVE SECRETA'


todos = [f'TODO {i}' for i in range(1,5)]


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error= error)

@app.route('/hello', methods=["GET", "POST"])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')  
    
    context = {
        "user_ip":user_ip, 
        "todos":todos,
        "login_form": login_form,
        "username": username
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        return redirect(url_for('index'))

    return render_template('hello.html', **context)

@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    
    return response
    