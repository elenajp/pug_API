import os

from flask import Flask, jsonify, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy

from database import result_list

sharks_folder = os.path.join('static', 'stuff')

app = Flask(__name__)
# this prevents a warning message when running the app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # this is the location of the database, can be local or remote
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['UPLOAD_FOLDER'] = sharks_folder
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/sharks', methods=['GET'])  # returns all the sharks in the db
def return_sharks():
    return jsonify({'result_list': result_list})


# returns all of one species type of shark
@app.route('/sharks/<string:species>', methods=['GET'])
def return_one(species):
    one_species = [
        specie for specie in result_list if specie['species'] == species]
    return jsonify({'specie': one_species[0]})


@app.route('/get_image')  # returns an image example on the home page
def get_image():
    filename = 'sharks/hammer1.jpg'
    return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
