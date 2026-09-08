import json
import re
from pathlib import Path

from jinja2 import Environment, meta
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[2]
repo = json.loads((root / "repo.json").read_text(encoding="utf-8"))
schema = json.loads((root / "schema/template-package.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema)
env = Environment()
known = {
    "user",
    "job_ref",
    "work_exp",
    "cap",
    "system",
    "csv",
    "latex_raw",
    "dump",
    "describe",
    *env.globals.keys(),
}
generation_pattern = re.compile(r"<([A-Za-z_][A-Za-z0-9_]*)(?::(?:text|list))?>")


def unresolved(source: str) -> list[str]:
    ast = env.parse(source)
    values = set(meta.find_undeclared_variables(ast))
    values -= known
    values -= set(generation_pattern.findall(source))
    return sorted(values)


assert repo["repo_version"] == "0.1.0"
assert repo["format_version"] == 1
assert repo["templates"]

for entry in repo["templates"]:
    package_root = root / entry["path"]
    manifest_path = package_root / "template.json"
    assert manifest_path.is_file(), f"missing {manifest_path}"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(manifest), key=lambda error: list(error.path))
    assert not errors, f"{manifest_path}: {errors[0].message if errors else ''}"
    assert manifest["id"] == entry["id"]

    template_path = package_root / manifest["template"]["file"]
    template_source = template_path.read_text(encoding="utf-8")
    section_symbols = [section["symbol"] for section in manifest["sections"]]
    assert unresolved(template_source) == sorted(section_symbols), (
        manifest["id"], "template refs", unresolved(template_source), section_symbols
    )

    for section in manifest["sections"]:
        section_path = package_root / section["file"]
        section_source = section_path.read_text(encoding="utf-8")
        function_symbols = [item["symbol"] for item in section.get("functions", [])]
        assert unresolved(section_source) == sorted(function_symbols), (
            manifest["id"], section["symbol"], unresolved(section_source), function_symbols
        )
        for function in section.get("functions", []):
            function_path = package_root / function["file"]
            function_source = function_path.read_text(encoding="utf-8")
            assert unresolved(function_source) == [], (
                manifest["id"], function["symbol"], unresolved(function_source)
            )

print(f"validated {len(repo['templates'])} template packages")
