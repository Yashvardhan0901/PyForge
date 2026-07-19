from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt


class DependencyGraph:
    """
    Builds an internal dependency graph for the project
    based on project imports.
    """

    def __init__(self, analysis_results):
        self.analysis_results = analysis_results
        self.graph = nx.DiGraph()

    def build_graph(self):
        """
        Build dependency graph using only
        internal project imports.
        """

        project_modules = {
            Path(result["file_name"]).stem: result
            for result in self.analysis_results
        }

        for result in self.analysis_results:

            current_module = Path(result["file_name"]).stem

            imports = result["analysis"]["imports"]

            has_dependency = False

            for imp in imports:

                parts = imp.split(".")

                # Ignore external libraries
                if parts[0] != "pyforge":
                    continue

                if len(parts) < 2:
                    continue

                imported_module = parts[-1]

                if imported_module == current_module:
                    continue

                if imported_module in project_modules:

                    self.graph.add_edge(
                        current_module,
                        imported_module
                    )

                    has_dependency = True

            # Include standalone modules
            if (
                has_dependency
                or result["analysis"]["functions"]
                or result["analysis"]["classes"]
            ):

                self.graph.add_node(current_module)

    def save_graph(self):
        """
        Save dependency graph inside reports folder.
        """

        report_folder = Path("reports")

        report_folder.mkdir(exist_ok=True)

        output_file = report_folder / "dependency_graph.png"

        plt.figure(figsize=(13, 9))

        pos = nx.spring_layout(
            self.graph,
            seed=42,
            k=2.2
        )

        node_colors = []

        for node in self.graph.nodes():

            if node == "app":

                node_colors.append("#F59E0B")

            elif node == "project_analyzer":

                node_colors.append("#22C55E")

            elif node == "streamlit_app":

                node_colors.append("#2563EB")

            else:

                node_colors.append("#7DD3FC")

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color=node_colors,
            node_size=3200,
            edgecolors="black"
        )

        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=10,
            font_weight="bold"
        )

        nx.draw_networkx_edges(
            self.graph,
            pos,
            arrows=True,
            arrowstyle="-|>",
            arrowsize=22,
            width=2,
            edge_color="#6B7280"
        )

        plt.title(
            "PyForge Internal Dependency Graph",
            fontsize=18,
            fontweight="bold"
        )

        plt.axis("off")

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        return output_file