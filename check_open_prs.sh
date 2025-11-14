#!/bin/bash
# Script to check open pull requests using GitHub CLI or git commands

set -e

OWNER="rafaelpadua-tlf"
REPO="skills-scale-institutional-knowledge-using-copilot-spaces"

# Allow override with command line arguments
if [ $# -eq 2 ]; then
    OWNER="$1"
    REPO="$2"
fi

echo "Checking open pull requests for $OWNER/$REPO"
echo "==============================================="
echo ""

# Check if gh CLI is available and authenticated
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    echo "Using GitHub CLI (gh)..."
    echo ""
    gh pr list --repo "$OWNER/$REPO" --state open --json number,title,author,createdAt,updatedAt,isDraft,url | \
    python3 -c "
import sys, json
prs = json.load(sys.stdin)
if not prs:
    print('No open pull requests found.')
else:
    for pr in prs:
        print(f'PR #{pr[\"number\"]}: {pr[\"title\"]}')
        print(f'  Author: {pr[\"author\"][\"login\"]}')
        print(f'  Draft: {pr[\"isDraft\"]}')
        print(f'  Created: {pr[\"createdAt\"]}')
        print(f'  Updated: {pr[\"updatedAt\"]}')
        print(f'  URL: {pr[\"url\"]}')
        print()
    print(f'Total open PRs: {len(prs)}')
"
else
    echo "GitHub CLI (gh) not available or not authenticated."
    echo "Trying Python script..."
    echo ""
    if [ -f "check_open_prs.py" ]; then
        python3 check_open_prs.py "$OWNER" "$REPO"
    else
        echo "Error: check_open_prs.py not found."
        echo ""
        echo "Alternative: View pull requests at:"
        echo "https://github.com/$OWNER/$REPO/pulls"
        exit 1
    fi
fi
