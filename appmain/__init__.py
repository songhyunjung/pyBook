import flask
from flask_mail import Mail

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = 'a4826dedcb1e8e0e012bba1b256d74cb'

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'YOUR_ACCOUNT'
app.config["MAIL_PASSWORD"] = 'YOUR_PASSWORD'

mail = Mail(app)

from appmain.routes import main
app.register_blueprint(main)

from appmain.user.routes import user
app.register_blueprint(user)

from appmain.article.routes import article
app.register_blueprint(article)