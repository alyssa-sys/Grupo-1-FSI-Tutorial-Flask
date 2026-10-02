from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario, Tarefa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chaveMuitoMuitoSecreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gerenciador_de_tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
#login_manager.login_view = 'login'

#admin
@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash("Access denied", 'danger')
        return redirect(url_for('dashboard'))

    tarefas = Tarefa.query.all()
    return render_template('admin_dashboard.html', tarefas = tarefas)
    
#adicionar tarefa
@app.route('/adicionar_tarefa', methods=['GET', 'POST'])
@login_required
def adicionar_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        status = request.form['status']
        responsavel_id = request.form.get('responsavel_id', current_user.id) 

        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, status=status, criador_id=current_user.id, responsavel_id=responsavel_id)

        db.session.add(nova_tarefa)
        db.session.commit()

        flash('Tarefa adicionada com sucesso!', 'success')
        return redirect(url_for('index'))
    
    usuarios = Usuario.query.filter(Usuario.id != current_user.id).all()
    return render_template('adicionar_tarefa.html', usuarios=usuarios)


#editar tarefa
@app.route('/editar_tarefa/<int:tarefa_id>', methods=['GET', 'POST'])
@login_required
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    if current_user.id != tarefa.criador_id and current_user.id != tarefa.responsavel_id:
        flash('Você não tem permissão para editar esta tarefa.', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        tarefa.status = request.form['status']

        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('editar_tarefa.html', tarefa=tarefa)

#excluir tarefa
@app.route('/excluir_tarefa/<int:tarefa_id>')
@login_required
def excluir_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    if current_user.id != tarefa.criador_id and current_user.id != tarefa.responsavel_id:
        flash('Você não tem permissão para excluir esta tarefa.', 'danger')
        return redirect(url_for('index'))
    
    db.session.delete(tarefa)
    db.session.commit()

    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('index'))

