# bigdata-storage-lab-<Sorzano>

## 🧪 Laboratorio Técnico: "De CSVs heterogéneos a un almacén analítico confiable"

### 🎯 Objetivo

El propósito de este laboratorio es construir un flujo de procesamiento de datos que tome archivos CSV heterogéneos como fuente, y los transforme en un almacén analítico robusto, trazable y de calidad. El flujo incluirá las siguientes etapas clave:

1. **Ingesta** de archivos CSV provenientes de diversas fuentes (estructura, codificación, esquema, etc.).
2. **Validación de calidad**: detección de errores estructurales, tipos incorrectos, valores faltantes y duplicados.
3. **Normalización de datos**: unificación de formatos, tipos y esquemas para facilitar su análisis posterior.
4. **Almacenamiento en capas**:
   - **Bronze**: datos crudos (raw) sin procesar, tal como fueron ingeridos.
   - **Silver**: datos limpios, validados y normalizados, listos para análisis.
5. **Exposición de KPIs** a través de una aplicación interactiva usando **Streamlit**, conectada a la capa Silver.

---

### 📦 Entregables

1. **Repositorio público en GitHub** (`bigdata-storage-lab-<apellido>`) que contenga:
   - Código fuente (scripts de ingesta, validación, transformación y carga).
   - Archivos de configuración.
   - Carpeta `docs/` con documentación técnica.
   - Carpeta `notebooks/` opcional para exploraciones o prototipos.
   - README bien estructurado con instrucciones de uso.
2. **Aplicación Streamlit** con visualización de KPIs clave derivados de los datos normalizados.
   - KPIs sugeridos: % de registros válidos, evolución temporal de datos, top entidades (clientes, productos, etc.).
   - Permitir filtrado básico y visualizaciones dinámicas.

---

### ✅ Criterios de Evaluación

| Criterio                         | Detalles                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| **Diseño y justificación técnica** | Claridad en la arquitectura del pipeline, elección de tecnologías, modularidad del código. |
| **Calidad de datos**             | Nivel de limpieza y validación implementado, manejo de casos extremos, cobertura de reglas de negocio. |
| **Trazabilidad y modelado DW**   | Organización en capas (bronze/silver), naming conventions, manejo de metadata y logs. |
| **Documentación**                | README completo, diagramas si aplica, instrucciones reproducibles, comentarios en el código. |
| **Uso adecuado de Streamlit**    | UX básica pero funcional, filtros útiles, KPIs relevantes, conexión efectiva a datos silver. |

---

### ⚠️ Qué NO subir

- 🚫 Archivos que contengan **datos personales, sensibles o confidenciales**.
- 🚫 Claves API, contraseñas o tokens en texto plano.
- 🚫 Archivos binarios innecesarios (.zip, .pyc, .exe, etc.).
- 🚫 Bases de datos completas (solo samples si son necesarias).

Usa archivos de ejemplo anonimizados o generados sintéticamente para pruebas.

---

### ⏱️ Tiempo Estimado por Fase

| Fase                             | Tiempo estimado         |
|----------------------------------|--------------------------|
| Ingesta de CSVs                 | 0.5 días (4 horas)       |
| Validación y profiling          | 1 día                    |
| Normalización + capa Bronze     | 1 día                    |
| Generación de capa Silver       | 1 día                    |
| Desarrollo de KPIs y Streamlit  | 1.5 días                 |
| Documentación y revisión final  | 0.5 días (4 horas)       |
| **Total estimado**              | **5.5 días (~44 horas)** |

---

### 🚀 ¡A trabajar!

Este laboratorio simula un caso real de trabajo con datos desordenados y la necesidad de construir confianza en ellos a través de un pipeline moderno. Usa las herramientas con las que te sientas más cómodo: `pandas`, `pyarrow`, `duckdb`, `pyspark`, `dbt`, etc. Lo importante es **la calidad del flujo y la claridad del resultado**.

> Para cualquier duda técnica, consulta los issues del repo o pregunta a tu instructor.

---
