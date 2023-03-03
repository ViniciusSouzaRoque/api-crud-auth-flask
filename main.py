from flask import Flask

from view.project import project_bp
from view.tasks import task_bp
from view.team import team_bp
from view.user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(team_bp, url_prefix="/team")
app.register_blueprint(project_bp, url_prefix="/project")
app.register_blueprint(task_bp, url_prefix="/task")


@app.route("/")
def home():
    return "<p>Home page</p>"


if __name__ == "__main__":
    app.run(debug=True)
