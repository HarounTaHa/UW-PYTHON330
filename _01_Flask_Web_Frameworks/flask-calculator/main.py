import base64
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from model import SavedTotal

app = Flask(__name__)
# os.urandom to generate key
# app.secret_key = b'\x16\x85\x9b\x14t\xc53\x0c\x03\xa3\xe6\xf7\xb2A\xa4\xdf\x91\xc8\x9c\x01Du\xc8>'

# Load .env
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/add', methods=['GET', 'POST'])
def add():
    # session['total']
    if 'total' not in session:
        session['total'] = 0
    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number
    return render_template('add.jinja2', session=session)


@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")
    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()
    return render_template('save.jinja2', code=code)


@app.route('/retrieve')
def retrieve():
    code = request.args.get("code", None)

    if code is None:
        return render_template('retrieve.jinja2')
    else:
        try:
            saved_total = SavedTotal.get(SavedTotal.code == code)
        except SavedTotal.DoesNotExist:
            return render_template('retrieve.jinja2', error="Code not dound")
        session['total'] = saved_total.value
        return redirect(url_for('add'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host='0.0.0.0', port=port, debug=True)
