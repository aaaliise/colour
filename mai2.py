from flask import Flask, render_template


app = Flask(__name__)


@app.route('/table/<pl>/<age>')
def table(pl, age):
    return render_template('table.html', pl=pl, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')