import os
from flask import Flask, request, redirect, url_for, render_template
from notifications_python_client.notifications import NotificationsAPIClient

notifications_client = NotificationsAPIClient(os.environ['NOTIFY_KEY'])
app = Flask(__name__)


DOCUMENT_PATHS = {
    'report': 'files/report.pdf',
    'project-proposal': 'files/project-proposal.pdf',
    'newsletter': 'files/newsletter.pdf',
    'research-paper': 'files/research-paper.txt',
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def send():

    email_address = request.form.get('email_address')
    document_key = request.form.get('document_key')

    with open('./files/' + document_key + '.pdf', 'rb') as f:
        response = notifications_client.send_email_notification(
            email_address=email_address,
            template_id='801c99bc-a70f-45c8-82d5-8263b9bf05bb',
            personalisation={
                'document': f,
            }
        )
        if 'status_code' in response:
            raise response

    return redirect(url_for(
        '.sent',
        email_address=email_address,
        document_key=document_key
    ))


@app.route('/sent')
def sent():

    email_address = request.args.get('email_address')
    document_key = request.args.get('document_key')

    result = 'Sent {} to {}'.format(DOCUMENT_PATHS[document_key], email_address)

    return render_template(
        'sent.html',
        result=result
    )
