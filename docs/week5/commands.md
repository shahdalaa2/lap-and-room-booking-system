# Suggested commit order (one commit per step, as Checkpoint D requires)

git switch -c week5-quality
git add .gitignore week5/grades.py week5/test_grades.py   # (see note below)
# Part B: commit 1 "Add letter_grade", commit 2 boundary tests,
# commit 3 "Remove magic numbers from letter_grade" with the Co-authored-by line
# Part D: commit after each refactoring step 1-7 of fees.py
git push -u origin week5-quality   # then open the pull request to main
