# -*- coding: utf-8 -*-
"""
Task07_2025.py
Querying RDF(s) for Assignment 4
"""

from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.plugins.sparql import prepareQuery
from validation import Report

# Crear el grafo y el reporte
g = Graph()
r = Report()

# Namespaces
ns = Namespace("http://mydomain.org#")
p = Namespace("http://oeg.fi.upm.es/def/people#")

g.namespace_manager.bind('ns', ns, override=False)
g.namespace_manager.bind('person', p, override=False)

# Cargar RDF (si quieres cargar un ttl local o el generado por task06.py)
g.parse("data06.ttl", format="TTL")  # si no existe, puedes usar g.serialize("data06.ttl") en task06.py

# ----------------------
# TASK 7.1a: List classes and superclasses using RDFLib
# ----------------------
result = []
vistas = set()
for c in g.subjects(RDF.type, RDFS.Class):
    if c in vistas:
        continue
    vistas.add(c)
    sc = g.value(subject=c, predicate=RDFS.subClassOf, object=None)
    result.append((c, sc))

r.validate_07_1a(result)

# ----------------------
# TASK 7.1b: Repeat in SPARQL
# ----------------------
query_7_1b = '''
    SELECT DISTINCT ?c ?sc WHERE {
        ?c a rdfs:Class .
        OPTIONAL { ?c rdfs:subClassOf ?sc. }
    }
'''
qres = g.query(query_7_1b)
result_7_1b = [(r[0], r[1]) for r in qres]  # Acceso por índice para evitar AttributeError
r.validate_07_1b(query_7_1b, g)

# ----------------------
# TASK 7.2a: List all individuals of Person using RDFLib
# ----------------------
classes = set(g.transitive_subjects(RDFS.subClassOf, p.Person)) | {p.Person}
individuals = sorted({s for c in classes for s in g.subjects(RDF.type, c)}, key=str)

r.validate_07_02a(individuals)

# ----------------------
# TASK 7.2b: Repeat in SPARQL
# ----------------------
query_7_2b = prepareQuery('''
    SELECT ?ind WHERE {
        ?ind rdf:type/rdfs:subClassOf* p:Person .
    }
''', initNs={"p": p, "rdf": RDF, "rdfs": RDFS})

qres_7_2b = g.query(query_7_2b)
individuals_sparql = [r[0] for r in qres_7_2b]  # Acceso por índice
r.validate_07_02b(g, query_7_2b)

# ----------------------
# TASK 7.3: List name and type of those who know Rocky (SPARQL only)
# ----------------------
query_7_3 = prepareQuery('''
    SELECT ?name ?type WHERE {
        ?ind p:knows p:Rocky .
        ?ind rdf:type ?type .
        {
            ?ind p:hasName ?name .
        } UNION {
            ?ind rdfs:label ?name .
        }
    }
''', initNs={"p": p, "rdf": RDF, "rdfs": RDFS})

qres_7_3 = g.query(query_7_3)
result_7_3 = [(r[0], r[1]) for r in qres_7_3]
r.validate_07_03(g, query_7_3)

# ----------------------
# TASK 7.4: List names of entities with a colleague with a dog (SPARQL)
# ----------------------
query_7_4 = prepareQuery('''
    SELECT DISTINCT ?name WHERE {
        ?ind rdfs:label ?name .
        ?ind p:hasColleague ?col .
        {
            ?col p:ownsPet ?pet .
        } UNION {
            ?col p:hasColleague ?col2 .
            ?col2 p:ownsPet ?pet .
        }
    }
''', initNs={"p": p, "rdfs": RDFS})

qres_7_4 = g.query(query_7_4)
result_7_4 = [r[0] for r in qres_7_4]
r.validate_07_04(g, query_7_4)

# Guardar reporte
r.save_report("report_result_Task_07.txt")

