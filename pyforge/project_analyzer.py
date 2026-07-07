from pyforge.scanner import ProjectScanner
from pyforge.code_parser import CodeParser
from pyforge.metrics import CodeMetrics


class ProjectAnalyzer:
    """
    Analyzes an entire Python project by combining
    the ProjectScanner, CodeParser and CodeMetrics.
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

            # Parse the source code
            parser = CodeParser(file)
            analysis = parser.analyze()

            # Calculate code metrics
            metrics = CodeMetrics(file)
            metric_result = metrics.get_metrics()

            analysis_results.append({
                "file_name": file.name,
                "file_path": str(file),
                "analysis": analysis,
                "metrics": metric_result
            })

        return analysis_results