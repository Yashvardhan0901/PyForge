from pathlib import Path
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


class ReportGenerator:
    """
    Generates a professional HTML report for PyForge.
    """

    def __init__(self, analysis_data):

        self.analysis_data = analysis_data

    def generate(self):

        template_folder = Path("assets/templates")

        env = Environment(
            loader=FileSystemLoader(template_folder)
        )

        template = env.get_template(
            "report_template.html"
        )

        html = template.render(

            summary=self.analysis_data["summary"],

            files=self.analysis_data["files"],

            top_complex_functions=self.analysis_data[
                "top_complex_functions"
            ],

            code_smells=self.analysis_data[
                "code_smells"
            ],

            generated_time=datetime.now().strftime(
                "%d %B %Y %I:%M %p"
            )

        )

        report_folder = Path("reports")

        report_folder.mkdir(exist_ok=True)

        output_file = report_folder / "analysis_report.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        return output_file