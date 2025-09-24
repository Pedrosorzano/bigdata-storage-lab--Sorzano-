# 📘 Diccionario de Datos Canónico

Este diccionario define el **esquema canónico** que se utilizará como base para la capa **Silver** del almacén analítico. Todos los datos normalizados deben adherirse a esta estructura para garantizar uniformidad, interoperabilidad y calidad analítica.

## 🧩 Esquema Canónico

| Campo     | Tipo       | Formato         | Descripción                                        |
|-----------|------------|-----------------|----------------------------------------------------|
| date      | `date`     | `YYYY-MM-DD`    | Fecha del evento, transacción o registro           |
| partner   | `string`   | libre (UTF-8)   | Nombre del socio, cliente o proveedor              |
| amount    | `float`    | Decimales (EUR) | Valor monetario de la operación (en euros)         |

---

## 🔄 Mapeos de Campos: Origen → Canónico

La siguiente tabla ilustra cómo distintos nombres de campos, provenientes de fuentes heterogéneas, se mapean al esquema canónico.

| Fuente        | Campo Origen     | Campo Canónico | Transformación requerida           |
|---------------|------------------|----------------|------------------------------------|
| sistema_A     | fecha_operacion  | date           | Formato `DD/MM/YYYY → YYYY-MM-DD` |
| sistema_B     | partner_name     | partner        | Ninguna                            |
| sistema_C     | importe_total    | amount         | Reemplazar `,` por `.`             |
| excel_manual  | Fecha            | date           | Inferir formato                    |
| API_XYZ       | vendor           | partner        | Renombrar                          |
| csv_legacy    | total_eur        | amount         | Cast a `float`                     |

> 💡 Estos mapeos deben registrarse y mantenerse actualizados en cada pipeline de transformación.
