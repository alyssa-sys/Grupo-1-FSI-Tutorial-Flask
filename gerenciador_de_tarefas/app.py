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
