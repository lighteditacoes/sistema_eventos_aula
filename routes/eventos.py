from flask import Blueprint, render_template, url_for, redirect, request
from models.models import Evento
from database import db
from datetime import datetime

eventos_bp = Blueprint("eventos", __name__)

@eventos_bp.route('/')
def home():
    data = datetime.now().date()
    print(data)
    lista_eventos = Evento.query.where(Evento.data >= data).order_by(Evento.data).limit(3).all()
    return render_template("index.html", lista_eventos=lista_eventos)

@eventos_bp.route('/eventos')
def lista_eventos():
    lista_eventos = Evento.query.order_by(Evento.data.desc()).all()
    return render_template("eventos.html", lista_eventos=lista_eventos)

@eventos_bp.route('/cadastrar', methods=["GET", "POST"])
def cadastrar_evento():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        data = request.form["data"]
        local = request.form["local"]
        categoria = request.form["categoria"]
        quantidade_participantes = request.form["participantes"]

        erro = []

        if not nome or not descricao or not data or not local or not categoria or quantidade_participantes is None:
            erro.append("Todos os campos devem ser preenchidos.")
        else:
            if len(nome) < 6 or len(nome) > 60:
                erro.append("Nome deve ter entre 6 e 60 caracteres.")

            if len(descricao) > 250:
                erro.append("A descrição deve ter no máximo 250 caracteres.")

            if len(data) != 10:
                erro.append("A data deve ter exatamente 10 caracteres.")

            if len(local) > 100:
                erro.append("O local deve ter no máximo 100 caracteres.")

            if len(categoria) < 3 or len(categoria) > 30:
                erro.append("A categoria deve ter entre 3 e 30 caracteres.")

            try:
                qtd = int(quantidade_participantes)
                if qtd < 0:
                    erro.append("A quantidade de participantes não pode ser negativa.")
            except (ValueError, TypeError):
                erro.append("A quantidade de participantes deve ser um número inteiro válido.")

        if erro:
            formulario=request.form
            print(formulario)
            return render_template("cadastro.html", erro=erro, formulario=request.form)

        evento = Evento(nome=nome, descricao=descricao, data=data,
                        local=local, categoria=categoria,
                        quantidade_participantes=quantidade_participantes)

        db.session.add(evento)
        db.session.commit()

        return redirect(url_for("eventos.home"))

    return render_template("cadastro.html")

@eventos_bp.route('/evento/<int:id>')
def detalhes_evento(id):
    evento = Evento.query.get(id)
    return render_template("detalhe.html", evento=evento)

@eventos_bp.route('/editar/<int:id>', methods=["GET", "POST"])
def editar_evento(id):
    evento = Evento.query.get(id)
    if request.method == "POST":
        evento.nome = request.form["nome"]
        evento.descricao = request.form["descricao"]
        evento.data = request.form["data"]
        evento.local = request.form["local"]
        evento.categoria = request.form["categoria"]
        evento.quantidade_participantes = request.form["participantes"]

        db.session.commit()
        return redirect(url_for('eventos.detalhes_evento', id=evento.id_evento))
    return render_template("editar.html", evento=evento)

@eventos_bp.route('/excluir/<int:id>', methods=["GET", "POST"])
def excluir_evento(id):
    evento = Evento.query.get(id)
    if request.method == "POST":

        db.session.delete(evento)
        db.session.commit()

        return redirect(url_for('eventos.home'))
    return render_template("index.html")