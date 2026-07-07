from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt


class DependencyGraph:
    """
    Builds a dependency graph for the project based
    on internal Python imports.
    """

    def __init__(self, analysis_results):
        self.analysis_results = analysis_results
        self.graph = nx.DiGraph()

    def build_graph(self):
        """
        Build dependency graph using only
        internal project imports.
        """

        # Store all project modules
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

                # Ignore third-party imports
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

            # Add isolated node only if it contains code
            if (
                has_dependency
                or result["analysis"]["functions"]
                or result["analysis"]["classes"]
            ):
                self.graph.add_node(current_module)

    def save_graph(self, output_file="dependency_graph.png"):
        """
        Save dependency graph as PNG.
        """

        plt.figure(figsize=(13, 9))

        pos = nx.spring_layout(
            self.graph,
            seed=42,
            k=2.2
        )

        # Highlight app.py
        node_colors = []

        for node in self.graph.nodes():

            if node == "app":
                node_colors.append("orange")

            elif node == "project_analyzer":
                node_colors.append("lightgreen")

            else:
                node_colors.append("skyblue")

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color=node_colors,
            node_size=3000,
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
            edge_color="gray"
        )

        plt.title(
            "PyForge Internal Dependency Graph",
            fontsize=16,
            fontweight="bold"
        )

        plt.axis("off")

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        return output_file