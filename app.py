import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import pydeck as pdk
import altair as alt
import numpy as np
import datetime
import zipfile
import base64
import io
import os


# Para ejecutar, primero en la terminal: pip install -r requirements.txt
# Después: streamlit run app.py


# Configuración de la Página
st.set_page_config(
    layout="wide",       
    initial_sidebar_state="expanded",
    page_title="X", # Escribe el título de la web, ahora por defecto saldría una X
    page_icon="📈", # Escribe el icono que quieres que salga, ahora mismo por defecto saldría este icono: 📈      
)

# CONTENIDO DE LA SIDEBAR
with st.sidebar:
    # 1. Logo (en style='width y height' se puede ajustar), cambiar el logo de la carpeta de assets y que tenga el título de logo
    # Es mejor usar el logo con el fondo transparente. It is better to use a png with a transparent background
    logo_path = "assets/logo.png"
    try:
        with open(logo_path, "rb") as image_file:
            encoded_logo = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-top: 15px; margin-bottom: 40px;">
                <img src="data:image/png;base64,{encoded_logo}" alt="Vanguard Logo" style="width: 140px; height: 140px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-top: 15px; margin-bottom: 40px;
                        width: 70px; height: 70px; background-color: #DDD; border-radius: 10px;
                        align-items: center; font-size: 28px; color: #555; font-weight: bold;">
                L
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
    """
    <style>
        /* Aplica el fondo, ancho y quita scroll */
        section[data-testid="stSidebar"] {
            background-color: #e7f5ff;
            width: 180px;
            overflow: hidden !important;
        }

        /* Fuerza que el contenido interno tampoco tenga scroll */
        section[data-testid="stSidebar"] > div:first-child {
            overflow: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

# Reemplaza el apartado anterior por este si quieres que haya un scroll vertical en la side bar:
# Copia y pega desde st.markdown hasta el paréntesis de cierre y quitale los comentarios
# st.markdown(
#     """
#     <style>
#         section[data-testid="stSidebar"] {
#             background-color: #e7f5ff;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

    # 2. Menú de Opciones
    option_titles_en = [
        "Overview",
        "Interactive Analysis",
        "Statistics",
        "ML/DP",
        "Conclusions",
        "Downloads & Resources",
        "Load & Quick EDA",
        "Settings"
    ]
    
    icons_list = [
        "house-door-fill",
        "bar-chart-line-fill",
        "percent",
        "cpu-fill",
        "clipboard-data-fill",
        "download",
        "folder-fill",
        "gear-fill"
    ]

    selected_title_en = option_menu(
        menu_title=None,
        options=option_titles_en,
        icons=icons_list,
        menu_icon="list", 
        default_index=0,
        orientation="vertical",
        styles={
            "container": { 
                           
                "padding": "5px !important",
                "background-color": "#e7f5ff", # Hacemos que coincida con el fondo de st.sidebar
            },
            "icon": {
                "color": "#0d6efd", 
                "font-size": "24px",
            },
            "nav-link": {
                "font-size": "0px",
                "text-align": "center",
                "margin": "8px 0px",
                "--hover-color": "rgba(13, 110, 253, 0.1)", # Hover sutil sobre el fondo azul claro
                "height": "55px",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "border-radius": "5px",
            },
            "nav-link span": {
                "display": "none !important"
            },
            "nav-link-selected": {
                "background-color": "rgba(13, 110, 253, 0.15)", # Fondo ligeramente más oscuro para seleccionado
            },
             "nav-link-selected .icon": { 
                "color": "#0a58ca !important", # Icono un poco más oscuro en selección
            }
        }
    )

# CONTENIDO PRINCIPAL DE LA PÁGINA
if 'current_page_key' not in st.session_state:
    st.session_state.current_page_key = selected_title_en

if selected_title_en != st.session_state.current_page_key:
    st.session_state.current_page_key = selected_title_en


if st.session_state.current_page_key == "Overview":
    # Título fijo arriba
    st.title("Overview")

    # Inicializamos el slide actual y lo ponemos en la primera slide (0) por defecto
    if "ov_page" not in st.session_state:
        st.session_state.ov_page = 0

    # Botones de navegación
    nav_col1, _, nav_col3 = st.columns([1, 6, 1])
    with nav_col1:
        if st.button("←", disabled=(st.session_state.ov_page == 0)):
            st.session_state.ov_page -= 1
    with nav_col3:
        if st.button("→", disabled=(st.session_state.ov_page == 2)):
            st.session_state.ov_page += 1

    # SLIDE 0: Who Are We?
    if st.session_state.ov_page == 0:
        st.subheader("🧑‍💼 Who Are We?") # O: "🧑‍💼 Who Am I?" si el proyecto es de una persona solo, a modo de ejemplo están marcadas las ciudades de los dos autores, pero se puede poner la ubicación de la empresa, o lo que cada uno crea conveniente
        df = pd.DataFrame([
            {
            "city": "Barcelona", "lat": 41.3851, "lon": 2.1734,
            },
            {
            "city": "Madrid",    "lat": 40.4168, "lon": -3.7038,
            }
        ])

        # Usamos un ScatterplotLayer con puntas rojas tipo chincheta
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["lon", "lat"],
            get_fill_color=[255, 0, 0, 200],  # rojo
            get_radius=20000
        )

        deck = pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=41.0, longitude=0.0, zoom=4.5, pitch=0
            ),
            layers=[layer]
        )
        st.pydeck_chart(deck, use_container_width=True)

        # Enlaces con badges tipo shields.io (están a modo de ejemplo los dos badges de los autores, modificarlo al gusto de cada uno)
        st.markdown("**Connect with us on GitHub:**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                [![Rocío Jiménez](https://img.shields.io/badge/@JimenezRoDA-GitHub-181717?logo=github&style=flat-square)](https://github.com/JimenezRoDA)
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                [![Xavi Fernández](https://img.shields.io/badge/@xavistem-GitHub-181717?logo=github&style=flat-square)](https://github.com/xavistem)
                """,
                unsafe_allow_html=True
            )


    # SLIDE 1: Data Sources & Timeline
    elif st.session_state.ov_page == 1:
        st.subheader("📑 Data Sources & Project Timeline")
        left, right = st.columns(2)
        with left: # Modificar el apartado siguiente, con los df utilizados en tu proyecto
            st.markdown("""
**Data Sources Used**  
- `df_1`  
- `df_2`  
- `df_3`  
- `df_4`  
""")
        with right: #M Modificar este apartado poniendo un calendario solo y marcando el inico y el final, o poner dos, eso ya depende de cada proyecto
            st.markdown("**Project Active Dates**")
            col_a, col_b = st.columns(2)
            with col_a:
                # Phase 1 calendar siempre visible
                st.date_input(
                    "Phase 1: May 19–23, 2025",
                    value=(datetime.date(2025,5,19), datetime.date(2025,5,23)),
                    min_value=datetime.date(2025,5,1),
                    max_value=datetime.date(2025,5,31),
                    key="phase1",
                    label_visibility="collapsed"
                )
            with col_b:
                # Phase 2 calendar siempre visible
                st.date_input(
                    "Phase 2: May 26–30, 2025",
                    value=(datetime.date(2025,5,26), datetime.date(2025,5,30)),
                    min_value=datetime.date(2025,5,1),
                    max_value=datetime.date(2025,5,31),
                    key="phase2",
                    label_visibility="collapsed"
                )

    # SLIDE 2: Texto e imagen
    else: # Modificar el texto según el proyecto, dejar (si se quiere) la parte final de "👉 Join us in this analysis"
        left_col, right_col = st.columns([2, 1])
        with left_col:
            st.markdown("""
    ### 🎯 Title of the objective of the project

    Definition of the company or the project  
    The goal is clear:

    Othe things:
    - X 
    - X

    ---

    #### 📊 Key Metrics Analyzed:
    - X
    - X

    #### 🎯 Success Criterion:
    > **Increase the completion rate by at least 5%.**

    ---

    On this page, we will explore the experiment data, analyze key metrics, identify behavioral patterns, and answer a fundamental question:

    > 🧠 *Firs part of the question  
    > Second part of the question?*

    👉 Join us in this analysis to discover X.
            """)
        with right_col: # Aquí puedes incluir una imagen que pongas en la carpeta de assets y titules image1
            st.image("assets/image1.png", use_container_width=True)


elif st.session_state.current_page_key == "Interactive Analysis":
    st.title("Interactive Analysis")

    # Pestañas principales: Demographics vs KPIs
    demo_tab, kpi_tab = st.tabs(["📊 Demographics", "📈 KPIs"])

    # Demographics: un único dashboard con tus 4 visualizaciones
    with demo_tab:
        st.subheader("Demographics Overview")
        components.iframe(
            "https://public.tableau.com/views/Clients_17485213608790/Dashboard1"
            "?:language=es-ES&publish=yes&:showVizHome=no&:embed=y",
            height=700,
            scrolling=True,
        )

    # KPIs: sub-pestañas para cada uno de los 4 dashboards
    with kpi_tab:
        st.subheader("Key Performance Indicators")
        kpi_subtabs = kpi_tab.tabs([
            "Completion Rate",
            "First-Time Completion",
            "Time Invested",
            "Error Rate"
        ])

        # 1️⃣ Completion Rate
        with kpi_subtabs[0]:
            st.markdown("#### Completion Rate")
            components.iframe(
                "https://public.tableau.com/views/Insights_17485215898210/CompletionRate"
                "?:language=es-ES&publish=yes&:showVizHome=no&:embed=y",
                height=650,
                scrolling=True,
            )

            # Robot: Completion Rate
            html_code = """
            <style>
            .tooltip {
              position: relative;
              display: inline-block;
              cursor: pointer;
            }
            .tooltip .tooltiptext {
              visibility: hidden;
              width: 220px;
              background-color: #555;
              color: #fff;
              text-align: center;
              border-radius: 6px;
              padding: 5px 8px;
              position: absolute;
              z-index: 1;
              bottom: 125%;
              left: 50%;
              margin-left: -110px;
              opacity: 0;
              transition: opacity 0.3s;
              font-size: 14px;
              pointer-events: none;
              white-space: nowrap;
            }
            .tooltip:hover .tooltiptext {
              visibility: visible;
              opacity: 1;
            }
            .tooltip .tooltiptext::after {
              content: "";
              position: absolute;
              top: 100%;
              left: 50%;
              margin-left: -5px;
              border-width: 5px;
              border-style: solid;
              border-color: #555 transparent transparent transparent;
            }
            </style>
            <script
              src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs"
              type="module"
            ></script>
            <div class="tooltip">
              <dotlottie-player
                src="https://lottie.host/24393e73-f3c0-43bc-b296-3695056055a6/rnxrzeYROf.lottie"
                background="transparent"
                speed="1"
                style="width: 150px; height: 150px;"
                loop
                autoplay
              ></dotlottie-player>
              <span class="tooltiptext">Click to see the hypothesis results</span>
            </div>
            """
            components.html(html_code, height=180)
            if st.button("Show hypothesis results", key="hypo1"):
                st.markdown("""
**H₀**: completion_rate(Control) = completion_rate(Test)  
**H₁**: completion_rate(Control) ≠ completion_rate(Test)  
We rejected **H₀**, so the difference is significant.  
However, the increase is below the **+5% threshold**, so it doesn’t meet the business criterion.
                """)

        # 2️⃣ Completion Rate at the First Time
        with kpi_subtabs[1]:
            st.markdown("#### Completion Rate at the First Time")
            components.iframe(
                "https://public.tableau.com/views/Completion_17485219424030/Firsttime"
                "?:language=es-ES&publish=yes&:showVizHome=no&:embed=y",
                height=650,
                scrolling=True,
            )

            # Robot: First Attempt Success
            components.html(html_code.replace(
                "Click to see the hypothesis results",
                "Click to see first attempt success results"
            ), height=180)
            if st.button("Show hypothesis results", key="hypo2"):
                st.markdown("""
**H₀**: first_attempt_success(Control) = first_attempt_success(Test)  
**H₁**: first_attempt_success(Control) ≠ first_attempt_success(Test)  
We performed the test and rejected **H₀**.  
✅ So, the difference in first attempt success rate is statistically significant.  
Although more users in the Test group completed the process, the success rate on the first attempt was **lower** than in the Control group (**43.67% vs. 47.39%**).
                """)

        # 3️⃣ Time Invested
        with kpi_subtabs[2]:
            st.markdown("#### Time Invested")
            components.iframe(
                "https://public.tableau.com/views/Timeinvested/Timeinvested"
                "?:language=es-ES&publish=yes&:showVizHome=no&:embed=y",
                height=650,
                scrolling=True,
            )

            # Robot: UX Insights
            components.html(html_code.replace(
                "Click to see the hypothesis results",
                "Click to see UX performance insights"
            ), height=180)
            if st.button("Show hypothesis results", key="hypo3"):
                st.markdown("""
**UX Insights**:  
• Test starts faster → less initial friction  
• Test slower at step_1 & confirm → +5s and +23s (not significant)  
• Big speedup at step_3 (**+7s**, highly significant)  
• Mixed results: some steps better, others worse  
• Statistically solid effects, but overall UX needs review
                """)

        # 4️⃣ Error Rate
        with kpi_subtabs[3]:
            st.markdown("#### Error Rate")
            components.iframe(
                "https://public.tableau.com/views/Errorrate_17485220756100/ErrorRate"
                "?:language=es-ES&publish=yes&:showVizHome=no&:embed=y",
                height=650,
                scrolling=True,
            )

            # Robot: Error Rate
            components.html(html_code.replace(
                "Click to see the hypothesis results",
                "Click to see error rate results"
            ), height=180)
            if st.button("Show hypothesis results", key="hypo4"):
                st.markdown("""
**H₀**: error_rate(Control) ≤ error_rate(Test)  
**H₁**: error_rate(Control) > error_rate(Test)  
We performed the test and rejected **H₀**.  
✅ So, the global error rate in **Control** is significantly higher than in **Test**.  
Control had an error rate of **0.19%**, while Test reduced this to **0.07%**, indicating a clear improvement in the new design’s performance.
                """)


elif st.session_state.current_page_key == "Statistics":
    st.title("Statistics")

elif st.session_state.current_page_key == "ML/DP": # Si solo hay ML, quitar lo de DP
    st.title("ML / Deep Learning")
    
elif st.session_state.current_page_key == "Conclusions":
    st.title("🔍 Conclusions")

    # Mete este apartado dentro de un expander para que no resulte abrumador a primera vista, cambiar el texto según el proyecto / Wrap in an expander so it's not overwhelming at first glance
    # Ahora mismo hay unos subapartados sugeridos, pero se puede escribir o incluir lo que quiera el usuario
    with st.expander("Show Summary of Findings", expanded=False):
        st.markdown("""
This (**Test group**) has shown **statistically significant improvements** in..., but it **does not fully meet all operational effectiveness criteria** defined by X.  
Below is a summary of the final trade-off between the two versions:
""")

        # Clear Advantages
        st.markdown("### ✅ Clear Advantages of the Test Group")
        st.markdown("""
- **X**:   
- **X**:  
- **Critical “confirm” step errors** reduced from x to x
  > +0.5 pp improvement, 
""")

        # Limitations
        st.markdown("### ⚠️ Limitations of the Test Group")
        st.markdown("""
- **X**: 43.7% vs. 47.4%  
  > Indicates...  
- **X**  
  > X → X 
- **X** in... 
  - Xds  
  - X 
  > X  
""")

        # Hypotheses & Business Considerations
        st.markdown("### 🧠 Hypotheses & Business Considerations")
        st.markdown("""
- Some improvements...  
  > e.g.   
- **Exception**:   
""")

        # Final Recommendation
        st.markdown("### 🧭 Final Recommendation")
        st.markdown("""
It is recommended to **X**:

> - X  
> - X
> - X

Final comment **x**, **x**, and **x**  
""")


elif st.session_state.current_page_key == "Downloads & Resources": 

# Este apartado es para quien no haya asistido o quiera más información, se pueda descargar un resumen y todos los datos limpios y procesados
# En este caso, el código está preparado para descargar lo que hay a modo de ejemplo dentro de la carpeta de data, la subcarpeta de reports (hay 2 pdfs) y las subcarpetas de raw y processed (con df a modo de ejemplo)
# Hay que ir las subcarpetas de reports, processed y raw, cambiar esos archivos por los nuevos (en los reports manenter el mismo nombre, en los de data processed/raw adatpar el código al nuevo nombre)
# Ahora mismo hay dos pdf, 3 archivos en processed y 4 en raw, son de otro proyecto a modo de ejemplo, pero habría que reemplzarlo todo

    st.title("📂 Downloads & Resources")

    # 1️⃣ Executive Summary Reports
    st.markdown("### 📄 Executive Summary Reports")
    st.markdown(
        """
        For those who couldn't attend the live presentation—or anyone who wants a quick, formal
        overview—please select your preferred language and download the concise executive summary.
        """
    )

    # Language selector
    lang = st.selectbox("Choose report language", ["English", "Español"])

    # Base path para los reports
    report_base = os.path.join("data", "reports")

    if lang == "English":
        report_path = os.path.join(report_base, "Executive_Summary_EN.pdf")
        with open(report_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📥 Download Executive Summary (English)",
            data=pdf_bytes,
            file_name="Vanguard_Digital_Redesign_Summary_EN.pdf",
            mime="application/pdf",
        )
    else:
        report_path = os.path.join(report_base, "Executive_Summary_ES.pdf")
        with open(report_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📥 Descargar Resumen Ejecutivo (Español)",
            data=pdf_bytes,
            file_name="Vanguard_Digital_Redesign_Resumen_ES.pdf",
            mime="application/pdf",
        )

    st.markdown("---")

    # 2️⃣ Data Downloads
    st.markdown("### 🗄️ Data Downloads")
    st.markdown(
        """
        You can download the raw and processed datasets used in our analysis.  
        - **Raw**: Original exported tables, before any cleaning.  
        - **Processed**: Final cleaned and joined tables ready for analysis.
        """
    )

    # Helper para comprimir cualquier carpeta en memoria
    def zip_folder_to_bytes(folder_path):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=folder_path)
                    z.write(file_path, arcname=arcname)
        buffer.seek(0)
        return buffer.read()

    # Raw data
    raw_zip = zip_folder_to_bytes(os.path.join("data", "raw"))
    st.download_button(
        label="📥 Download Raw Data (ZIP)",
        data=raw_zip,
        file_name="vanguard_raw_data.zip",
        mime="application/zip",
    )

    # Processed data
    processed_zip = zip_folder_to_bytes(os.path.join("data", "processed"))
    st.download_button(
        label="📥 Download Processed Data (ZIP)",
        data=processed_zip,
        file_name="vanguard_processed_data.zip",
        mime="application/zip",
    )

    st.markdown( # Cambiar este apartado y poner, si se quiere, el nombre de la nueva empresa en vez del nombre que viene por defecto que es X
        """
        ---
        *These datasets are provided under internal X use—please do not redistribute.*
        """
    )


elif st.session_state.current_page_key == "Load & Quick EDA":
    st.title("Load & Quick EDA")


elif st.session_state.current_page_key == "Settings":
    st.title("Settings")


else:
    st.write("Welcome to Vanguard Analytics. Please select an option.")
