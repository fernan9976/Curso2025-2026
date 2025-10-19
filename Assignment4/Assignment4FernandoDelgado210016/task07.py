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

# Cargar RDF generado por task06.py
try:
    g.parse("data06.ttl", format="TTL")  # si no existe, puedes generar un TTL desde task06.py
except Exception as e:
    print("No se pudo cargar data06.ttl:", e)

# ----------------------
# TASK 7.1a: List classes and superclasses using RDFLib
# ----------------------
try:
    result = []
    vistas = set()
    for c in g.subjects(RDF.type, RDFS.Class):
        if c in vistas:
            continue
        vistas.add(c)
        sc = g.value(subject=c, predicate=RDFS.subClassOf, object=None)
        result.append((c, sc))
    r.validate_07_1a(result)
except Exception as e:
    print("Error en TASK 7.1a:", e)

# ----------------------
# TASK 7.1b: Repeat in SPARQL
# ----------------------
try:
    query_7_1b = '''
        SELECT DISTINCT ?c ?sc WHERE {
            ?c a rdfs:Class .
            OPTIONAL { ?c rdfs:subClassOf ?sc. }
        }
    '''
    r.validate_07_1b(query_7_1b, g)
except Exception as e:
    print("Error en TASK 7.1b:", e)

# ----------------------
# TASK 7.2a: List all individuals of Person using RDFLib
# ----------------------
try:
    classes = set(g.transitive_subjects(RDFS.subClassOf, p.Person)) | {p.Person}
    individuals = sorted({s for c in classes for s in g.subjects(RDF.type, c)}, key=str)
    r.validate_07_02a(individuals)
except Exception as e:
    print("Error en TASK 7.2a:", e)

# ----------------------
# TASK 7.2b: Repeat in SPARQL
# ----------------------
try:
    query_7_2b = prepareQuery('''
        SELECT ?ind WHERE {
            ?ind rdf:type/rdfs:subClassOf* p:Person .
        }
    ''', initNs={"p": p, "rdf": RDF, "rdfs": RDFS})
    r.validate_07_02b(g, query_7_2b)
except Exception as e:
    print("Error en TASK 7.2b:", e)

# ----------------------
# TASK 7.3: List name and type of those who know Rocky (SPARQL only)
# ----------------------
try:
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
    r.validate_07_03(g, query_7_3)
except Exception as e:
    print("Error en TASK 7.3:", e)

# ----------------------
# TASK 7.4: List names of entities with a colleague with a dog (SPARQL)
# ----------------------
try:
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
    r.validate_07_04(g, query_7_4)
except Exception as e:
    print("Error en TASK 7.4:", e)

# ------------------------------
# GUARDAR REPORTE SIEMPRE
# ------------------------------
try:
    r.save_report("_Task_07")  # Esto creará "report_result_Task_07.txt"
    print("Reporte Task 07 generado correctamente.")
except Exception as e:
    print("Error guardando report_result_Task_07.txt:", e)

