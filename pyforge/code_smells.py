from pathlib import Path


class CodeSmellDetector:
    """
    Detects common code smells in a Python project.
    """

    def __init__(self):
        pass

    def detect(self, file_name, analysis, metrics):

        smells = []

        # ----------------------------------
        # Large File
        # ----------------------------------

        if metrics["total_lines"] > 300:

            smells.append({
                "type": "Large File",
                "severity": "High",
                "message": f"{file_name} has {metrics['total_lines']} lines."
            })

        elif metrics["total_lines"] > 200:

            smells.append({
                "type": "Large File",
                "severity": "Medium",
                "message": f"{file_name} has {metrics['total_lines']} lines."
            })

        # ----------------------------------
        # Too Many Functions
        # ----------------------------------

        function_count = len(analysis["functions"])

        if function_count > 20:

            smells.append({
                "type": "Too Many Functions",
                "severity": "Medium",
                "message": f"{file_name} contains {function_count} functions."
            })

        # ----------------------------------
        # Too Many Classes
        # ----------------------------------

        class_count = len(analysis["classes"])

        if class_count > 10:

            smells.append({
                "type": "Too Many Classes",
                "severity": "Medium",
                "message": f"{file_name} contains {class_count} classes."
            })

        # ----------------------------------
        # Low Maintainability
        # ----------------------------------

        mi = metrics["maintainability_index"]

        if mi < 60:

            smells.append({
                "type": "Low Maintainability",
                "severity": "High",
                "message": f"Maintainability Index = {mi}"
            })

        elif mi < 75:

            smells.append({
                "type": "Low Maintainability",
                "severity": "Medium",
                "message": f"Maintainability Index = {mi}"
            })

        # ----------------------------------
        # High Cyclomatic Complexity
        # ----------------------------------

        for item in metrics["complexity"]:

            if item["complexity"] >= 10:

                smells.append({

                    "type": "High Complexity",

                    "severity": "High",

                    "message":
                        f"{item['name']}() has complexity "
                        f"{item['complexity']}"
                })

            elif item["complexity"] >= 7:

                smells.append({

                    "type": "Moderate Complexity",

                    "severity": "Medium",

                    "message":
                        f"{item['name']}() has complexity "
                        f"{item['complexity']}"
                })

        return smells