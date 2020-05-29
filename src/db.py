from py2neo import Graph

# Database Credentials
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "123"
db = Graph(uri, auth=(userName, password), encrypted=False)


#Metodo que muestra todos los videos que cierto usuario ha visto
def mostrarVideosVistosPorUsuario(name):
        for record in db.run("MATCH (a:user)-[:watched]->(r) " "WHERE a.name = $name " "RETURN r.name", name=name):
           print(record["r.name"])

#mostrarVideosVistosPorUsuario("Gabriel")

#Metodo que revisa si un usuario existe (Para hacer el login)
def usuarioExiste(name):
        resultado = db.run("MATCH (a:user) WHERE a.name = $name RETURN a.name", name=name)
        for line in resultado:
            if line["a.name"] == name:
                return True
            else:
                return False


#print(usuarioExiste("Oscar"))
            
#Metodo que crea una relationship entre usuario y video
def crearRelacion(name, video):
        db.run("MATCH (a:user),(b:video) WHERE a.name = $name AND b.name = $video CREATE (a)-[:watched]->(b)")
        

#Recomendaciones
def Recomendaciones(name, video, tag, category):
    lista = []
    videos = db.run("MATCH (a:user)-[:watched]->(b:video), (b)-[:hasTag]->(c:tag), (b)-[:hasGenre]->(d:category), (e:video)-[:hasGenre]->(d:category), (e:video)-[:hasTag]->(c:tag) WHERE a.name = $name AND b.name = $video AND c.name = $tag AND d.name = $category RETURN e.name UNION MATCH (a:user)-[:watched]->(b:video), (b)-[:hasGenre]->(d:category), (e:video)-[:hasGenre]->(d:category) RETURN e.name UNION MATCH (a:user)-[:watched]->(b:video), (b)-[:hasGenre]->(d:category), (e:video)-[:hasTag]->(c:tag) RETURN e.name", name=name, video=video, tag=tag, category=category)
    for line in videos:
        lista.append(videos["e.name"])
        return lista
#Explorar
def Explorar(name, video, tag, category):
    lista = []
    videos = db.run("MATCH (a:user)-[:watched]->(b:video), (b)-[:hasTag]->(c:tag), (b)-[:hasGenre]->(d:category), (e:video)-[:hasGenre]->(d:category), (e:video)-[:hasTag]->(c:tag) WHERE a.name <> $name AND b.name <> $video AND c.name <> $tag AND d.name <> $category RETURN e.name", name=name, video=video, tag=tag, category=category)
    for line in videos:
        lista.append(videos["e.name"])
        return lista

#Devolver Nodo Video
def DevolverNodoV(name):
    resultado = db.run("MATCH (a:user)-[:watched]->(b:video) WHERE a.name = $name RETURN b.name", name=name)
    for line in resultado:
          return  line["b.name"]         
    

#Devolver Nodo Tag
def DevolverNodoT(name, video):
    resultado = db.run("MATCH (a:user)-[:watched]->(b:video), (b)-[:hasTag]->(c:tag) WHERE a.name = $name AND b.name = $video RETURN c.name", name=name, video=video)
    for line in resultado:
          return  line["c.name"]
          
#Devolver Nodo categoria
def DevolverNodoC(name, video):
    resultado = db.run("MATCH (a:user)-[:watched]->(b:video), (b)-[:hasGenre]->(d:category) WHERE a.name = $name AND b.name = $video RETURN d.name", name=name, video=video)
    for line in resultado:
          return  line["d.name"]
        
#Prueba de los metodos
"""nombre = "Guido"
print(DevolverNodoV(nombre))
print(DevolverNodoT(nombre,DevolverNodoV(nombre)))
print(DevolverNodoC(nombre,DevolverNodoV(nombre)))
print(Recomendaciones(nombre, DevolverNodoV(nombre), DevolverNodoT(nombre,DevolverNodoV(nombre)), DevolverNodoC(nombre,DevolverNodoV(nombre))))
print(Explorar(nombre, DevolverNodoV(nombre), DevolverNodoT(nombre,DevolverNodoV(nombre)), DevolverNodoC(nombr
