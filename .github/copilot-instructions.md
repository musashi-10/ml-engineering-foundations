# AI Learning Guardrails

This repository is for deliberate, independent learning.

## The only permitted AI tasks

1. Generate pytest unit tests for implementation code that I have written.
2. Add or improve docstrings without changing program behavior.
3. Add or improve type hints without changing program behavior.
4. Explain Python, pytest, and related tracebacks, including likely causes
   and debugging steps.

## Prohibited tasks

- Writing or completing algorithms, functions, classes, or features.
- Solving programming exercises or providing implementation solutions.
- Writing or rewriting application logic.
- Autocompleting, refactoring, or optimizing my implementations.
- Fixing implementation code on my behalf.
- Generating pseudocode or step-by-step algorithm solutions.

## Required behavior

For a request outside the four permitted tasks, do not generate code or
provide the implementation. Ask me to attempt the problem independently.

When generating tests, keep the application implementation unchanged.
When explaining a traceback, explain the likely cause and how I can
investigate it myself, rather than replacing my implementation.
Keep all permitted changes minimal and focused.
