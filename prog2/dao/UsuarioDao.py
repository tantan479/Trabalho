from model.Usuario import Usuario

class UsuarioDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarUsuarios(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM usuario'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            usuario = Usuario()
            usuario.id = item[0]
            usuario.nome = item[1]
            usuario.email = item[2]
            usuario.senha = item[3]

            lista.append(usuario)

        return lista

    def inserirUsuario1(self, nome, email, senha) -> int:
        c = self.connection.cursor()

        sql = "insert into usuario(nome, email, senha) values (%s, %s, %s) RETURNING id"
        c.execute(sql,[nome, email, senha])
        id = c.fetchone()[0]
        c.close()
        self.connection.commit()

        return id

    def apagarUsuario1(self, id):
        c = self.connection.cursor()

        sql = "delete from usuario where id=%s"
    
        c.execute(sql,[id])
        c.close()
        self.connection.commit()