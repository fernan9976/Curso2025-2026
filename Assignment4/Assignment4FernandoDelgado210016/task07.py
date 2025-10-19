#!pip install rdflib
# -*- coding: utf-8 -*-


import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
source_repo = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

from validation import Report
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

# Carga del grafo RDF
rdf_graph = Graph()
ns = Namespace("http://somewhere#")
rdf_graph.namespace_manager.bind("ns", ns, override=False)
rdf_graph.parse(source_repo + "/rdf/data06.ttl", format="turtle")

rep = Report()

# ==========================================================
# TASK 7.1a - RDFLib: clases y superclases
# ==========================================================
resultado = []
vistos = set()

for clase in rdf_graph.subjects(RDF.type, RDFS.Class):
    if clase in vistos:
        continue
    vistos.add(clase)
    super_clase = rdf_graph.value(subject=clase, predicate=RDFS.subClassOf)
    resultado.append((clase, super_clase))

for par in resultado:
    print(f"{par[0]} --> {par[1]}")

rep.validate_07_1a(resultado)

# ==========================================================
# TASK 7.1b - SPARQL
# ==========================================================
# ==========================================================
# TASK 7.1b - SPARQL
# ==========================================================
consulta_1b = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""

for fila in rdf_graph.query(consulta_1b):
    print(fila.c, fila.sc)

rep.validate_07_1b(consulta_1b, rdf_graph)


# ==========================================================
# TASK 7.2a - RDFLib: individuos de Person
# ==========================================================
p = Namespace("http://oeg.fi.upm.es/def/people#")

todas = set(rdf_graph.transitive_subjects(RDFS.subClassOf, p.Person)) | {p.Person}
individuos = sorted({ind for cls in todas for ind in rdf_graph.subjects(RDF.type, cls)}, key=str)

for i in individuos:
    print(i)

rep.validate_07_02a(individuos)

# ==========================================================
# TASK 7.2b - SPARQL
# ==========================================================

from rdflib import Namespace

PEOPLE = Namespace("http://oeg.fi.upm.es/def/people#")

consulta_2b = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT ?ind
WHERE {
    ?ind a people:FullProfessor .
}
"""

rep.validate_07_02b(rdf_graph, consulta_2b)


# ==========================================================
# TASK 7.3 - SPARQL: quienes conocen a Rocky
# ==========================================================
consulta_3 = prepareQuery("""
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?nombre ?tipo
WHERE {
  ?ind p:knows p:Rocky ;
       rdf:type ?tipo .
  {
    ?ind p:hasName ?nombre .
  }
  UNION
  {
    ?ind rdfs:label ?nombre .
  }
}
""")

for fila in rdf_graph.query(consulta_3):
    print(fila.nombre, fila.tipo)

rep.validate_07_03(rdf_graph, consulta_3)

# ==========================================================
# TASK 7.4 - SPARQL: entidades con colega con perro
# ==========================================================
consulta_4 = prepareQuery("""
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?nombre
WHERE {
  ?e rdfs:label ?nombre ;
     p:hasColleague ?col .
  
  {
    ?col p:ownsPet ?m .
  }
  UNION
  {
    ?col p:hasColleague ?col2 .
    ?col2 p:ownsPet ?m .
  }
}
""")

for x in rdf_graph.query(consulta_4):
    print(x.nombre)

rep.validate_07_04(rdf_graph, consulta_4)
rep.save_report("_Task_07")
