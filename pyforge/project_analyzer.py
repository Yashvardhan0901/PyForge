from pyforge.scanner import ProjectScanner
from pyforge.code_parser import CodeParser
from pyforge.metrics import CodeMetrics
from pyforge.code_smells import CodeSmellDetector


class ProjectAnalyzer:
    """
    Performs complete analysis of a Python project.
    """

    def __init__(self, project_path):
        self.project_path = project_path

    def analyze_project(self):

        scanner = ProjectScanner(self.project_path)
        python_files = scanner.get_python_files()

        smell_detector = CodeSmellDetector()

        results = []

        total_classes = 0
        total_functions = 0
        total_imports = 0
        total_lines = 0
        total_blank = 0
        total_comments = 0

        maintainability_scores = []
        complexity_scores = []
        top_complex_functions = []
        all_smells = []

        for file in python_files:

            parser = CodeParser(file)
            analysis = parser.analyze()

            metrics = CodeMetrics(file)
            metric = metrics.get_metrics()

            smells = smell_detector.detect(
                file.name,
                analysis,
                metric
            )

            total_classes += len(analysis["classes"])
            total_functions += len(analysis["functions"])
            total_imports += len(analysis["imports"])

            total_lines += metric["total_lines"]
            total_blank += metric["blank_lines"]
            total_comments += metric["comment_lines"]

            maintainability_scores.append(
                metric["maintainability_index"]
            )

            for item in metric["complexity"]:

                complexity_scores.append(item["complexity"])

                top_complex_functions.append(
                    {
                        "file": file.name,
                        "function": item["name"],
                        "complexity": item["complexity"],
                    }
                )

            all_smells.extend(smells)

            results.append(
                {
                    "file_name": file.name,
                    "file_path": str(file),
                    "analysis": analysis,
                    "metrics": metric,
                    "code_smells": smells,
                }
            )

        average_mi = round(
            sum(maintainability_scores) / len(maintainability_scores),
            2
        ) if maintainability_scores else 0

        average_complexity = round(
            sum(complexity_scores) / len(complexity_scores),
            2
        ) if complexity_scores else 0

        top_complex_functions = sorted(
            top_complex_functions,
            key=lambda x: x["complexity"],
            reverse=True
        )[:10]

        if average_mi >= 90:
            health_score = 100
            health_status = "Excellent"
        elif average_mi >= 80:
            health_score = 90
            health_status = "Good"
        elif average_mi >= 70:
            health_score = 80
            health_status = "Fair"
        else:
            health_score = 60
            health_status = "Needs Improvement"

        summary = {
            "total_files": len(results),
            "total_classes": total_classes,
            "total_functions": total_functions,
            "total_imports": total_imports,
            "total_lines": total_lines,
            "total_blank": total_blank,
            "total_comments": total_comments,
            "average_maintainability": average_mi,
            "average_complexity": average_complexity,
            "health_score": health_score,
            "health_status": health_status,
            "total_code_smells": len(all_smells),
        }

        return {
            "summary": summary,
            "files": results,
            "top_complex_functions": top_complex_functions,
            "code_smells": all_smells,
        }