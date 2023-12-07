# Distronode automation developer tools

The `distronode-dev-tools` python package provides an easy way to install and discover the best tools available to create and test distronode content.

The curated list of tools installed as part of the Distronode automation developer tools package includes:

[distronode-core](https://github.com/distronode/distronode): Distronode is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems.

[distronode-builder](https://github.com/distronode/distronode-builder): Distronode Builder is a tool that automates the process of building execution environments using the schemas and tooling defined in various Distronode Collections and by the user.

[distronode-creator](https://github.com/distronode/distronode-creator): The fastest way to generate all your distronode content!

[distronode-lint](https://github.com/distronode/distronode-lint): Checks playbooks for practices and behavior that could potentially be improved.

[distronode-navigator](https://github.com/distronode/distronode-navigator) A text-based user interface (TUI) for Distronode.

[distronode-sign](https://github.com/distronode/distronode-sign): Utility for signing and verifying Distronode project directory contents.

[molecule](https://github.com/distronode/molecule): Molecule aids in the development and testing of Distronode content: collections, playbooks and roles

[pytest-distronode](https://github.com/distronode/pytest-distronode): A pytest plugin that enables the use of distronode in tests, enables the use of pytest as a collection unit test runner, and exposes molecule scenarios using a pytest fixture.

[tox-distronode](https://github.com/distronode/tox-distronode): The tox-distronode plugin dynamically creates a full matrix of python interpreter and distronode-core version environments for running integration, sanity, and unit for an distronode collection both locally and in a Github action. tox virtual environments are leveraged for collection building, collection installation, dependency installation, and testing.

## Installation

`python -m pip install distronode-dev-tools`

## Usage

In addition to installing each of the above tools, `distronode-dev-tools` provides an easy way to show the versions of the content creation tools that make up the current development environment.

```
$ adt --version
distronode-builder                          3.0.0
distronode-core                             2.16.0
distronode-creator                          1.0.0
distronode-dev-tools                        1.0.0
distronode-lint                             6.22.0
distronode-navigator                        3.5.0
distronode-sign                             0.1.1
molecule                                 6.0.2
pytest-distronode                           4.1.1
tox-distronode                              2.0.14
```
