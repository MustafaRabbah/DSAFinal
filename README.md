# DSA Final — MCQ Exam Practice

**Author:** Mustafa Rabbah · [Telegram @MustafaRabbah](https://t.me/MustafaRabbah)

Mobile-friendly multiple-choice quiz for your Data Structures & Algorithms final exam.  
Choose **Both**, **English only**, or **Arabic only** on the home screen (saved in your browser). You can switch anytime during a quiz too.

## Live site (GitHub Pages)

1. Create a repo on GitHub and push this project.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Choose branch `main` (or `master`) and folder **`/docs`**.
5. Save. After a minute, your site is at  
   `https://<your-username>.github.io/<repo-name>/`

Open that URL on your phone browser to practice.

## Add or update questions

1. Edit questions in `FInal/1` (tab-separated, same columns as the Excel files) and/or the `.xlsx` files in `FInal/`.
2. Rebuild the quiz data:

```bash
pip install openpyxl   # once
python3 scripts/build-questions.py
```

3. Commit and push — GitHub Pages will update automatically.

### Question file format

Columns (tab-separated in `FInal/1`, or Excel headers):

`difficulty` · `case_scenario` · `lead_in` · `a` · `b` · `c` · `d` · `e` · `answer`

- `difficulty`: `easy`, `medium`, or `hard`
- `answer`: single letter `a`–`e`
- `case_scenario`: e.g. `Arrays_case1` (used for topic grouping)

## Test locally

```bash
cd docs && python3 -m http.server 8080
```

Then open `http://localhost:8080` on your phone (same Wi‑Fi) or in the browser.

## Features

- Works on phone browsers (large tap targets, safe areas)
- Practice all topics or one topic at a time
- Filter by difficulty
- Instant feedback after each answer (English + Arabic)
- “Review missed” remembers wrong answers in the browser

Arabic text lives in `scripts/translations_ar.py`. Edit there, then run `python3 scripts/build-questions.py`.
