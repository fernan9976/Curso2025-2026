# -*- coding: utf-8 -*-
"""
TASK 07: Queries with SPARQL
"""

from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS
from utils import *
from rdflib import Namespace

# Namespaces
ns = Namespace("http://oeg.fi.upm.es/def/people#")

# Graph
rdf_graph = Graph()
rdf_graph.parse("people.rdf", format="xml")

# 7.1a
consulta_1a = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?class WHERE {
  ?class rdfs:subClassOf* p:Person .
}
''')
for r in rdf_graph.query(consulta_1a):
    print(r.class)

rep.validate_07_01a(rdf_graph, consulta_1a)


# 7.1b
consulta_1b = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT DISTINCT ?ind WHERE {
  ?ind rdf:type/rdfs:subClassOf* p:Person .
}
''')
for r in rdf_graph.query(consulta_1b):
    print(r.ind)

rep.validate_07_01b(rdf_graph, consulta_1b)


# 7.2a
consulta_2a = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT DISTINCT ?ind WHERE {
  ?ind rdf:type ?class .
  ?class rdfs:subClassOf* p:Researcher .
}
''')
for r in rdf_graph.query(consulta_2a):
    print(r.ind)

rep.validate_07_02a(rdf_graph, consulta_2a)


# 7.2b
consulta_2b = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?ind WHERE {
  ?ind rdf:type ?class .
  ?class rdfs:subClassOf* p:Person .
}
''')
for r in rdf_graph.query(consulta_2b):
    print(r.ind)

rep.validate_07_02b(rdf_graph, consulta_2b)


# 7.3
consulta_3 = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?name ?type WHERE {
  ?ind p:knows p:Rocky .
  ?ind rdf:type ?type .
  {
    ?ind p:hasName ?name .
  }
  UNION {
    ?ind rdfs:label ?name .
  }
}
''')
for r in rdf_graph.query(consulta_3):
    print(r.name, r.type)

rep.validate_07_03(rdf_graph, consulta_3)


# 7.4
consulta_4 = prepareQuery('''
PREFIX p: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?name WHERE {
  ?x p:worksWith p:John .
  ?x p:hasName ?name .
}
''')
for r in rdf_graph.query(consulta_4):
    print(r.name)

rep.validate_07_04(rdf_graph, consulta_4)
