import flask
from flask_mail import Mail

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = '99a2726256c1239da4dfe613e0dbf61a'

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