from pathlib import Path
from radon.complexity import cc_visit
from radon.metrics import mi_visit


class CodeMetrics:
    """
    Calculates code quality metrics for a Python file.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read_code(self):
        return self.file_path.read_text(encoding="utf-8")

    def get_metrics(self):

        code = self.read_code()

        lines = code.splitlines()

        total_lines = len(lines)

        blank_lines = sum(
            1 for line in lines if not line.strip()
        )

        comment_lines = sum(
            1 for line in lines
            if line.strip().startswith("#")
        )

        complexity = cc_visit(code)

        maintainability = mi_visit(code, multi=True)

        return {
            "total_lines": total_lines,
            "blank_lines": blank_lines,
            "comment_lines": comment_lines,
            "maintainability_index": round(maintainability, 2),
            "complexity": [
                {
                    "name": c.name,
                    "complexity": c.complexity
                }
                for c in complexity
            ]
        }