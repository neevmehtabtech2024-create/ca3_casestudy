# Evidence

Screenshots were taken on the group's Windows machine on 2026-10-12.

| File | Shows | Used in report |
|---|---|---|
| `initial-public-and-folders.png` | `C:\Users\Public` with the test folders `click demo` and `click-demo` | Figure 1 |
| `initial-documents-window.png` | Click 8.2.1: Documents opened instead of selecting `click demo` (bug) | Figure 2 |
| `after-test-folder-highlighted.png` | Click 8.4.1: Public opened with `click demo` highlighted | Figure 3 |
| `click-8-4-1-install-and-test.png` | PowerShell: installing Click 8.4.1 and running the launch command | Figure 4 |
| `click-version-and-test-terminal.png` | PowerShell: `click.__version__` is 8.4.1, then `click-demo.py` runs | Figure 5 |
| `cmdline-quoting-demo-output.txt` | Output of `reproduction/cmdline-quoting-demo.py` (root cause) | Section 5 |

Still to add: a screenshot of `pip show click` (version 8.2.1) taken just before the failing run, and the issue and PR pages (reporter, dates, status, review comments).

Screenshots show local behaviour only; the cause is established from the Click source and the quoting demo.
