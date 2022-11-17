from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_session import Session
from flask import send_from_directory,send_file
from flask_mysqldb import MySQL
from flask_bcrypt import check_password_hash
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
import hashlib
from dao_anp import *
from dao_user import *
from model import*
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "cimento1"
app.config['MYSQL_DB'] = "oleos"
app.config['MYSQL_PORT'] = 3306
app.secret_key = 'cimento1' #ela é essencial para deletar dados do banco
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = MySQL(app)
atividade_dao = DAO(db)
atividade_dao_user = DAO_USER(db)
