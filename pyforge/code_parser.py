import ast
from pathlib import Path


class CodeParser:
    """
    Parses a Python source file using Python's
    Abstract Syntax Tree (AST).
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read_source_code(self):
        """
        Read the Python source file.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        return self.file_path.read_text(encoding="utf-8")

    def generate_ast(self):
        """
        Generate AST from source code.
        """

        source_code = self.read_source_code()

        return ast.parse(source_code)

    def analyze(self):
        """
        Analyze the Python file and return
        imports, classes and functions.
        """

        tree = self.generate_ast()

        project_info = {
            "imports": [],
            "classes": [],
            "functions": []
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    project_info["imports"].append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    project_info["imports"].append(node.module)

            elif isinstance(node, ast.ClassDef):

                project_info["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):

                project_info["functions"].append(node.name)

        return project_info