# Our contribution: regression test for `click.launch(..., locate=True)` on Windows

Upstream fix PR #3478 changed one line in `src/click/_termui_impl.py` and added
**no test**. Click's PR template asks for "tests that demonstrate the correct
behavior of the change. Tests should fail without the change", so this is a gap
we can fill.

`0001-test-open_url-locate-on-windows.patch` adds to `tests/test_termui.py`:

- `test_open_url_locate_windows_passes_select_as_separate_argument` (3 cases:
  no space, space in name, spaces in several path parts)
- `test_open_url_locate_windows_unquotes_file_url`

The tests fake Windows (`WIN = True`) and replace `subprocess.call`, so they run
on any OS in CI and need no Explorer window.

## Results (Click `main`, Python 3.13, Linux)

| Code under test | Result |
|---|---|
| with the fix (`["explorer", "/select,", path]`) | 4 passed |
| before the fix (`f"/select,{path}"`, commit `9b327da^`) | 4 failed |
| whole `tests/test_termui.py` with the new tests | 263 passed, 23 skipped |

## Apply it

```bash
git clone https://github.com/pallets/click && cd click
git apply path/to/0001-test-open_url-locate-on-windows.patch
python -m pytest tests/test_termui.py -k open_url_locate
```

## Submit it upstream (to be done by the group)

Fork `pallets/click`, apply the patch on a branch, push, and open a PR that
links issue #2994 ("refs #2994"). A test-only change needs no CHANGES entry.
Record the PR link in the report once it exists.
