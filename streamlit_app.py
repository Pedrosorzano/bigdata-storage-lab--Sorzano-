import streamlit as st
import pandas as pd
from io import StringIO

from src.transform import normalize_columns, to_silver
from src.validate import basic_checks
from src.ingest import tag_lineage, concat_bronze

# Configuración de página
st.set_page_config(page_title="Almacén Analítico", layout="wide")

st.title("🧪 Almacén Analítico desde CSVs Heterogéneos")
st.markdown("Sube múltiples archivos CSV, normaliza y valida tus datos, y genera una vista Silver con KPIs.")

# --- Sidebar: Inputs para columnas origen ---
st.sidebar.header("🔧 Configuración de Mapeo de Columnas")
col_date = st.sidebar.text_input("Nombre de columna de fecha", value="fecha")
col_partner = st.sidebar.text_input("Nombre de columna de partner", value="partner")
col_amount = st.sidebar.text_input("Nombre de columna de monto", value="monto")

mapping = {
    col_date: "date",
    col_partner: "partner",
    col_amount: "amount"
}

# --- Carga de archivos ---
uploaded_files = st.file_uploader("📤 Sube uno o más archivos CSV", type="csv", accept_multiple_files=True)

bronze_frames = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.markdown(f"### Archivo: `{uploaded_file.name}`")

        try:
            # Intentar UTF-8 y fallback a Latin-1
            content = uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            content = uploaded_file.read().decode("latin-1")

        df = pd.read_csv(StringIO(content))

        # Normalización y linaje
        df = normalize_columns(df, mapping)
        df = tag_lineage(df, uploaded_file.name)

        # Mostrar vista previa
        st.dataframe(df.head(), use_container_width=True)

        # Validación
        errors = basic_checks(df)
        if errors:
            st.error("❌ Errores de validación:")
            for err in errors:
                st.write(f"- {err}")
        else:
            st.success("✅ Validaciones superadas.")
            bronze_frames.append(df)

# --- Procesamiento global ---
if bronze_frames:
    bronze = concat_bronze(bronze_frames)
    st.markdown("## 🔎 Capa Bronze (unificada)")
    st.dataframe(bronze, use_container_width=True)

    # Derivar capa Silver
    silver = to_silver(bronze)

    st.markdown("## 📊 Capa Silver (agregada por partner y mes)")
    st.dataframe(silver, use_container_width=True)

    # KPIs simples
    total_amount = silver['amount'].sum()
    num_partners = silver['partner'].nunique()
    num_months = silver['month'].nunique()

    st.markdown("### 📌 KPIs")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total €", f"{total_amount:,.2f}")
    kpi2.metric("Partners únicos", num_partners)
    kpi3.metric("Meses registrados", num_months)

    # Gráfico de barras: monto por mes
    st.markdown("### 📈 Monto total por mes")
    chart_df = silver.groupby("month", as_index=False).agg({"amount": "sum"})
    st.bar_chart(chart_df.set_index("month"))

    # Descarga de archivos
    st.markdown("### 📥 Descargas")
    col1, col2 = st.columns(2)

    bronze_csv = bronze.to_csv(index=False).encode("utf-8")
    silver_csv = silver.to_csv(index=False).encode("utf-8")

    col1.download_button("⬇️ Descargar Bronze CSV", bronze_csv, "bronze.csv", "text/csv")
    col2.download_button("⬇️ Descargar Silver CSV", silver_csv, "silver.csv", "text/csv")
else:
    st.info("Sube archivos CSV válidos para procesar los datos.")
