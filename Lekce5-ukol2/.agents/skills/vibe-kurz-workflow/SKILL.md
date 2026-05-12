---
name: "vibe-kurz-workflow"
description: "Use when working on a Vibe Coding course assignment in a lesson directory. Keeps output inside the correct `Lekce*` folder, treats nearby course materials as reference-only, adds concise documentation, validates the result, and prepares the repository for a clean signed commit."
---

# Vibe Kurz Workflow

Use this skill when the task is a course assignment stored in a lesson folder such as `Lekce1` or `Lekce5-ukol2`.

## Workflow

1. Keep all deliverables inside the target lesson folder.
2. Treat starter projects and course materials as reference-only unless the user explicitly asks to edit them.
3. Produce a self-contained deliverable:
   - code or configuration files
   - lesson-level `README.md`
   - `.gitignore` when local artifacts are likely
   - `.env.example` only when environment variables are actually required
4. Add brief comments only where they materially improve readability.
5. Validate the result before proposing commit or push.
6. Review `git status` and keep secrets, caches, and local helper files out of git.
7. Prepare a short submission text with the GitHub link and one-sentence summary of the assignment.

## Repository Rules

- The lesson directory is the delivery boundary.
- Do not place assignment files in the repository root unless explicitly requested.
- If a nested directory is marked as reference material, do not edit it.
- Prefer documentation-first outputs when the assignment is about setup or workflow rather than application code.
