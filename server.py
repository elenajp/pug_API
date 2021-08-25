from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from database import result_list

app = Flask(__name__)
# this prevents a warning message when running the app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # this is the location of the database, can be local or remote
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('index.html')


# @app.route('/<string:page_name>/')
# def render_static(page_name):
#     return render_template('%s.html' % page_name)


@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/docs")
# def docs():
 #    return render_template('docs.html')


@app.route('/sharks', methods=['GET'])
def return_sharks():
    return jsonify({'result_list': result_list})


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
