from util import classe_sql

sql = classe_sql.SQL("root", "Root12345678", "bd_vacinacao")

cmd = "DROP TABLE IF EXISTS tb_vacinacao;"

if sql.executar(cmd, []):
   print ("Tabela excluída com sucesso!")


cmd = '''
    CREATE TABLE tb_vacinacao (
        idVacinacao INT AUTO_INCREMENT PRIMARY KEY,
        nomeVacina VARCHAR(50),
        local VARCHAR(75) NOT NULL,
        dataVaga DATE NOT NULL,
        horarioVaga TIME NOT NULL);
    '''

if sql.executar(cmd, []):
   print ("Tabela criada com sucesso!")
