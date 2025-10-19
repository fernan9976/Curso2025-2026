# -*- coding: utf-8 -*-
"""
Task06_2025.py
Modifying RDF(s) for Assignment 4
"""

import urllib.request
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from validation import Report

# Crear gráfico RDF
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

# Namespaces
ns = Namespace("http://mydomain.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

# Task 6.0: Prefijos
g.namespace_manager.bind('ontology', ns, override=False)
g.namespace_manager.bind('person', Namespace("http://oeg.fi.upm.es/def/people#"), override=False)

# Task 6.1: Clases y jerarquía
Person = Namespace("http://oeg.fi.upm.es/def/people#").Person
Professor = ns.Professor
AssociateProfessor = ns.AssociateProfessor
InterimAssociateProfessor = ns.InterimAssociateProfessor
FullProfessor = ns.FullProfessor

classes = [Person, Professor, AssociateProfessor, InterimAssociateProfessor, FullProfessor]

for c in classes:
    g.add((c, RDF.type, RDFS.Class))
    g.add((c, RDFS.label, Literal(c.split("#")[-1], datatype=XSD.string)))

# Jerarquía
g.add((Professor, RDFS.subClassOf, Person))
g.add((AssociateProfessor, RDFS.subClassOf, Professor))
g.add((InterimAssociateProfessor, RDFS.subClassOf, AssociateProfessor))
g.add((FullProfessor, RDFS.subClassOf, Professor))

# Task 6.2: Propiedades
hasColleague = ns.hasColleague
hasName = ns.hasName
hasHomePage = ns.hasHomePage

g.add((hasColleague, RDF.type, RDF.Property))
g.add((hasColleague, RDFS.domain, Person))
g.add((hasColleague, RDFS.range, Person))
g.add((hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))

g.add((hasName, RDF.type, RDF.Property))
g.add((hasName, RDFS.domain, Person))
g.add((hasName, RDFS.range, RDFS.Literal))
g.add((hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))

g.add((hasHomePage, RDF.type, RDF.Property))
g.add((hasHomePage, RDFS.domain, FullProfessor))
g.add((hasHomePage, RDFS.range, RDFS.Literal))
g.add((hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))

# Task 6.3: Individuos
Oscar = Namespace("http://oeg.fi.upm.es/resource/person/").Oscar
Asun = Namespace("http://oeg.fi.upm.es/resource/person/").Asun
Raul = Namespace("http://oeg.fi.upm.es/resource/person/").Raul

g.add((Oscar, RDF.type, Professor))
g.add((Oscar, RDFS.label, Literal("Oscar", datatype=XSD.string)))
g.add((Oscar, hasColleague, Asun))
g.add((Oscar, hasName, Literal("Oscar", datatype=XSD.string)))

g.add((Asun, RDF.type, AssociateProfessor))
g.add((Asun, RDFS.label, Literal("Asun", datatype=XSD.string)))
g.add((Asun, hasColleague, Raul))
g.add((Asun, hasHomePage, Literal("asun_homepage", datatype=XSD.string)))

g.add((Raul, RDF.type, InterimAssociateProfessor))
g.add((Raul, RDFS.label, Literal("Raul", datatype=XSD.string)))
g.add((Raul, hasColleague, Oscar))

# Task 6.4: Propiedades VCARD/FOAF
g.add((Oscar, VCARD.Given, Literal("Oscar", datatype=XSD.string)))
g.add((Oscar, VCARD.Family, Literal("Lastname", datatype=XSD.string)))
g.add((Oscar, FOAF.email, Literal("oscar@email.com", datatype=XSD.string)))

# ------------------------------
# VALIDACIONES CON TRY/EXCEPT
# ------------------------------
try:
    r.validate_task_06_01(g)
except Exception as e:
    print("Error en tarea 6.1:", e)

try:
    r.validate_task_06_02(g)
except Exception as e:
    print("Error en tarea 6.2:", e)

try:
    r.validate_task_06_03(g)
except Exception as e:
    print("Error en tarea 6.3:", e)

try:
    r.validate_task_06_04(g)
except Exception as e:
    print("Error en tarea 6.4:", e)

# ------------------------------
# GUARDAR REPORTE SIEMPRE
# ------------------------------
r.save_report("_Task_06")  # Nota: el método de tu clase concatena "report_result" + task + ".txt"
print("Reporte Task 06 generado correctamente.")


