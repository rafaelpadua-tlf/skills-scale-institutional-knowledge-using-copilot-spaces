# Checking Open Pull Requests

This document explains how to check open pull requests in this repository.

## Using the Python Script

The repository includes a Python script `check_open_prs.py` that fetches and displays open pull requests using the GitHub API.

### Basic Usage

```bash
python3 check_open_prs.py
```

This will check open pull requests in the current repository (rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces).

### Check Another Repository

```bash
python3 check_open_prs.py <owner> <repo>
```

Example:
```bash
python3 check_open_prs.py octocat Hello-World
```

### Using GitHub Token (Recommended)

For better rate limits, set the GITHUB_TOKEN environment variable:

```bash
export GITHUB_TOKEN=your_personal_access_token
python3 check_open_prs.py
```

## Using GitHub CLI

If you have the GitHub CLI (`gh`) installed, you can also check pull requests:

```bash
gh pr list --state open
```

For more detailed information:

```bash
gh pr list --state open --json number,title,author,createdAt,updatedAt,url,isDraft
```

## Using the GitHub Web Interface

You can also view open pull requests directly on GitHub:
https://github.com/rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces/pulls

## Current Open Pull Requests

As of the last check, there are 2 open pull requests:

1. **PR #4**: [WIP] Implement functionality to check open pull requests
   - Draft PR that implements this functionality

2. **PR #3**: [WIP] Add OctoAcme Project Management README
   - Draft PR to add README for OctoAcme Project Management documentation

## Script Features

The `check_open_prs.py` script displays:
- PR number and title
- Author
- State (open/closed)
- Draft status
- Creation and update timestamps
- PR URL
- Description preview (first 200 characters)

## Requirements

- Python 3.x (standard library only, no external dependencies)
- Internet connection to access GitHub API
- Optional: GITHUB_TOKEN environment variable for authentication
