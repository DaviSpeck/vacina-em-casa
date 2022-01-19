import mysql.connector
from util import classe_sql
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('index.html')


@app.route('/menuAdmin')
def menuAdmin():
    return render_template('menuAdmin.html')


@app.route('/formincluirVacinacao')
def formIncluirVacinacao():
    return render_template('Inclusao/formIncluirVacinacao.html')


@app.route('/incluirVacinacao', methods=['POST'])
def incluirVacinacao():
    nomeVacina = request.form['nomeVacina']
    local = request.form['local']
    dataVaga = request.form['dataVaga']
    horarioVaga = request.form['horarioVaga']

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = '''
            INSERT INTO tb_vacinacao(nomeVacina, local, dataVaga, horarioVaga)
            VALUES (%s, %s, %s, %s);
            '''
    if sql.executar(cmd, [nomeVacina, local, dataVaga, horarioVaga]):
        msg = "Vacinação para " + nomeVacina + " cadastrada com sucesso!"
    else:
        msg = "Falha na inclusão da vacinação."

    return render_template('Inclusao/incluirVacinacao.html', msg=msg)


@app.route('/parconsultarAstrazeneca')
def parConsultarAstrazeneca():
    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = "SELECT DISTINCT local FROM tb_vacinacao WHERE nomeVacina = 'Astrazeneca' ORDER BY local ;"

    cs = sql.consultar(cmd, [])
    sel_local = "<SELECT NAME='local'>"
    sel_local += "<OPTION>Todos</OPTION>"
    for [local] in cs:
        sel_local += "<OPTION>" + local + "</OPTION>"
    sel_local += "</SELECT>"
    cs.close()

    return render_template('Astrazeneca/parConsultarAstrazeneca.html', sel_local=sel_local)


@app.route('/parconsultarCoronavac')
def parConsultarCoronavac():
    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = "SELECT DISTINCT local FROM tb_vacinacao WHERE nomeVacina = 'CoronaVac' ORDER BY local;"

    cs = sql.consultar(cmd, [])
    sel_local = "<SELECT NAME='local'>"
    sel_local += "<OPTION>Todos</OPTION>"
    for [local] in cs:
        sel_local += "<OPTION>" + local + "</OPTION>"
    sel_local += "</SELECT>"
    cs.close()

    return render_template('CoronaVac/parConsultarCoronaVac.html', sel_local=sel_local)


@app.route('/parconsultarJanssen')
def parConsultarJanssen():
    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = "SELECT DISTINCT local FROM tb_vacinacao WHERE nomeVacina = 'Janssen' ORDER BY local;"

    cs = sql.consultar(cmd, [])
    sel_local = "<SELECT NAME='local'>"
    sel_local += "<OPTION>Todos</OPTION>"
    for [local] in cs:
        sel_local += "<OPTION>" + local + "</OPTION>"
    sel_local += "</SELECT>"
    cs.close()

    return render_template('Janssen/parConsultarJanssen.html', sel_local=sel_local)


@app.route('/parconsultarPfizer')
def parConsultarPfizer():
    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = "SELECT DISTINCT local FROM tb_vacinacao WHERE nomeVacina = 'Pfizer' ORDER BY local;"

    cs = sql.consultar(cmd, [])
    sel_local = "<SELECT NAME='local'>"
    sel_local += "<OPTION>Todos</OPTION>"
    for [local] in cs:
        sel_local += "<OPTION>" + local + "</OPTION>"
    sel_local += "</SELECT>"
    cs.close()

    return render_template('Pfizer/parConsultarPfizer.html', sel_local=sel_local)


@app.route('/consultarAstrazeneca', methods=['POST'])
def consultarAstrazeneca():
    local = request.form['local']

    local = "" if local == "Todos" else local

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = ''' 
          SELECT * FROM tb_vacinacao WHERE local LIKE CONCAT('%', %s, '%') 
          AND nomeVacina = 'Astrazeneca'
          '''

    cs = sql.consultar(cmd, [local])
    vacinacaoAstrazeneca = ""
    for [idVacinacao, nomeVacina, local, dataVaga, horarioVaga] in cs:
        vacinacaoAstrazeneca += "<TR>"
        vacinacaoAstrazeneca += "<TD>" + nomeVacina + "</TD>"
        vacinacaoAstrazeneca += "<TD>" + local + "</TD>"
        vacinacaoAstrazeneca += "<TD>" + str(dataVaga) + "</TD>"
        vacinacaoAstrazeneca += "<TD>" + str(horarioVaga) + "</TD>"
        vacinacaoAstrazeneca += "</TR>"
    cs.close()

    return render_template('Astrazeneca/consultarAstrazeneca.html', vacinacaoAstrazeneca=vacinacaoAstrazeneca)


@app.route('/consultarCoronavac', methods=['POST'])
def consultarCoronovac():
    local = request.form['local']

    local = "" if local == "Todos" else local

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = ''' 
          SELECT * FROM tb_vacinacao WHERE local LIKE CONCAT('%', %s, '%')
          AND nomeVacina = 'CoronaVac' 
          '''

    cs = sql.consultar(cmd, [local])
    vacinacaoCoronavac = ""
    for [idVacinacao, nomeVacina, local, dataVaga, horarioVaga] in cs:
        vacinacaoCoronavac += "<TR>"
        vacinacaoCoronavac += "<TD>" + nomeVacina + "</TD>"
        vacinacaoCoronavac += "<TD>" + local + "</TD>"
        vacinacaoCoronavac += "<TD>" + str(dataVaga) + "</TD>"
        vacinacaoCoronavac += "<TD>" + str(horarioVaga) + "</TD>"
        vacinacaoCoronavac += "</TR>"
    cs.close()

    return render_template('CoronaVac/consultarCoronaVac.html', vacinacaoCoronavac=vacinacaoCoronavac)


@app.route('/consultarJanssen', methods=['POST'])
def consultarJanssen():
    local = request.form['local']

    local = "" if local == "Todos" else local

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = ''' 
          SELECT * FROM tb_vacinacao WHERE local LIKE CONCAT('%', %s, '%') 
          AND nomeVacina = 'Janssen'
          '''

    cs = sql.consultar(cmd, [local])
    vacinacaoJanssen = ""
    for [idVacinacao, nomeVacina, local, dataVaga, horarioVaga] in cs:
        vacinacaoJanssen += "<TR>"
        vacinacaoJanssen += "<TD>" + nomeVacina + "</TD>"
        vacinacaoJanssen += "<TD>" + local + "</TD>"
        vacinacaoJanssen += "<TD>" + str(dataVaga) + "</TD>"
        vacinacaoJanssen += "<TD>" + str(horarioVaga) + "</TD>"
        vacinacaoJanssen += "</TR>"
    cs.close()

    return render_template('Janssen/consultarJanssen.html', vacinacaoJanssen=vacinacaoJanssen)


@app.route('/consultarPfizer', methods=['POST'])
def consultarPfizer():
    local = request.form['local']

    local = "" if local == "Todos" else local

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = ''' 
          SELECT * FROM tb_vacinacao WHERE local LIKE CONCAT('%', %s, '%') 
          AND nomeVacina = 'Pfizer'
          '''

    cs = sql.consultar(cmd, [local])
    vacinacaoPfizer = ""
    for [idVacinacao, nomeVacina, local, dataVaga, horarioVaga] in cs:
        vacinacaoPfizer += "<TR>"
        vacinacaoPfizer += "<TD>" + nomeVacina + "</TD>"
        vacinacaoPfizer += "<TD>" + local + "</TD>"
        vacinacaoPfizer += "<TD>" + str(dataVaga) + "</TD>"
        vacinacaoPfizer += "<TD>" + str(horarioVaga) + "</TD>"
        vacinacaoPfizer += "</TR>"
    cs.close()

    return render_template('Pfizer/consultarPfizer.html', vacinacaoPfizer=vacinacaoPfizer)


@app.route('/paralterar')
def parAlterar():
    return render_template('Alteracao/parAlterar.html')


@app.route('/formalterar', methods=['POST'])
def formAlterar():
    nomeVacina = request.form['nomeVacina']
    local = request.form['local']
    dataVaga = request.form['dataVaga']
    horarioVaga = request.form['horarioVaga']

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = "SELECT * FROM tb_vacinacao WHERE nomeVacina=%s AND local=%s AND dataVaga=%s AND horarioVaga=%s;"

    cs = sql.consultar(cmd, [nomeVacina, local, dataVaga, horarioVaga])
    dados = cs.fetchone()
    cs.close()

    if dados != None:
        return render_template('Alteracao/formAlterar.html',
                               idVacinacao=dados[0], nomeVacina=dados[1], local=dados[2],
                               dataVaga=dados[3], horarioVaga=dados[4])
    else:
        return render_template('Alteracao/naoEncontrado.html')


@app.route('/alterar', methods=['POST'])
def alterar():
    idVacinacao = int(request.form['idVacinacao'])
    nomeVacina = request.form['nomeVacina']
    local = request.form['local']
    dataVaga = str(request.form['dataVaga'])
    horarioVaga = str(request.form['horarioVaga'])

    sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
    cmd = '''
          UPDATE tb_vacinacao SET nomeVacina=%s, local=%s, dataVaga=%s, horarioVaga=%s
          WHERE idVacinacao=%s;
          '''

    if sql.executar(cmd, [nomeVacina, local, dataVaga, horarioVaga, idVacinacao]):
        msg = "Vacinação para" + nomeVacina + " alterado com sucesso!"
    else:
        msg = "Falha na alteração da vacina."

    return render_template('Alteracao/alterar.html', msg=msg)


@app.route('/parexcluir')
def parExcluir():
   sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
   cmd = ''' 
         SELECT idVacinacao, nomeVacina, local, dataVaga, horarioVaga 
         FROM tb_vacinacao ORDER BY nomeVacina;
         '''

   cs = sql.consultar(cmd, [])
   vacinacoes = ""
   for [idVacinacao, nomeVacina, local, dataVaga, horarioVaga] in cs:
       vacinacoes += "<TR>"
       vacinacoes += "<TD>" + nomeVacina + " | " + local + "</TD>"
       vacinacoes += "<TD>" + str(dataVaga) + "</TD>"
       vacinacoes += "<TD>" + str(horarioVaga) + "</TD>"
       vacinacoes += "<TD><BUTTON ONCLICK=\"jsExcluir('" + nomeVacina + " (" + local + ")" + "', " + str(idVacinacao) + ")\">Excluir" + "</BUTTON></TD>"
       vacinacoes += "</TR>"
   cs.close()

   return render_template('Exclusao/parExcluir.html', vacinacoes=vacinacoes)

@app.route('/excluir', methods=['POST'])
def excluir():
   idVacinacao = int(request.form['idVacinacao'])

   sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")
   cmd = "DELETE FROM tb_vacinacao WHERE idVacinacao=%s;"

   if sql.executar(cmd, [idVacinacao]):
       msg="Vacinação excluída com sucesso!"
   else:
       msg="Falha na exclusão de vacinação."

   return render_template('Exclusao/excluir.html', msg=msg)


app.debug = 1
app.run()
