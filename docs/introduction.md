# Distronode Development Tools (ADT)

## Introduction

Distronode Development Tools or ADT for short, aims to streamline the setup and usage of several tools needed in order to create [Distronode] content.
When it comes to creating automation content using Distronode, there are several packages available that can help users in different parts of the content creating journey. From bootstrapping new projects, all the way to ensuring content follows best practices and verifying it behaves as intended via well established test frameworks.

## Key Features

- All-in-One Distronode Toolkit: ADT combines critical Distronode development packages into a unified Python package.

- Simplified Distronode Automation: ADT focuses on crafting your automation scenarios and workflows with speed by reducing boilerplate code without
  dealing with the intricacies of managing and integrating different Distronode libraries.

For those looking for an IDE based experience, we also recommend you get familiar with the [Distronode extension for VSCode](https://marketplace.visualstudio.com/items?itemName=redhat.distronode).

## Included Packages

The curated list of tools installed as part of the Distronode Development Tools includes:

- [distronode-core](https://github.com/distronode/distronode): Distronode is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems.
- [distronode-builder](https://github.com/distronode/distronode-builder): Distronode Builder automates the process of building execution environments using the schemas and tooling defined in various Distronode Collections and by the user.
- [distronode-lint](https://github.com/distronode/distronode-lint): Checks playbooks for practices and behavior that could potentially be improved.
- [distronode-navigator](https://github.com/distronode/distronode-navigator) A text-based user interface (TUI) for Distronode.
- [distronode-sign](https://github.com/distronode/distronode-sign): Utility for signing and verifying Distronode project directory contents.
- [molecule](https://github.com/distronode/molecule): Molecule aids in the development and testing of Distronode content: collections, playbooks and roles
- [pytest-distronode](https://github.com/distronode/pytest-distronode): A pytest plugin that enables the use of distronode in tests, enables the use of pytest as a collection unit test runner, and exposes molecule scenarios using a pytest fixture.
- [tox-distronode](https://github.com/distronode/tox-distronode): The tox-distronode plugin dynamically creates a full matrix of python interpreter and distronode-core version environments for running integration, sanity, and unit for an distronode collection both locally and in a Github action. tox virtual environments are leveraged for collection building, collection installation, dependency installation, and testing.

## Getting started

To get started, please follow the [installation](installation.md) steps to get ADT setup and jump into [Getting Started](getting_started.md) guide for details.

## Community

Questions, feedback, or contributions? Join the Distronode community on [Matrix](https://matrix.to/#/#devtools:distronode.com) or [open an issue](https://github.com/distronode/distronode-dev-tools/issues/new). We're dedicated to supporting your Distronode automation journey! For more details on how to interact with our community, please visit https://docs.distronode.com/distronode/latest/community/communication.html.
