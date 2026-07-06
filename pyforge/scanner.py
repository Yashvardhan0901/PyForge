from pathlib import Path


class ProjectScanner:
    """
    Scans a Python project directory and gathers
    information about its files and folders.
    """

    def __init__(self, project_path):
        """
        Initialize the scanner.

        Args:
            project_path (str): Path to the project directory.
        """

        self.project_path = Path(project_path)

        self.ignored_directories = {
            ".git",
            "venv",
            "__pycache__",
            ".idea",
            ".vscode",
        }

    def scan_project(self):
        """
        Scan the project directory and collect
        information about different file types.
        """

        if not self.project_path.exists():
            raise FileNotFoundError(
                f"Project folder not found: {self.project_path}"
            )

        project_data = {
            "project_name": self.project_path.name,
            "project_path": str(self.project_path),

            "all_files": [],
            "python_files": [],
            "csv_files": [],
            "json_files": [],
            "image_files": [],
            "other_files": [],

            "total_files": 0,
            "total_folders": 0
        }

        # Count folders
        for folder in self.project_path.rglob("*"):

            if folder.is_dir():

                if folder.name in self.ignored_directories:
                    continue

                project_data["total_folders"] += 1

        # Scan files
        for file in self.project_path.rglob("*"):

            if not file.is_file():
                continue

            if any(
                ignored in file.parts
                for ignored in self.ignored_directories
            ):
                continue

            project_data["all_files"].append(file)
            project_data["total_files"] += 1

            suffix = file.suffix.lower()

            if suffix == ".py":
                project_data["python_files"].append(file)

            elif suffix == ".csv":
                project_data["csv_files"].append(file)

            elif suffix == ".json":
                project_data["json_files"].append(file)

            elif suffix in [".png", ".jpg", ".jpeg", ".gif", ".bmp"]:
                project_data["image_files"].append(file)

            else:
                project_data["other_files"].append(file)

        return project_data