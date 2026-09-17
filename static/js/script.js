function cadastrar(event) {
    event.preventDefault();

    alert("Evento cadastrado com sucesso!");
    {{ url_for('eventos.cadastrar_evento') }}

    event.target.reset();
}

function editar(event) {
    event.preventDefault();

    alert("Evento atualizado com sucesso!");
}

function excluir() {
    const confirmar = confirm(
        "Deseja realmente excluir este evento?"
    );

    if (confirmar) {
        alert("Evento excluído com sucesso!");
    }
}