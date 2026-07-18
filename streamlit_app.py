import streamlit as st
import pandas as pd
from pathlib import Path

from pyforge.project_analyzer import ProjectAnalyzer
from pyforge.dependency import DependencyGraph
from pyforge.report_generator import ReportGenerator

st.set_page_config(
    page_title="PyForge",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 PyForge")
st.subheader("Intelligent Python Code Quality Analyzer")

project_path = st.text_input(
    "Enter Project Folder Path",
    value=""
)

if st.button("Analyze Project"):

    if not project_path:

        st.error("Please enter a project path.")

    elif not Path(project_path).exists():

        st.error("Project path not found.")

    else:

        analyzer = ProjectAnalyzer(project_path)

        analysis_data = analyzer.analyze_project()

        summary = analysis_data["summary"]

        results = analysis_data["files"]

        graph = DependencyGraph(results)
        graph.build_graph()
        graph.save_graph()

        report = ReportGenerator(analysis_data)
        report_path = report.generate()

        st.success("Analysis Completed Successfully!")

        st.divider()

        st.subheader("📊 Project Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Python Files",
            summary["total_files"]
        )

        c2.metric(
            "Classes",
            summary["total_classes"]
        )

        c3.metric(
            "Functions",
            summary["total_functions"]
        )

        c4.metric(
            "Avg Maintainability",
            summary["average_maintainability"]
        )

        st.divider()

        st.subheader("📋 File Analysis")

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

        st.divider()

        st.subheader("🕸 Dependency Graph")

        st.image(
            "dependency_graph.png",
            use_container_width=True
        )

        st.divider()

        st.subheader("📥 Download Report")

        with open(report_path, "rb") as file:

            st.download_button(
                label="Download HTML Report",
                data=file,
                file_name="analysis_report.html",
                mime="text/html"
            )