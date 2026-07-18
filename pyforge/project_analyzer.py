from pyforge.scanner import ProjectScanner
from pyforge.code_parser import CodeParser
from pyforge.metrics import CodeMetrics


class ProjectAnalyzer:
    """
    Analyzes an entire Python project and returns
    both file-wise analysis and project summary.
    """

    def __init__(self, project_path):
        self.project_path = project_path

    def analyze_project(self):

        scanner = ProjectScanner(self.project_path)

        python_files = scanner.get_python_files()

        analysis_results = []

        total_classes = 0
        total_functions = 0
        total_imports = 0
        maintainability_scores = []

        for file in python_files:

            parser = CodeParser(file)
            analysis = parser.analyze()

            metrics = CodeMetrics(file)
            metric_result = metrics.get_metrics()

            total_classes += len(analysis["classes"])
            total_functions += len(analysis["functions"])
            total_imports += len(analysis["imports"])

            maintainability_scores.append(
                metric_result["maintainability_index"]
            )

            analysis_results.append(
                {
                    "file_name": file.name,
                    "file_path": str(file),
                    "analysis": analysis,
                    "metrics": metric_result,
                }
            )

        average_mi = (
            round(
                sum(maintainability_scores)
                / len(maintainability_scores),
                2,
            )
            if maintainability_scores
            else 0
        )

        return {
            "summary": {
                "total_files": len(analysis_results),
                "total_classes": total_classes,
                "total_functions": total_functions,
                "total_imports": total_imports,
                "average_maintainability": average_mi,
            },
            "files": analysis_results,
        }