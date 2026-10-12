# Click CA-3 Case Study

**Course:** Open Source Technologies (TE7756) — CA-3
**Project:** Investigating Windows folder-selection behaviour in [Click](https://github.com/pallets/click)
**Issue:** [pallets/click#2994](https://github.com/pallets/click/issues/2994) · **Fix PR:** [pallets/click#3478](https://github.com/pallets/click/pull/3478)

## What this repo shows

`click.launch(path, locate=True)` on Windows opened the Documents folder instead of selecting the target when the path contained a space. We reproduced it on Click 8.2.1, confirmed Click 8.4.1 selects the folder, traced the fix (one line in `src/click/_termui_impl.py`, merged 2026-05-19, released in 8.4.1), explained the cause, and wrote regression tests the upstream PR lacked.

| Cause (see `reproduction/cmdline-quoting-demo.py`) | Command line Explorer receives |
|---|---|
| Click 8.2.1 `["explorer", f"/select,{url}"]` | `explorer "/select,C:\Users\Public\click demo"` |
| Click 8.4.1 `["explorer", "/select,", url]` | `explorer /select, "C:\Users\Public\click demo"` |

## Repository contents

| Path | Contents |
|---|---|
| `report/Click_CA3_Case_Study_Report.docx` | Final report (screenshots embedded); `report/case-study-report.md` is the same text |
| `reproduction/` | `click-demo.py` (Windows symptom), `cmdline-quoting-demo.py` (root cause, any OS) |
| `contribution/` | Our regression-test patch for Click and how to apply/submit it |
| `evidence/` | Screenshots and demo output, described in `evidence/README.md` |
| `requirements.txt` | `click==8.2.1`, the version that shows the bug |

## Reproduce (Windows, PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install click==8.2.1
python .\reproduction\click-demo.py        # Documents opens for the "click demo" folder (bug)
python -m pip install --upgrade click==8.4.1
python .\reproduction\click-demo.py        # Public opens, "click demo" highlighted (fixed)
```

Observations come from one local Windows machine. We did not write the upstream fix; it is by Rowlando13 (PR #3478). Our own contribution is in `contribution/`.


## Team contribution allocation

Division of work and contribution allocation: Neev Mehta – regression-test patch and final integration (30%); Shivam Dev – issue investigation and reproduction workflow (23%); Pranav Mangla – upstream pull-request and code-diff analysis (23%); Raghvendra Pathe – screenshots, evidence organization and report review (24%). All members should be able to explain the full case study.
