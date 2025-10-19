# -*- coding: utf-8 -*-
"""
Task07_2025.py
Querying RDF(s) for Assignment 4
"""

from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.plugins.sparql import prepareQuery
from validation import Report

# Crear el grafo
g = Graph()
g.parse("data06.ttl", format="ttl")  # asegúrate de guardar tu task06 en TTL

report = Report()

# Namespaces
ns = Namespace("http://mydomain.org#")          # Profesores y propiedades custom
p = Namespace("http://oeg.fi.upm.es/def/people#")  # Persona

# -----------------------------
# TASK 7.1a: List classes + superclasses (RDFLib)
# -----------------------------
result = []
vistas = set()
for c in g.subjects(RDF.type, RDFS.Class):
    if c in vistas:
        continue
    vistas.add(c)
    sc = g.value(subject=c, predicate=RDFS.subClassOf, object=None)  # None si no tiene superclase
    result.append((c, sc))

for r in result:
    print(r)

report.validate_07_1a(result)

# -----------------------------
# TASK 7.1b: Same with SPARQL
# -----------------------------
query_71b = prepareQuery('''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?c ?sc WHERE {
    ?c a rdfs:Class .
    OPTIONAL { ?c rdfs:subClassOf ?sc }
}
''')

for r in g.query(query_71b):
    print(r.c, r.sc)

report.validate_07_1b(query_71b, g)

# -----------------------------
# TASK 7.2a: List all individuals of Person + subclasses (RDFLib)
# -----------------------------
classes_person = set(g.transitive_subjects(RDFS.subClassOf, p.Person)) | {p.Person}
individuals = sorted({s for c in classes_person for s in g.subjects(RDF.type, c)}, key=str)

for i in individuals:
    print(i)

report.validate_07_02a(individuals)

# -----------------------------
# TASK 7.2b: Same with SPARQL
# -----------------------------
query_72b = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?ind WHERE {
    ?ind rdf:type ?s .
    ?s rdfs:subClassOf* p:Person .
}
''')

for r in g.query(query_72b):
    print(r.ind)

report.validate_07_02b(g, query_72b)

# -----------------------------
# TASK 7.3: Name and type of those who know Rocky (SPARQL)
# -----------------------------
query_73 = prepareQuery('''
PREFIX p: <http://mydomain.org#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?type WHERE {
    ?ind p:knows p:Rocky .
    ?ind rdf:type ?type .
    { ?ind p:hasName ?name }
    UNION { ?ind rdfs:label ?name }
}
''')

for r in g.query(query_73):
    print(r.name, r.type)

report.validate_07_03(g, query_73)

# -----------------------------
# TASK 7.4: Entities with colleague with dog (SPARQL)
# -----------------------------
query_74 = prepareQuery('''
PREFIX p: <http://mydomain.org#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?name WHERE {
    ?ind rdfs:label ?name .
    ?ind p:hasColleague ?c1 .
    { ?c1 p:ownsPet ?pet }
    UNION {
        ?c1 p:hasColleague ?c2 .
        ?c2 p:ownsPet ?pet
    }
}
''')

for r in g.query(query_74):
    print(r.name)

report.validate_07_04(g, query_74)
report.save_report("_Task_07")

