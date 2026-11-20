# Week 5 – Findings (legacy_fees.py)

## Findings table

| Rule | Count | Smell (lecture name) | Refactoring |
|---|---|---|---|
| F401 | 2 | Dead code (unused imports) | Delete the imports |
| PLR2004 | 6 | Magic numbers | Replace with named constants / an enum |
| C901 | 1 | Long method / complex conditionals | Replace the if/elif chain with a rate table; extract functions |
| PLR0913 | 1 | Long parameter list | Remove unused parameters; give the rest defaults or group them |
| ARG001 | 1 | Dead code (unused parameter `y`) | Remove the parameter |
| B006 | 1 | Mutable default argument | Use an immutable default such as `()` |
| E711 / E712 | 2 | Non-idiomatic comparisons (`!= None`, `== True`) | Default `discount` to 0; write `if summer:` |
| F841 | 1 | Dead code (unused variable `tmp`) | Delete it |
| N802 | 1 | Bad naming (breaks naming convention) | Rename `ProcessAll` to `process_all` |

Note: Ruff 0.17 also reports PLR0917 (too many positional arguments) on `calc`,
so the total on my machine is 17 instead of the 16 in the handout. It is fixed by the same
refactoring as PLR0913.

## Smells Ruff did not report

1. **Cryptic names** – `d`, `t`, `y`, `s`, `x`, `c`, `h` say nothing about their meaning.
2. **Type codes with a comment** – `1/2/3` are explained only by a comment instead of an Enum.
3. **Primitive obsession** – courses are plain dicts like `{"h": 3}`.
4. **Duplicated code** – the two branches in `ProcessAll` differ only in the type code.
5. **Mixed responsibilities** – `report` calculates, prints and returns.
6. **Pointless statement** – `total = total + 0` does nothing.
7. **Unused function** – `report` is never called.

## Hidden bug in ProcessAll

Type 3 (scholarship) matches neither `if`, so `fee` is never reassigned for Omar and
the `print` shows the value left over from Sara's iteration (1050 instead of 0). If Omar were
the first student, `fee` would not exist yet and Python would raise an error
(`UnboundLocalError`). Pylint warns about this as `possibly-used-before-assignment`.
