from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
