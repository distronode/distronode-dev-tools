"""Build version text."""
import importlib.metadata


PKGS = [
    "distronode-builder",
    "distronode-dev-tools",
    "distronode-core",
    "distronode-creator",
    "distronode-lint",
    "distronode-navigator",
    "distronode-sign",
    "molecule",
    "pytest-distronode",
    "tox-distronode",
]


def version_builder() -> str:
    """Build a string of formatted versions.

    Returns:
        The versions string
    """
    lines = []
    for pkg in sorted(PKGS):
        version = importlib.metadata.version(pkg)
        lines.append(f"{pkg: <40} {version}")

    return "\n".join(lines)
