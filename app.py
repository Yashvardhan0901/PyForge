from pyforge.project_analyzer import ProjectAnalyzer
from pyforge.dependency import DependencyGraph
from pyforge.report_generator import ReportGenerator


def main():

    print("=" * 60)
    print("          Welcome to PyForge")
    print("=" * 60)

    project_path = input("\nEnter project folder path: ")

    analyzer = ProjectAnalyzer(project_path)

    analysis_data = analyzer.analyze_project()

    summary = analysis_data["summary"]
    results = analysis_data["files"]

    print("\n")
    print("=" * 60)
    print("PROJECT SUMMARY")
    print("=" * 60)

    print(f"Python Files           : {summary['total_files']}")
    print(f"Classes               : {summary['total_classes']}")
    print(f"Functions             : {summary['total_functions']}")
    print(f"Imports               : {summary['total_imports']}")
    print(
        f"Average Maintainability : {summary['average_maintainability']}"
    )

    print("\n")
    print("=" * 60)
    print("FILE ANALYSIS")
    print("=" * 60)

    for result in results:

        print("\n" + "-" * 60)

        print(f"File : {result['file_name']}")

        print(f"Imports : {len(result['analysis']['imports'])}")
        print(f"Classes : {len(result['analysis']['classes'])}")
        print(f"Functions : {len(result['analysis']['functions'])}")

        print(f"Total Lines : {result['metrics']['total_lines']}")
        print(f"Blank Lines : {result['metrics']['blank_lines']}")
        print(f"Comment Lines : {result['metrics']['comment_lines']}")
        print(
            f"Maintainability : {result['metrics']['maintainability_index']}"
        )

    graph = DependencyGraph(results)

    graph.build_graph()

    graph.save_graph()

    report = ReportGenerator(analysis_data)

    report_path = report.generate()

    print("\n")
    print("=" * 60)
    print("OUTPUT")
    print("=" * 60)

    print("Dependency Graph : dependency_graph.png")
    print(f"HTML Report      : {report_path}")

    print("\nAnalysis Completed Successfully!")


if __name__ == "__main__":
    main()