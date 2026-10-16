# CloudOps Agent

A minimal GitHub Agent + DevSecOps demonstration.

## Scenario

A cloud storage account has public network access enabled.

The GitHub Agent investigates the issue and creates a secure fix.

## Flow

Issue
→ Agent investigation
→ Bicep change
→ Pull Request
→ GitHub Actions
→ Tests
→ Approval
→ Merge

## Security rule

Public network access must be disabled.

## Infrastructure

The demo uses a single Azure Bicep file.

## Validation

Run:

```powershell
python -m unittest discover -v
