import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONNECT = ROOT / "scripts" / "connect.py"


class ConnectTests(unittest.TestCase):
    def run_connect(self, target: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CONNECT), "--target", str(target), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_dry_run_does_not_write_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = self.run_connect(target, "--tools", "all", "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Would add 6 file(s)", result.stdout)
            self.assertEqual(list(target.iterdir()), [])

    def test_all_adds_canonical_file_and_adapters(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = self.run_connect(target, "--tools", "all")
            self.assertEqual(result.returncode, 0, result.stderr)
            for relative in (
                "AGENTS.md",
                "CLAUDE.md",
                "GEMINI.md",
                ".github/copilot-instructions.md",
                ".aider.conf.yml",
                ".continue/rules/00-project.md",
            ):
                self.assertTrue((target / relative).is_file(), relative)

    def test_selected_tools_only_install_selected_adapters(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = self.run_connect(target, "--tools", "codex", "claude")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "CLAUDE.md").is_file())
            self.assertFalse((target / "GEMINI.md").exists())
            self.assertFalse((target / ".aider.conf.yml").exists())

    def test_existing_files_are_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            original = "team-owned instructions\n"
            (target / "AGENTS.md").write_text(original, encoding="utf-8")
            result = self.run_connect(target, "--tools", "all")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Kept existing files", result.stdout)
            self.assertEqual((target / "AGENTS.md").read_text(encoding="utf-8"), original)

    def test_missing_target_returns_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "missing"
            result = self.run_connect(target, "--tools", "all")
            self.assertEqual(result.returncode, 2)
            self.assertIn("does not exist", result.stderr)


if __name__ == "__main__":
    unittest.main()
