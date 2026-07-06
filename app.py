from pyforge.project_analyzer import ProjectAnalyzer


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

        print(
            f"Imports : {len(result['analysis']['imports'])}"
        )

        print(
            f"Classes : {len(result['analysis']['classes'])}"
        )

        print(
            f"Functions : {len(result['analysis']['functions'])}"
        )

    print("\nAnalysis Completed Successfully!")


if __name__ == "__main__":
    main()