import subprocess
import tempfile
import os
import shutil
from dataclasses import dataclass

from app.config import get_settings


@dataclass
class RunResult:
    stdout: str
    stderr: str
    exit_code: int
    execution_time_ms: int


def run_python_code(code: str, stdin: str = "") -> RunResult:
    """
    Run Python code safely. Uses Docker sandbox when available, falls back to subprocess.
    """
    settings = get_settings()
    if settings.code_runner_use_docker and _docker_available():
        return _run_docker(code, stdin, settings)
    return _run_subprocess(code, stdin, settings)


def _docker_available() -> bool:
    return shutil.which("docker") is not None


def _run_docker(code: str, stdin: str, settings) -> RunResult:
    with tempfile.TemporaryDirectory() as run_dir:
        temp_path = os.path.join(run_dir, "code.py")
        with open(temp_path, "w", encoding="utf-8") as handle:
            handle.write(code)

        args = [
            "docker", "run", "--rm",
            "--network", "none",
            "--read-only",
            f"--memory={settings.code_runner_memory_limit_mb}m",
            f"--cpus={settings.code_runner_cpu_limit}",
            "--pids-limit", "50",
            "--tmpfs", "/work:rw,nosuid,size=1m",
            "--workdir", "/work",
            "-v", f"{temp_path}:/sandbox/code.py:ro",
            settings.code_runner_image,
            "python3", "/sandbox/code.py",
        ]

        try:
            proc = subprocess.run(
                args,
                input=stdin,
                capture_output=True,
                text=True,
                timeout=settings.code_runner_timeout_seconds,
            )
            return RunResult(
                stdout=proc.stdout,
                stderr=proc.stderr,
                exit_code=proc.returncode,
                execution_time_ms=0,
            )
        except subprocess.TimeoutExpired:
            return RunResult(
                stdout="",
                stderr="Error: Code execution timed out.",
                exit_code=-1,
                execution_time_ms=settings.code_runner_timeout_seconds * 1000,
            )


def _run_subprocess(code: str, stdin: str, settings) -> RunResult:
    with tempfile.TemporaryDirectory() as run_dir:
        temp_path = os.path.join(run_dir, "code.py")
        with open(temp_path, "w", encoding="utf-8") as handle:
            handle.write(code)

        try:
            proc = subprocess.run(
                ["python3", temp_path],
                input=stdin,
                capture_output=True,
                text=True,
                timeout=settings.code_runner_timeout_seconds,
                cwd=run_dir,
            )
            return RunResult(
                stdout=proc.stdout,
                stderr=proc.stderr,
                exit_code=proc.returncode,
                execution_time_ms=0,
            )
        except subprocess.TimeoutExpired:
            return RunResult(
                stdout="",
                stderr="Error: Code execution timed out.",
                exit_code=-1,
                execution_time_ms=settings.code_runner_timeout_seconds * 1000,
            )
