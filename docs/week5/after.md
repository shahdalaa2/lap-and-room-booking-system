# Week 5 – Before / after

| Measure | Before (legacy_fees.py) | After (fees.py) |
|---|---|---|
| Ruff issues (total) | 17 (16 in the handout; Ruff 0.17 adds PLR0917) | 0 (`All checks passed!`) |
| Highest cyclomatic complexity | 9 (`calc`) | 4 (`tuition_fee`) |
| Arguments of the main function | 6 | 5 (3 required, 2 with defaults) |
| Pylint score (/10) | 4.86 | 10.00 |
| Tests passing | 0 (no tests) | 6 in test_fees.py (16 with the kata tests) |

Tool versions: Ruff 0.17.6, Pylint 4.1.4, pytest 9.2.0.

## Pairing reflection (3–4 sentences, write in your own words)

<!-- Each partner: one or two sentences. What was easier or harder with a driver and a navigator? -->
Working together made reviewing the refactoring changes and spotting edge cases much easier than working alone. Untangling the legacy logic and fixing all lint and test issues took the most effort, especially keeping the code clean and clear. Reviewing each other's work helped us catch mistakes early and feel more confident in the final results.