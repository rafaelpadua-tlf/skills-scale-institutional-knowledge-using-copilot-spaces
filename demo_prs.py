#!/usr/bin/env python3
"""
Demo script that shows example output of checking open pull requests.

This demonstrates what the check_open_prs.py script would display
when it successfully connects to the GitHub API.
"""

def show_demo_output():
    """Display example output showing open pull requests."""
    
    print("Open Pull Requests in rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces:")
    print("=" * 80)
    
    # PR #4 (current PR)
    print("\nPR #4: [WIP] Implement functionality to check open pull requests")
    print("  Author: Copilot")
    print("  State: open")
    print("  Draft: True")
    print("  Created: 2025-11-14T17:12:01Z")
    print("  Updated: 2025-11-14T17:12:01Z")
    print("  URL: https://github.com/rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces/pull/4")
    print("  Description: Thanks for asking me to work on this. I will get started on it and keep this PR's description up to date as I form a plan and make progress...")
    
    # PR #3
    print("\nPR #3: [WIP] Add OctoAcme Project Management README")
    print("  Author: Copilot")
    print("  State: open")
    print("  Draft: True")
    print("  Created: 2025-11-14T17:09:45Z")
    print("  Updated: 2025-11-14T17:12:27Z")
    print("  URL: https://github.com/rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces/pull/3")
    print("  Description: ## Plan to Add OctoAcme Project Management README\n\nThis PR addresses issue #2 by adding a comprehensive README.md at the repository root to introduce and index the OctoAcme Project...")
    
    print("\n" + "=" * 80)
    print("Total open PRs: 2")
    print("\nNote: This is a demonstration output. For live data, use:")
    print("  - check_open_prs.py with GITHUB_TOKEN environment variable")
    print("  - check_open_prs.sh (requires authentication)")
    print("  - GitHub CLI: gh pr list --state open")
    print("  - Web browser: https://github.com/rafaelpadua-tlf/skills-scale-institutional-knowledge-using-copilot-spaces/pulls")

if __name__ == "__main__":
    show_demo_output()
