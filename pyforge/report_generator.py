from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class ReportGenerator:

    """
    Generates HTML report using Jinja2.
    """

    def __init__(self, results):

        self.results = results

    def generate(self):

        template_folder = Path("assets/templates")

        env = Environment(
            loader=FileSystemLoader(template_folder)
        )

        template = env.get_template(
            "report_template.html"
        )

        html = template.render(
            total_files=len(self.results),
            files=self.results
        )

        report_folder = Path("reports")

        report_folder.mkdir(
            exist_ok=True
        )

        output_file = report_folder / "analysis_report.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        return output_file