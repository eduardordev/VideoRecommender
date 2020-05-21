from neo4j import GraphDatabase

# Database Credentials
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "123"
db = GraphDatabase.driver(uri, auth=(userName, password), encrypted=False)

#Metodo que muestra todos los videos que cierto usuario ha visto
def mostrarVideosVistosPorUsuario(name):
    with db.session() as session:
        for record in session.run("MATCH (a:user)-[:watched]->(r) "
                             "WHERE a.name = $name "
                             "RETURN r.name", name=name):
            print(record["r.name"])

#mostrarVideosVistosPorUsuario("Gabriel")

#Metodo que revisa si un usuario existe (Para hacer el login)
def usuarioExiste(name):
    with db.session() as session:
        resultado = session.run("MATCH (a:user) WHERE a.name = $name RETURN a.name", name=name)
        for line in resultado:
            if line["a.name"] == name:
                return True
            else:
                return False


#print(usuarioExiste("Oscar"))
            
#Metodo que crea una relationship entre usuario y video
def crearRelacion(name, video):
    with db.session() as session:
        session.run("MATCH (a:user),(b:video) WHERE a.name = $name AND b.name = $video CREATE (a)-[:watched]->(b)")

          
