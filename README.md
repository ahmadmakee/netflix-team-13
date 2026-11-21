Netflix Team 13 analysis



**Selected assignment challenge:** Challenge 1 — What Makes Content Popular on Netflix?

## Files

- `Netflix_Analysis_Simplified.ipynb` — completed, executed Jupyter Notebook with explanations and 3 labeled charts
- `netflix_simple.py` — simple script alternative for PyCharm or VS Code
- `AGILE_PROJECT_PLAN.md` — sprint goal, Kanban board, two risks and retrospective template
- `requirements_simplified.txt` — dependencies
- `charts/` — exported PNG charts
- `Netflix_Analysis_Simplified.html` — optional executed HTML notebook export

The original repository already contains `movies.csv`, `users.csv` and `watchhistory.csv`. **Keep those files unchanged.**

## Run

1. Open the repository folder in VS Code, with the Python and Jupyter extensions installed.
2. Run `py -m pip install -r requirements_simplified.txt` in its terminal.
3. Open `Netflix_Analysis_Simplified.ipynb`, select the Python kernel, and click **Run All**.
4. Verify three charts, and take a screenshot of the final successfully executed notebook.

To run the optional script, use `py netflix_simple.py`.

**Important:** These 10 watch events are only a tiny classroom example, not representative Netflix-wide popularity data. Complete real team names, actual task statuses and sprint retrospective before submission.

## Commit to a separate branch

Inside your local clone of https://github.com/ahmadmakee/netflix-team-13, make a branch using `git checkout -b simplified-netflix-analysis`, copy the files from this ZIP into the repository root, then run:

```bash
git add Netflix_Analysis_Simplified.ipynb netflix_simple.py AGILE_PROJECT_PLAN.md README_SIMPLIFIED.md requirements_simplified.txt Netflix_Analysis_Simplified.html charts/
git commit -m "Add simplified Netflix notebook and Agile project plan"
git push -u origin simplified-netflix-analysis
```

Then open a pull request to `main` on GitHub.
