#!/usr/bin/env python3
"""
Script to check and display open pull requests for the repository.

This script uses the GitHub API to fetch and display information about
open pull requests in the repository.

Environment Variables:
    GITHUB_TOKEN: Optional GitHub personal access token for authentication
"""

import json
import os
import sys
import urllib.request
import urllib.error

def check_open_pull_requests(owner, repo):
    """
    Fetch and display open pull requests from GitHub API.
    
    Args:
        owner: Repository owner/organization name
        repo: Repository name
    
    Returns:
        List of open pull requests
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    
    # Create request with optional authentication
    req = urllib.request.Request(api_url)
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token:
        req.add_header('Authorization', f'token {github_token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            pull_requests = json.loads(data)
            
            if not pull_requests:
                print(f"No open pull requests found in {owner}/{repo}")
                return []
            
            print(f"Open Pull Requests in {owner}/{repo}:")
            print("=" * 80)
            
            for pr in pull_requests:
                print(f"\nPR #{pr['number']}: {pr['title']}")
                print(f"  Author: {pr['user']['login']}")
                print(f"  State: {pr['state']}")
                print(f"  Draft: {pr['draft']}")
                print(f"  Created: {pr['created_at']}")
                print(f"  Updated: {pr['updated_at']}")
                print(f"  URL: {pr['html_url']}")
                
                if pr['body']:
                    # Show first 200 characters of the PR body
                    body_preview = pr['body'][:200].replace('\n', ' ')
                    if len(pr['body']) > 200:
                        body_preview += "..."
                    print(f"  Description: {body_preview}")
            
            print("\n" + "=" * 80)
            print(f"Total open PRs: {len(pull_requests)}")
            
            return pull_requests
            
    except urllib.error.HTTPError as e:
        print(f"Error fetching pull requests: {e.code} {e.reason}")
        if e.code == 403:
            print("\nNote: GitHub API has rate limits for unauthenticated requests.")
            print("You can set the GITHUB_TOKEN environment variable with a personal access token")
            print("to increase the rate limit. Example: export GITHUB_TOKEN=your_token_here")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

def main():
    """Main function to run the PR checker."""
    # Default to this repository
    owner = "rafaelpadua-tlf"
    repo = "skills-scale-institutional-knowledge-using-copilot-spaces"
    
    # Allow command line arguments to override
    if len(sys.argv) == 3:
        owner = sys.argv[1]
        repo = sys.argv[2]
    elif len(sys.argv) > 1:
        print("Usage: python check_open_prs.py [owner] [repo]")
        print("Example: python check_open_prs.py rafaelpadua-tlf skills-scale-institutional-knowledge-using-copilot-spaces")
        sys.exit(1)
    
    check_open_pull_requests(owner, repo)

if __name__ == "__main__":
    main()
