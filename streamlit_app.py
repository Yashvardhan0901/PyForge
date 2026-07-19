import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from pyforge.project_analyzer import ProjectAnalyzer
from pyforge.dependency import DependencyGraph
from pyforge.report_generator import ReportGenerator

st.set_page_config(
    page_title="PyForge",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main{
    background:#f8fafc;
}

.metric-card{
    background:white;
    padding:18px;
    border-radius:12px;
    box-shadow:0 3px 12px rgba(0,0,0,.08);
    text-align:center;
}

h1,h2,h3{
    color:#1f2937;
}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.title("🔥 PyForge")

st.caption(
    "Professional Python Static Code Analyzer"
)

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.header("Project")

    project_path = st.text_input(
        "Project Folder",
        value=""
    )

    analyze = st.button(
        "Analyze Project",
        use_container_width=True
    )

if not analyze:

    st.info("Enter project path and click Analyze Project.")

    st.stop()

# -----------------------------
# VALIDATION
# -----------------------------

if not Path(project_path).exists():

    st.error("Project path not found.")

    st.stop()

# -----------------------------
# ANALYSIS
# -----------------------------

analyzer = ProjectAnalyzer(project_path)

analysis_data = analyzer.analyze_project()

summary = analysis_data["summary"]

results = analysis_data["files"]

complexity = analysis_data["top_complex_functions"]

smells = analysis_data["code_smells"]

graph = DependencyGraph(results)

graph.build_graph()

graph_path = graph.save_graph()

report = ReportGenerator(analysis_data)

report_path = report.generate()

st.success("Analysis Completed Successfully!")
# ==========================================================
# KPI SECTION
# ==========================================================

st.divider()

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "📁 Files",
    summary["total_files"]
)

col2.metric(
    "🏛 Classes",
    summary["total_classes"]
)

col3.metric(
    "⚙ Functions",
    summary["total_functions"]
)

col4.metric(
    "📦 Imports",
    summary["total_imports"]
)

col5.metric(
    "📈 Maintainability",
    summary["average_maintainability"]
)

col6.metric(
    "⚠ Code Smells",
    summary["total_code_smells"]
)

st.divider()

# ==========================================================
# HEALTH SCORE
# ==========================================================

st.subheader("❤️ Project Health")

health = summary["health_score"]

if health >= 90:

    st.success(
        f"Excellent Project ({health}/100)"
    )

elif health >= 80:

    st.info(
        f"Good Project ({health}/100)"
    )

elif health >= 70:

    st.warning(
        f"Fair Project ({health}/100)"
    )

else:

    st.error(
        f"Needs Improvement ({health}/100)"
    )

st.progress(health / 100)

st.divider()

# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "📋 File Analysis",

        "📊 Charts",

        "🏆 Complexity",

        "⚠ Code Smells",

        "🕸 Dependency Graph"

    ]

)

# ==========================================================
# FILE ANALYSIS
# ==========================================================

with tab1:

    rows = []

    for result in results:

        rows.append(

            {

                "File": result["file_name"],

                "Imports": len(result["analysis"]["imports"]),

                "Classes": len(result["analysis"]["classes"]),

                "Functions": len(result["analysis"]["functions"]),

                "LOC": result["metrics"]["total_lines"],

                "Maintainability": result["metrics"]["maintainability_index"]

            }

        )

    df = pd.DataFrame(rows)

    st.dataframe(

        df,

        use_container_width=True

    )
    # ==========================================================
# CHARTS
# ==========================================================

with tab2:

    st.subheader("Project Statistics")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        fig = px.bar(
            df,
            x="File",
            y="LOC",
            title="Lines of Code per File",
            text="LOC"
        )

        fig.update_layout(
            xaxis_title="Python File",
            yaxis_title="Lines of Code"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart_col2:

        fig = px.bar(
            df,
            x="File",
            y="Maintainability",
            title="Maintainability Index",
            text="Maintainability"
        )

        fig.update_layout(
            xaxis_title="Python File",
            yaxis_title="Maintainability"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    fig = px.pie(
        values=[
            summary["total_classes"],
            summary["total_functions"],
            summary["total_imports"]
        ],
        names=[
            "Classes",
            "Functions",
            "Imports"
        ],
        title="Project Composition"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# TOP COMPLEX FUNCTIONS
# ==========================================================

with tab3:

    st.subheader("Top 10 Most Complex Functions")

    if complexity:

        complexity_df = pd.DataFrame(complexity)

        complexity_df.columns = [
            "File",
            "Function",
            "Complexity"
        ]

        st.dataframe(
            complexity_df,
            use_container_width=True
        )

        fig = px.bar(
            complexity_df,
            x="Function",
            y="Complexity",
            color="Complexity",
            title="Cyclomatic Complexity"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.success("No complex functions found.")
        # ==========================================================
# CODE SMELLS
# ==========================================================

with tab4:

    st.subheader("Detected Code Smells")

    if smells:

        smell_df = pd.DataFrame(smells)

        st.dataframe(
            smell_df,
            use_container_width=True
        )

        severity_counts = (
            smell_df["severity"]
            .value_counts()
            .reset_index()
        )

        severity_counts.columns = [
            "Severity",
            "Count"
        ]

        fig = px.bar(
            severity_counts,
            x="Severity",
            y="Count",
            color="Severity",
            title="Code Smell Severity Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.success("🎉 No code smells detected.")

# ==========================================================
# DEPENDENCY GRAPH
# ==========================================================

with tab5:

    st.subheader("Project Dependency Graph")

    graph_path = Path("reports/dependency_graph.png")

    if graph_path.exists():

        st.image(
        str(graph_path),
        width="stretch"
    )

    else:

        st.info("Dependency graph not available.")

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.divider()

st.subheader("📄 HTML Report")

try:

    with open(report_path, "rb") as report_file:

        st.download_button(
            label="⬇ Download HTML Report",
            data=report_file,
            file_name="PyForge_Report.html",
            mime="text/html",
            use_container_width=True
        )

except Exception as e:

    st.error(f"Unable to load report: {e}")

# ==========================================================
# PROJECT SUMMARY
# ==========================================================

st.divider()

with st.expander("📌 Project Summary"):

    st.write(f"**Total Files:** {summary['total_files']}")
    st.write(f"**Total Classes:** {summary['total_classes']}")
    st.write(f"**Total Functions:** {summary['total_functions']}")
    st.write(f"**Total Imports:** {summary['total_imports']}")
    st.write(f"**Average Maintainability:** {summary['average_maintainability']}")
    st.write(f"**Average Complexity:** {summary['average_complexity']}")
    st.write(f"**Health Score:** {summary['health_score']}/100")
    st.write(f"**Code Smells:** {summary['total_code_smells']}")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🔥 PyForge | Python Static Code Analyzer | Developed using Python, Streamlit, AST & Plotly"
)