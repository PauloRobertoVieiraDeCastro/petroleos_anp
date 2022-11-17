from config import *
 
@app.route("/")
def sessao():
    if not session.get("nome"):
        return redirect("/login")
    lista = atividade_dao.listar()
    flash("Seja bem-vindo(a)")
    return render_template("index.html",lista=lista)

@app.route('/deletar/<string:ide>')
def deletar(ide):
    atividade_dao.apagar(ide)
    flash("A tarefa foi removida com sucesso")
    return redirect(url_for('sessao'))

@app.route('/criar', methods=['POST',])
def criar():
    corrente = request.form['corrente']
    tipo = request.form['tipo']
    bacia = request.form['bacia']
    api = request.form['API']
    nafta = request.form['nafta']
    medio = request.form['medio']
    residuo = request.form['residuo']
    lista = ANP(corrente,tipo,bacia,api,nafta,medio,residuo)
    atividade_dao.salvar(lista)
    return redirect(url_for('sessao'))

@app.route('/inserir')
def inserir():
    if not session.get("nome"):
        return redirect("/login")
    return render_template("inserir.html")

@app.route('/atualizar/<int:ide>')
def atualizar(ide):
    lista = atividade_dao.busca_por_id(ide)
    return render_template("atualizar.html",lista=lista)

@app.route('/editar', methods=['POST',])
def editar():
    corrente = request.form['corrente']
    tipo = request.form['tipo']
    bacia = request.form['bacia']
    api = request.form['API']
    nafta = request.form['nafta']
    medio = request.form['medio']
    residuo = request.form['residuo']
    lista = ANP(corrente,tipo,bacia,api,nafta,medio,residuo,ide=request.form['ide'])
    atividade_dao.salvar(lista)
    return redirect(url_for('sessao'))

@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    if not session.get("nome"):
        return redirect("/login")
    lista_count = atividade_dao.contagem()[0][0]
    pesado = atividade_dao.min_api()[0][0]
    leve = atividade_dao.max_api()[0][0]
    quant = atividade_dao.qtd_pet()
    df1 = pd.DataFrame(quant)
    df1.columns = ['Tipo','Quantidade']

    bacia = atividade_dao.qtd_bacia()
    df2 = pd.DataFrame(bacia)
    df2.columns = ['Bacia','Quantidade']
    df2 = df2.head()

    carac = atividade_dao.caract_tipo()
    df3 = pd.DataFrame(carac)
    df3.columns = ['Tipo','Média %Nafta','Média %Diesel','Média %Resíduos']

    carac_bacia = atividade_dao.caract_bacia()
    df4 = pd.DataFrame(carac_bacia)
    df4.columns = ['Bacia','Média %Nafta','Média %Diesel','Média %Resíduos']
    
    
    config = {'responsive': True}
    fig1 = px.pie(df1, values="Quantidade", names="Tipo", title='Proporção de tipos nas correntes')
    fig2 = px.bar(df2, y='Quantidade', x='Bacia',title="Bacias com maior número de correntes")
    fig3 = px.histogram(df3,x='Tipo',y=['Média %Nafta','Média %Diesel','Média %Resíduos'],barmode='group', text_auto='.1f',title='Perfil de destilados por tipo')
    fig4 = px.histogram(df4,x='Bacia',y=['Média %Nafta','Média %Diesel','Média %Resíduos'],barmode='group', text_auto='.1f',title='Perfil de destilados por bacia')
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("dashboard.html",lista_count = lista_count,pesado = pesado, leve = leve,
                           graphJSON = [graphJSON1, graphJSON2, graphJSON3,graphJSON4])

@app.errorhandler(404)
def not_found(e):  
# defining function
    return render_template("404.html")

#-----------------------logando------------------------------------------------------

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    session.pop('name')
    session.clear()
    return redirect(url_for("login"))

@app.route("/autenticar", methods=['POST',])
def autenticar():
    s = atividade_dao_user.usuario(request.form['nome'])
    if(len(s)==0):
        flash("Usuário e\ou senha incorreto(s)")
        return redirect(url_for("login"))
    else:
        senha = hashlib.md5(request.form['senha1'].encode()).hexdigest() #senha criptografada do usuario
        name,passwords = s[0] #consulta bem sucedida ao banco
        passwords = hashlib.md5(passwords.encode()).hexdigest() #senha criptografada do banco de dados
        name = hashlib.md5(name.encode()).hexdigest() #nome criptografado do banco de dados
        nome = hashlib.md5(request.form['nome'].encode()).hexdigest() #nome do usuario criptografa
        if(name == nome and senha == passwords):
            if request.method == "POST":
                session["nome"] = request.form.get("nome")
                return redirect(url_for("sessao"))
            else:
                flash("Usuário e\ou senha incorreto(s)")
                return redirect(url_for("login"))
        else:
            flash("Usuário e\ou senha incorreto(s)")
            return redirect(url_for("login"))
    
    
    
    


if __name__=="__main__":
    app.run(debug=True)
