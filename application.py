from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():

    phone_number = request.args.get('phone_number')

    return render_template(
        'index.html',
        phone_number=phone_number
    )


@app.route('/', methods=['POST'])
def send():

    phone_number = request.form.get('phone_number')

    return redirect(url_for(
        '.sent',
        phone_number=phone_number
    ))


@app.route('/sent/<phone_number>')
def sent(phone_number=''):

    result = 'Phone number is {}'.format(phone_number)

    return render_template(
        'sent.html',
        result=result
    )
