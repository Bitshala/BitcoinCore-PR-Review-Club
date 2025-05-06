---
name: PR Review Club Announcement
about: Announce an upcoming PR review session
title: "PR Review Club: [PR Title]"
labels: announcement
assignees: ''
---

# Bitcoin Core PR Review Club

## Session Details

- **Date**: <!-- Date in format Month DD, YYYY -->
- **Time**: IST 19:00 (UTC 13:30)
- **Title**: <!-- Title of the PR being reviewed -->
- **PR**: <!-- Link to the PR -->

## PR Summary

<!-- Brief description of the PR and what it aims to accomplish -->

## Prerequisites

<!-- Any specific knowledge or setup required to participate -->

## Notes and Questions

<!-- List of questions to guide the review -->

1. 
2. 
3. 

## Preparation Steps

1. Clone the Bitcoin Core repository if you haven't already:
   ```
   git clone https://github.com/bitcoin/bitcoin.git
   ```

2. Fetch and checkout the PR:
   ```
   cd bitcoin
   git fetch origin pull/[PR_NUMBER]/head:pr_review
   git checkout pr_review
   ```

3. Build and run tests (if applicable):
   ```
   cmake -B build
   cmake --build build
   ```

4. Review the code changes and consider the provided questions.

## Joining the Session

The Jitsi link will be shared in the #announcements channel of the [Bitshala Discord](https://discord.gg/atjEPVTdsQ) shortly before the session.

Looking forward to seeing you there!