from pyforge.project_analyzer import ProjectAnalyzer
from pyforge.dependency import DependencyGraph


def main():
    print("=" * 50)
    print("        Welcome to PyForge")
    print("=" * 50)

    project_path = input("\nEnter project folder path: ")

    analyzer = ProjectAnalyzer(project_path)

    results = analyzer.analyze_project()

    print("\n")
    print("=" * 50)
    print("PROJECT ANALYSIS")
    print("=" * 50)

    print(f"Total Python Files: {len(results)}")

    for result in results:

        print("\n" + "-" * 50)
        print(f"File : {result['file_name']}")

        print(f"Imports : {len(result['analysis']['imports'])}")
        print(f"Classes : {len(result['analysis']['classes'])}")
        print(f"Functions : {len(result['analysis']['functions'])}")

        print(f"Total Lines : {result['metrics']['total_lines']}")
        print(f"Blank Lines : {result['metrics']['blank_lines']}")
        print(f"Comment Lines : {result['metrics']['comment_lines']}")
        print(
            f"Maintainability Index : {result['metrics']['maintainability_index']}"
        )

        print("\nCyclomatic Complexity:")

        if result["metrics"]["complexity"]:

            for func in result["metrics"]["complexity"]:

                print(
                    f"   {func['name']} : {func['complexity']}"
                )

        else:
            print("   No functions found.")

    # Generate Dependency Graph
    graph = DependencyGraph(results)

    graph.build_graph()

    output = graph.save_graph()

    print("\n" + "=" * 50)
    print(f"Dependency Graph Saved As : {output}")

    print("\nAnalysis Completed Successfully!")


if __name__ == "__main__":
    main()