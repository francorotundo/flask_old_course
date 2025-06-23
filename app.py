from flask import Flask, make_response, redirect, render_template, request, session
from flask_bootstrap import Bootstrap

app = Flask(
    __name__,
    template_folder='./templates', 
    static_folder='./static'
    )

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'MI CLAVE SECRETA'


todos = [f'TODO {i}' for i in range(1,5)]

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error= error)
@app.route('/hello', methods=["GET"])
def hello_world():
    user_ip = session.get('user_ip')
    
    context = {
        "user_ip":user_ip, 
        "todos":todos
    }
    return render_template('hello.html', **context)

@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    
    return response
    