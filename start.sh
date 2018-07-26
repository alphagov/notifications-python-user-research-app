pip install -r requirements.txt
export FLASK_APP=application.py
export FLASK_DEBUG=1

set -a
source .env
set +a
flask run
