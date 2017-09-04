from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


form_fields = [
    ('Name', 'name'),
    ('Street address', 'street_address'),
    ('Town', 'town'),
    ('County', 'county'),
    ('Postcode', 'postcode'),
]

form_field_names = [field_name for label, field_name in form_fields]

@app.route('/')
def index():

    return render_template(
        'index.html',
        form_fields=form_fields
    )


@app.route('/', methods=['POST'])
def send():

    result = {
        field_name: request.form.get(field_name)
        for field_name in form_field_names
    }

    return redirect(url_for(
        '.sent',
        **result
    ))


@app.route('/sent')
def sent():

    result = [
        '{}: {}'.format(field_name, request.args.get(field_name, ''))
        for field_name in form_field_names
    ]

    return render_template(
        'sent.html',
        result=result
    )
