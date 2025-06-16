from flask import Flask, make_response, redirect, render_template, request

app = Flask(
    __name__,
    template_folder='./templates', 
    static_folder='./static'
    )

todos = [f'TODO {i}' for i in range(1,5)]

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error= error)
@app.route('/hello', methods=["GET"])
def hello_world():
    user_ip = request.cookies.get('user_ip')
    context = {
        "user_ip":user_ip, 
        "todos":todos
    }
    return render_template('hello.html', **context)

@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    
    return response
    