from pyforge.scanner import ProjectScanner
from pyforge.code_parser import CodeParser


class ProjectAnalyzer:
    """
    Analyzes an entire Python project by combining
    the ProjectScanner and CodeParser.
    """

    def __init__(self, project_path):
        self.project_path = project_path

    def analyze_project(self):
        """
        Analyze every Python file in the project.
        """

        scanner = ProjectScanner(self.project_path)

        python_files = scanner.get_python_files()

        analysis_results = []

        for file in python_files:

            parser = CodeParser(file)

            result = parser.analyze()

            analysis_results.append({
                "file_name": file.name,
                "file_path": str(file),
                "analysis": result
            })

        return analysis_results