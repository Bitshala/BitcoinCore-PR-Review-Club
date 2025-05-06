#!/usr/bin/env python3

import os
import re
import sys
from datetime import datetime
from dateutil import parser
from github import Github

def extract_pr_info(issue_body):
    """Extract PR information from issue body."""
    date_pattern = r"Date[^\n]*:\s*(.*?)(?:\n|$)"
    title_pattern = r"Title[^\n]*:\s*(.*?)(?:\n|$)"
    pr_pattern = r"PR[^\n]*:\s*(.*?)(?:\n|$)"
    
    date_match = re.search(date_pattern, issue_body, re.IGNORECASE)
    title_match = re.search(title_pattern, issue_body, re.IGNORECASE)
    pr_match = re.search(pr_pattern, issue_body, re.IGNORECASE)
    
    date = date_match.group(1).strip() if date_match else None
    title = title_match.group(1).strip() if title_match else None
    pr_details = pr_match.group(1).strip() if pr_match else None
    
    # Try to parse the date to ensure it's valid
    if date:
        try:
            parsed_date = parser.parse(date)
            date = parsed_date.strftime("%B %d, %Y")
        except:
            pass
    
    return date, title, pr_details

def update_readme(date, title, pr_details):
    """Update the README.md file with new PR review information."""
    with open("README.md", "r") as file:
        content = file.read()
    
    # Update the "Next Review Club" section
    next_review_pattern = r"## Next Review Club\n- Date: .*?\n- Title: .*?\n- PR Details: .*?\n"
    next_review_replacement = f"## Next Review Club\n- Date: {date}\n- Title: {title}\n- PR Details: {pr_details}\n"
    
    updated_content = re.sub(next_review_pattern, next_review_replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w") as file:
        file.write(updated_content)

def main():
    """Main function to process the issue and update the README."""
    # Get environment variables
    github_token = os.environ.get("GITHUB_TOKEN")
    issue_number = int(os.environ.get("ISSUE_NUMBER"))
    issue_title = os.environ.get("ISSUE_TITLE")
    issue_body = os.environ.get("ISSUE_BODY")
    repo_name = os.environ.get("REPO")
    
    if not all([github_token, issue_number, issue_title, issue_body, repo_name]):
        print("Missing required environment variables.")
        sys.exit(1)
    
    # Extract PR information from issue body
    date, title, pr_details = extract_pr_info(issue_body)
    
    # If we couldn't extract all required info, log and exit
    if not all([date, title]):
        print("Could not extract all required information from issue.")
        print(f"Date: {date}, Title: {title}, PR Details: {pr_details}")
        # Use defaults for missing info
        if not date:
            # Find next Thursday from today
            today = datetime.now()
            days_until_thursday = (3 - today.weekday()) % 7
            if days_until_thursday == 0:
                days_until_thursday = 7
            next_thursday = today.replace(day=today.day + days_until_thursday)
            date = next_thursday.strftime("%B %d, %Y")
        
        if not title:
            title = "TBA"
        
        if not pr_details:
            pr_details = "TBA"
    
    # Update the README
    update_readme(date, title, pr_details)
    print(f"README updated with new PR review information.")

if __name__ == "__main__":
    main()