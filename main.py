from flask import Flask

from view.user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/user')


@app.route("/")
def home():
    return "<p>Home page</p>"


if __name__ == "__main__":
    app.run(debug=True)
