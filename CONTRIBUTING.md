# Contributing to LibreTunes

🎵🌱 Thank you for your interest in contributing to LibreTunes! We're excited to have you join our community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Code Contributions](#code-contributions)
- [Development Setup](#development-setup)
- [Local Development Environment](#local-development-environment)
- [Dependencies by Distribution](#dependencies-by-distribution)
- [Pull Request Process](#pull-request-process)
- [PR Title Format](#pr-title-format)
- [Style Guides](#style-guides)
- [Git Commit Messages](#git-commit-messages)
- [Documentation](#documentation)
- [Need Help?](#need-help)

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. We are committed to providing a welcoming and inclusive environment for everyone.

## Getting Started

- **Familiarize yourself** with the project by reading the [README](README.md) and [documentation](docs/README.md)
- **Explore existing issues** to see what others are working on
- **Start small** - look for issues tagged `good-first-issue` or `help-wanted`

## How Can I Contribute?

### Reporting Bugs

**Before reporting a bug, please check:**
- [Existing issues](https://github.com/FredXYZ-cmd/LibreTunes/issues) to see if it's already reported
- [Documentation](docs/README.md) for possible solutions

**When reporting a bug, include:**
- **Description**: What happened vs what you expected
- **Steps to Reproduce**: Clear, step-by-step instructions
- **Environment**:
  - Operating System and version
  - Python version
  - LibreTunes version
- **Screenshots**: If applicable
- **Logs**: Any error messages or console output

## Suggesting Features

We welcome feature ideas! When suggesting a feature:

- **Check existing feature requests** first
- **Explain the problem** you're trying to solve
- **Describe your proposed solution**
- **Provide examples** of how it would work
- **Consider alternatives** you've thought about

## Code Contributions

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   
3. **Make your changes**
4. **Test your changes thoroughly**
5. **Commit your changes:**
   
       git commit -m 'feat: add amazing feature'

6. **Push to your fork:**

       git push origin feature/amazing-feature
 
7. **Open a Pull Request**

## Development Setup
**Prerequisites**

Python 3.10+

GTK 4.0

GStreamer

## Local Development Environment
**1. Fork and clone the repository**

    git clone https://github.com/your-username/LibreTunes.git
    cd LibreTunes

**2. Create virtual environment**

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

**3. Install dependencies**

    pip install -r requirements.txt

**4. Install in development mode**

    pip install -e .

**5. Run the application**

    python -m libretunes

## Dependencies by Distribution

**Ubuntu/Debian**

    sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 gir1.2-adw-1 python3-pip

**Fedora**

    sudo dnf install python3-gobject gtk4 libadwaita python3-pip

**Arch Linux**

    sudo pacman -S python-gobject gtk4 libadwaita python-pip

## Pull Request Process

**1.** **Update documentation** if you've changed functionality

**2.** **Add tests** for new features (when applicable)

**3.** **Ensure all tests pass**

**4.** **Request review** from maintainers

**5.** **Address review feedback** promptly

## PR Title Format

**Use [conventional commits]( https://www.conventionalcommits.org/en/v1.0.0/) format:**

**feat**: New features

**fix**: Bug fixes

**docs**: Documentation changes

**style**: Code style changes (formatting, etc.)

**refactor**: Code refactoring

**test**: Adding or modifying tests

**chore**: Maintenance tasks

## Style Guides

**Python Code**

We use:

**Black** for formatting

**Flake8** for linting

**PEP 8** for style guidelines

**Run before committing**
    
    black src/ 
    flake8 src/

## Git Commit Messages

Use the present tense ("Add feature" not "Added feature")

Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

Limit the first line to 72 characters or fewer

Reference issues and pull requests liberally after the first line

## Documentation

Use Markdown for all documentation

Include code examples where helpful

Keep language clear and concise


## Need Help?

**Open an issue** for questions about contributing

**Check existing discussions** in issues and pull requests

**Be patient**-we're all volunteers here! 😊


### Thank you for contributing to LibreTunes! Your help makes this project better for everyone. 🎶
