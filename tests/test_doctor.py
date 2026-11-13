import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONNECT = ROOT / "scripts" / "connect.py"
DOCTOR = ROOT / "scripts" / "doctor.py"


class DoctorTests(unittest.TestCase):
    def run_script(self, script: Path, target: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), "--target", str(target), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_missing_canonical_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_script(DOCTOR, Path(temp))
            self.assertEqual(result.returncode, 1)
            self.assertIn("AGENTS.md is missing", result.stdout)

    def test_direct_agents_tools_work_without_optional_adapters(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "AGENTS.md").write_text("# Project rules\n", encoding="utf-8")
            result = self.run_script(DOCTOR, target)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("[NOT-INSTALLED] Claude Code", result.stdout)
            self.assertIn("[CONNECTED] Codex, Cursor, Cline, Windsurf", result.stdout)

    def test_installed_adapters_are_recognized(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            installed = self.run_script(CONNECT, target, "--tools", "all")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            result = self.run_script(DOCTOR, target)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("[CONNECTED] Claude Code", result.stdout)
            self.assertIn("[CONNECTED] Gemini CLI", result.stdout)
            self.assertIn("[CONNECTED] Aider", result.stdout)

    def test_broken_adapter_is_reported_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            installed = self.run_script(CONNECT, target, "--tools", "claude")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            claude_file = target / "CLAUDE.md"
            claude_file.write_text("# Independent instructions\n", encoding="utf-8")
            before = claude_file.read_text(encoding="utf-8")
            result = self.run_script(DOCTOR, target)
            self.assertEqual(result.returncode, 1)
            self.assertIn("[REVIEW] Claude Code", result.stdout)
            self.assertEqual(claude_file.read_text(encoding="utf-8"), before)

    def test_json_output_is_machine_readable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "AGENTS.md").write_text("# Project rules\n", encoding="utf-8")
            result = self.run_script(DOCTOR, target, "--json")
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertTrue(report["ok"])
            self.assertEqual(report["canonical_file"], "AGENTS.md")


if __name__ == "__main__":
    unittest.main()
