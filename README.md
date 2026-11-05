<div align="center">

<img src="assets/banner.svg" alt="Econometrics" width="100%">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-0F2E20?style=for-the-badge&logo=apple&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Progress-059669?style=for-the-badge)

</div>

---

# econometrics — my labs for the Econometrics course

Chernivtsi National University, 2nd year, Economic Cybernetics, group 251. The first labs
are regression by hand in Excel; from lab 3 the same models are rebuilt in Python and
compared against the Excel results.

---

## 🎓 Labs

| № | Topic | Tool | Status |
|---|---|---|---|
| 01 | Paired linear regression, by hand | Excel | ✅ done |
| 02 | Multiple linear regression, by hand | Excel | ✅ done (file not in repo) |
| 03 | Regression in Python (OLS) and comparison with Excel | Python | 🔨 part 1 ✅ · part 2 🔨 · part 3 planned |

---

## 🚀 Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd Лабораторна_3
python Lab_3_Lehotskyi_251_first_part.py
```

Run scripts from inside their lab folder: the Excel data file is read by relative path.

---

## 🗂 Structure

```
Econometrics CHNU/
├── assets/                  — repository banner
├── Лабораторна_3/
│   ├── Lab_3_Lehotskyi_251_first_part.py   — part 1: OLS, plots
│   ├── Lab_3_Lehotskyi_251_second_part.py  — part 2 (in progress)
│   └── ЛР1_Легоцький_251.xlsx              — lab 1 workbook, source of the data
├── requirements.txt
└── README.md
```

The lecturer's materials (task PDFs, lecture notes) are deliberately kept out of the repo.

---

## 🛠 Stack

| | |
|---|---|
| Language | Python 3 |
| Libraries | pandas, statsmodels, matplotlib, seaborn |
| Spreadsheets | Excel (openpyxl for reading) |
| IDE | PyCharm |
| OS | macOS |
