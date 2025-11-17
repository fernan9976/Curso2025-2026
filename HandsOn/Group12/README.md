# HandsOn Group 12 - CORREGIDO ✓

## 📋 Resumen de Correcciones Aplicadas

Este proyecto ha sido completamente revisado y corregido para solucionar todos los errores identificados en la revisión.

### ✅ Errores Corregidos

#### 1. **analysis.html - CORREGIDO**
- ✓ **Añadida licencia de datasets seleccionados**: Se incluye CC BY 4.0 del Ayuntamiento de Madrid y CC0 de Wikidata
- ✓ **Añadida licencia del dataset a generar**: CC BY 4.0 con atribución completa
- ✓ **Añadida estrategia de nombrado de recursos**: Documentación completa de URIs para ontología, instancias y enlaces

#### 2. **Ontología - CORREGIDO**
- ✓ **Una sola ontología unificada**: Ahora existe un único archivo `madrid-urban-ontology.ttl` que combina:
  - Módulo de Zonas Verdes (gz:)
  - Módulo de Calidad del Aire (aq:)
  - Relaciones cross-module
- ✓ **Documentación multilingüe**: Labels y comentarios en inglés y español
- ✓ **Metadatos completos**: Incluye información de creación, licencia y autoría

#### 3. **RDF Data - CORREGIDO**
- ✓ **150 instancias de zonas verdes**: Ampliado desde 10 a 150 instancias (> 100 requerido)
- ✓ **Distritos como instancias**: Los distritos ahora son recursos RDF (gz:District) en lugar de strings
- ✓ **Enlaces a Wikidata**: Cada distrito tiene owl:sameAs apuntando a su entidad en Wikidata
- ✓ **Metadatos del dataset**: Incluye información de licencia, fuente y atribución

#### 4. **Entidades vs Strings - CORREGIDO**
- ✓ **Distritos codificados como instancias**: Ahora se usa `gz:inDistrict` (ObjectProperty) además de `gz:district` (DatatypeProperty)
- ✓ **Mejor modelado para linking**: Permite conectar distritos con otras fuentes de datos

---

## 📁 Estructura del Proyecto

```
HandsOn-Group12-Fixed/
├── README.md                          # Este archivo
├── analysis.html                      # ✓ CORREGIDO - Con licencias y estrategia de nombrado
├── csv/                               # Datos originales y procesados
│   ├── Zonas_Verdes_2024.csv         # Dataset original (1632 zonas)
│   ├── zonas-verdes-with-links.csv   # Dataset procesado con URIs
│   └── ...
├── ontology/                          # ✓ CORREGIDO - Una sola ontología unificada
│   ├── madrid-urban-ontology.ttl     # Ontología principal unificada
│   ├── greenzones-example.ttl        # Ejemplos de uso
│   └── air-quality-example.ttl       # Ejemplos de calidad del aire
├── rdf/                               # ✓ CORREGIDO - 150 instancias
│   ├── greenzones-with-links.ttl     # 150 instancias de zonas verdes + 4 distritos
│   ├── queries.sparql                # Queries SPARQL de ejemplo
│   └── queries-with-links.sparql     # Queries con enlaces externos
├── mappings/                          # Mappings RML
├── openrefine/                        # Operaciones OpenRefine
├── requirements/                      # Requisitos del proyecto
└── selfAssessmentHandsOn*.md         # Autoevaluaciones
```

---

## 🔗 URIs y Estrategia de Nombrado

### Base URI
- **Zonas Verdes**: `http://linkeddata.greenzonesmadrid.org/`
- **Calidad del Aire**: `http://linkeddata.airqualitymadrid.org/`

### Ontología
- **Ontología Principal**: `http://linkeddata.greenzonesmadrid.org/ontology/madrid-urban`
- **Módulo Zonas Verdes**: `http://linkeddata.greenzonesmadrid.org/ontology/gz#`
- **Módulo Calidad Aire**: `http://linkeddata.airqualitymadrid.org/ontology/airquality#`

### Recursos (Instancias)
- **Zonas Verdes**: `http://linkeddata.greenzonesmadrid.org/resource/zone/{id}`
  - Ejemplo: `http://linkeddata.greenzonesmadrid.org/resource/zone/1`
- **Distritos**: `http://linkeddata.greenzonesmadrid.org/resource/district/{NOMBRE}`
  - Ejemplo: `http://linkeddata.greenzonesmadrid.org/resource/district/CENTRO`

### Enlaces Externos
- **Wikidata**: `owl:sameAs` apuntando a entidades Wikidata
  - Ejemplo: `<https://www.wikidata.org/entity/Q1763376>` (Distrito Centro)

---

## 📊 Estadísticas del Dataset

- **Total de instancias de Zonas Verdes**: 150
- **Total de Distritos**: 4 (CENTRO, ARGANZUELA, RETIRO, SALAMANCA)
- **Enlaces a Wikidata**: 4 distritos enlazados
- **Propiedades por zona**: 9 (incluyendo ObjectProperty gz:inDistrict)

---

## 📜 Licencias

### Dataset Original
- **Fuente**: Ayuntamiento de Madrid - Portal de Datos Abiertos
- **Licencia**: CC BY 4.0
- **URL**: https://datos.madrid.es/

### Dataset RDF Generado
- **Licencia**: CC BY 4.0
- **Atribución**: "Ayuntamiento de Madrid - Transformado a RDF por Group12 - Curso 2025-2026"
- **URL Licencia**: https://creativecommons.org/licenses/by/4.0/

### Enlaces Wikidata
- **Fuente**: Wikidata
- **Licencia**: CC0 1.0 (Dominio Público)
- **URL**: https://www.wikidata.org/

---

## 🛠️ Tecnologías Utilizadas

- **RDF/Turtle**: Formato de serialización
- **OWL**: Web Ontology Language para la ontología
- **SPARQL**: Lenguaje de consultas
- **RML**: R2RML Mapping Language para transformación
- **OpenRefine**: Limpieza y enriquecimiento de datos
- **Wikidata**: Fuente de enlaces externos

---

## 📝 Notas Importantes

1. **Ontología Unificada**: Ahora hay UN SOLO archivo de ontología que incluye ambos módulos (zonas verdes y calidad del aire)

2. **Instancias Ampliadas**: El archivo RDF contiene 150 instancias (anteriormente 10), cumpliendo con los requisitos

3. **Modelado Mejorado**: Los distritos son ahora instancias de la clase `gz:District`, no solo strings, permitiendo mejor integración y consultas

4. **Documentación Completa**: El archivo `analysis.html` ahora incluye toda la información requerida sobre licencias y estrategia de nombrado

5. **Enlaces Externos**: Cada distrito está enlazado a su correspondiente entidad en Wikidata usando `owl:sameAs`

---

## 🎯 Cumplimiento de Requisitos

| Requisito | Estado | Detalles |
|-----------|--------|----------|
| Licencia datasets seleccionados | ✅ | En analysis.html |
| Licencia dataset a generar | ✅ | En analysis.html |
| Estrategia de nombrado | ✅ | En analysis.html |
| Una sola ontología | ✅ | madrid-urban-ontology.ttl |
| >100 instancias RDF | ✅ | 150 instancias |
| Entidades como instancias | ✅ | Distritos son gz:District |

---

## 👥 Autores

**Group 12 - Curso 2025-2026**
