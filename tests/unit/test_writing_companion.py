"""Verify the independently installable writing package and its dependency closure."""
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "writing-companion"

def test_companion_is_distinct_and_installable():
    portable = json.loads((PACKAGE / "plugin.json").read_text(encoding="utf-8"))
    codex = json.loads((PACKAGE / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    assert portable["name"] == codex["name"] == "egm-writing"
    assert portable["version"] == codex["version"] == "0.2.0"
    assert (PACKAGE / codex["skills"] / "egm-write/SKILL.md").is_file()
    assert portable["name"] != json.loads((ROOT / "plugin.json").read_text())["name"]
    assert not any(k in codex for k in ("hooks", "mcpServers", "apps"))

def test_companion_skill_and_ui_discover_correctly():
    skill = PACKAGE / "skills/egm-write"
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = yaml.safe_load(text.split("---", 2)[1])
    assert front["name"] == "egm-write"
    assert front["description"].startswith("Use when")
    assert len(front["description"]) < 1024
    ui = yaml.safe_load((skill / "agents/openai.yaml").read_text())["interface"]
    assert "$egm-write" in ui["default_prompt"]
    assert 25 <= len(ui["short_description"]) <= 64

def test_all_companion_links_survive_copy_installation(tmp_path):
    import shutil
    installed = tmp_path / "plugin"
    shutil.copytree(PACKAGE, installed)
    for md in installed.rglob("*.md"):
        text = re.sub(r"```[\s\S]*?```", "", md.read_text(encoding="utf-8"))
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "#")):
                continue
            dest = (md.parent / target.split("#")[0]).resolve()
            assert dest.is_relative_to(installed.resolve()), (md, target)
            assert dest.is_file(), (md, target)
    for name in ("evidence", "argument", "reader"):
        assert (installed / f"agents/{name}.md").is_file()
    for name in ("paper", "work", "review-contract", "wallace-wray"):
        assert (installed / f"resources/{name}.md").is_file()
    for manifest in ("plugin.json", ".codex-plugin/plugin.json"):
        obj = json.loads((installed / manifest).read_text())
        interface = obj.get("interface", obj.get("extensions", {}).get("com.openai", {}).get("interface", {}))
        for key in ("logo", "composerIcon"):
            assert (installed / interface[key]).is_file()

def test_fork_catalog_exposes_both_plugins():
    catalog = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    assert catalog["name"] == "egm-writing-fork"
    assert {entry["name"] for entry in catalog["plugins"]} == {"egm", "egm-writing"}
    for entry in catalog["plugins"]:
        package = (ROOT / entry["source"]).resolve()
        assert package.is_relative_to(ROOT)
        assert json.loads((package / ".codex-plugin/plugin.json").read_text())["name"] == entry["name"]


def test_wallace_wray_standard_is_reachable_from_skill_and_every_reader():
    """Installing a standard is insufficient if the loaded prompts cannot reach it."""
    target = (PACKAGE / "resources/wallace-wray.md").resolve()
    starts = [PACKAGE / "skills/egm-write/SKILL.md"] + list((PACKAGE / "agents").glob("*.md"))
    for start in starts:
        pending = [start.resolve()]
        visited = set()
        while pending:
            current = pending.pop()
            if current in visited:
                continue
            visited.add(current)
            content = current.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
                if link.startswith(("https://", "http://", "#")):
                    continue
                linked = (current.parent / link.split("#")[0]).resolve()
                if linked.suffix == ".md" and linked.is_file():
                    pending.append(linked)
        assert target in visited, f"{start} cannot reach the writing standard"
