from py2neo import Graph

# Database Credentials
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "123"
db = Graph(uri, auth=(userName, password), encrypted=False)

#Metodo que revisa si un usuario existe (Para hacer el login)
def usuarioExiste(name):
    resultado = db.run("MATCH (a:user) WHERE a.name = $name RETURN a.name", name=name)
    for line in resultado:
        if line["a.name"] == name:
            return True
        else:
            return False

            
#Metodo que crea una relationship entre usuario y video
def crearRelacion(name, video):
    db.run("MATCH (a:user),(b:video) WHERE a.name = $name AND b.name = $video CREATE (a)-[:watched]->(b)")

#Explorar
def Explorar(name):
    lista = []
    resultado = db.run("MATCH (a:user)-[:watched]->(b:video), (b)-[:hasTag]->(c:tag), (b)-[:hasGenre]->(d:genre), (e:video)-[:hasGenre]->(d:genre), (e:video)-[:hasTag]->(c:tag) WHERE a.name <> $name RETURN b.name", name=name).data()
    for line in resultado:
        lista.append(line.get("b.name"))
    return lista

#Recomendaciones
def Recomendaciones(name):
    lista = []
    resultado = db.run("MATCH (u:user)-[:watched]->(v1), (v1)-[:hasTag]->(t)<-[:hasTag]-(v2), (v1)-[:hasGenre]->(g)<-[:hasGenre]-(v2) WHERE u.name = $name RETURN v2.name", name = name).data()
    for line in resultado:
        lista.append(line.get("v2.name"))
    return lista

#Metodo que muestra todos los videos que cierto usuario ha visto
def Historial(name):
    lista = []
    for record in db.run("MATCH (a:user)-[:watched]->(r) " "WHERE a.name = $name " "RETURN r.name", name=name):
        lista.append(record["r.name"])
    return lista

#Todos los videos existentes
def allVideos():
    lista = []
    for record in db.run("MATCH (v:video) return v.name"):
        lista.append(record["v.name"])
    return lista

