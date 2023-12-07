"""A runpy entry point for distronode-dev-tools.

This makes it possible to invoke CLI
via :command:`python -m distronode_dev_tools`.
"""

from .cli import main


if __name__ == "__main__":
    main()
