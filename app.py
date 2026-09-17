from flask import Flask, render_template, url_for, redirect, request
from database import db
from models.models import Evento
from routes.eventos import eventos_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

app.register_blueprint(eventos_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)