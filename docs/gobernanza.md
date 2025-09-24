# 🛡️ Políticas de Gobernanza de Datos

Este documento establece las directrices mínimas para garantizar el uso confiable, seguro y trazable de los datos dentro del laboratorio.

---

## 📍 Origen y Linaje de Datos

- Todo archivo procesado debe:
  - Ser guardado en `data/raw/` antes de ser transformado.
  - Contener metadata mínima: nombre de fuente, fecha de carga, formato original.
- El linaje debe ser documentado desde la fuente original hasta la capa Silver.
- Usar nombres consistentes para facilitar el rastreo (`source_<origen>_YYYYMMDD.csv`).

---

## ✅ Validaciones Mínimas

Cada dataset debe pasar por una etapa de validación automática, incluyendo:

- Verificación de tipos de datos esperados.
- Chequeo de nulos en campos clave (`date`, `amount`).
- Rango razonable de fechas (e.g. no fechas futuras).
- Detección de duplicados por clave primaria compuesta (si aplica).
- Conformidad con el esquema canónico (`date`, `partner`, `amount`).

---

## 🔐 Política de Mínimos Privilegios

- Solo los roles responsables de transformación pueden modificar datos en `bronze/` o `silver/`.
- Los datos en `raw/` son de solo lectura. No deben ser editados bajo ningún motivo.
- La app Streamlit accede exclusivamente a `silver/`, nunca a `raw/` o `bronze/`.
- No se almacenan credenciales ni tokens en el repositorio.

---

## 🔎 Trazabilidad y Roles

| Rol               | Responsabilidades                                    |
|------------------|------------------------------------------------------|
| Data Engineer     | Ingesta, validación, transformación y documentación |
| Data Analyst      | Consumo de datos desde `silver/` y creación de KPIs |
| QA/Data Steward   | Revisión de calidad, validaciones, documentación     |

Toda modificación a los datos debe quedar reflejada en:
- Commits con mensajes claros.
- Logs del pipeline (si aplica).
- Actualización del diccionario y checklist de calidad.

---

> 🧠 Recordatorio: La gobernanza no es opcional. Es lo que convierte un experimento en una solución confiable.
