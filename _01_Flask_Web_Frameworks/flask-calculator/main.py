import os

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# os.urandom to generate key
app.secret_key = b'\x16\x85\x9b\x14t\xc53\x0c\x03\xa3\xe6\xf7\xb2A\xa4\xdf\x91\xc8\x9c\x01Du\xc8>'


@app.route('/add', methods=['GET', 'POST'])
def add():
    # session['total']
    if 'total' not in session:
        session['total'] = 0
    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number
    return render_template('add.jinja2', session=session)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host='0.0.0.0', port=port, debug=True)
