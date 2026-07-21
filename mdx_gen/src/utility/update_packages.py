import subprocess
import tomllib
from pathlib import Path
from typing import Any


def load_pyproject() -> dict[str, Any]:
    with Path("pyproject.toml").open("rb") as f:
        return tomllib.load(f)


def read_deps(proj_data: dict[str, Any]) -> dict[str, str]:
    deps: list[str] = proj_data["project"]["dependencies"]
    deps_map: dict[str, str] = {}
    for dep in deps:
        name, version = dep.split(">")
        deps_map[name] = version
    return deps_map

def read_dev_deps(proj_data: dict[str, Any]) -> dict[str, str]:
    deps: list[str] = proj_data["dependency-groups"]["dev"]
    deps_map: dict[str, str] = {}
    for dep in deps:
        name, version = dep.split(">")
        deps_map[name] = version
    return deps_map

def run_cli(deps: dict[str, str], dev: bool = False) -> None:
    for d, v in deps.items():
      try:
          rm_cli = ["uv", "remove", f"{d}"]
          if dev:
            rm_cli.append("--dev")
          result = subprocess.run(
              rm_cli,
              capture_output=True,
              text=True,
              check=True,
          )
          print(result.stdout)
          print(f"Removed the {d} with version {v}")
          add_cli = ["uv", "add", f"{d}"]
          if dev:
            add_cli.append("--dev")
          result = subprocess.run(
              add_cli,
              capture_output=True,
              text=True,
              check=True,
          )
          print(result.stdout)
          print(f"Added the {d}")
      except subprocess.CalledProcessError as e:
          print(f"An error occurred while running: {e.cmd}")
          print(f"Exit code: {e.returncode}")
          print(f"Error message: {e.stderr}")

def update_deps():
    toml_data = load_pyproject()
    deps = read_deps(toml_data)
    dev_deps = read_dev_deps(toml_data)
    run_cli(deps)
    run_cli(dev_deps, dev=True)


if __name__ == "__main__":
    update_deps()
