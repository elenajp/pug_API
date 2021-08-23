from flask import Flask, jsonify, render_template, request

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


# @app.route("/about")
# def about():
#     return render_template('about.html')


# @app.route("/docs")
# def docs():
 #    return render_template('docs.html')

@app.route('/upload', method=['POST'])
def upload():
    image = request.files['image']
    if not image:
        return 'no image uploaded', 400


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
