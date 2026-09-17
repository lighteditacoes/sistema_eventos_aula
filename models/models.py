from database import db

class Evento(db.Model):
    id_evento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))
    descricao = db.Column(db.String(250))
    data = db.Column(db.String(10))
    local = db.Column(db.String(100))
    categoria = db.Column(db.String(30))
    quantidade_participantes = db.Column(db.Integer)