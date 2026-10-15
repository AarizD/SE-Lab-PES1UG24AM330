# Lab 5: Static Code Analysis - Issue Documentation

This document records the issues identified by static analysis tools (Pylint, Bandit, and Flake8) during the analysis of `dairy_collection.py`, along with the approaches used to fix them.

## Issue Tracking Table

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Hardcoded SQL Expression** (Bandit B608)[cite: 3] | Security (Medium)[cite: 3] | 11[cite: 3] | Possible SQL injection vector through string-based query formatting (`.format()`) | Replaced string formatting with parameterized queries using placeholders (`?`)[cite: 3]. |
| **Weak MD5 Hash** (Bandit B324) | Security (High) | 16 | Use of weak MD5 hash (`hashlib.md5`) for security purposes | Upgraded cryptographic hashing algorithm from MD5 to SHA-256 (`hashlib.sha256()`). |
| **Shell Injection Risk** (Bandit B605) | Security (High) | 31 | Starting a process through the shell using `os.system()` | Replaced shell-based execution with `subprocess.run()` passing arguments as a safe list. |
| **Line Too Long** (Flake8 E501 / Pylint C0301) | Style / Quality | Various | Lines exceeded the standard character length limit | Wrapped long lines using implicit line continuation and parentheses. |
| **Comparison to None** (Flake8 E711 / Pylint C0121) | Style / Quality | Various | Using `== None` instead of identity comparison | Changed comparisons to use `is None` according to PEP 8 standards. |
| **Redefined Outer Name** (Pylint W0621) | Code Quality | Various | Function parameters (`conn`) shadowed the global connection object | Renamed function parameters to `db_conn` and managed the connection locally within `main()`. |
