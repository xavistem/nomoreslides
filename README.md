# No More Slides  
*An all-in-one Streamlit template for data professionals to present entire projects without slides*

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Live Preview](#live-preview)   
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation & Running Locally](#installation--running-locally)  
   - [App Structure & Comments](#app-structure--comments)  
5. [Usage Overview](#usage-overview)  
   - [Personal Introduction](#personal-introduction)  
   - [Data Upload & Automated EDA](#data-upload--automated-eda)  
   - [Dashboards & Analysis](#dashboards--analysis)  
   - [Machine Learning & Statistics](#machine-learning--statistics)  
6. [Customization & Theming](#customization--theming)  
7. [Why “No More Slides”?](#why-no-more-slides)  
   - [Communication Focus](#communication-focus)   
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Authors](#authors)  

---

## Introduction
**No More Slides** is an MIT-licensed, open-source Streamlit template designed for any data-focused role (Data Analyst, Data Scientist, Data Engineer, ML Engineer, BI Developer, etc) to **present an entire project** (introduction, data cleaning, EDA, dashboards, ML, statistics, conclusions) within a single web app. Instead of building multiple slide decks, use this template to keep your audience engaged and focus on **communicating your insights**, not formatting slides.

---

## Features
- **Complete Project Flow**: Personal introduction, data upload & cleaning, automated EDA, interactive dashboards, ML and statistical analysis, conclusion—all in one `app.py`.  
- **Automated Data Cleaning & EDA**: Upload a CSV (or similar), and the template will:  
  1. Detect missing values and suggest imputations.  
  2. Provide summary statistics (mean, median, std, etc.).  
  3. Generate initial plots (histograms, boxplots, correlation heatmaps).  
  4. Show interactive tables for raw vs. cleaned data.  
- **Interactive Dashboards**: Pre-built charts (line, bar, pie), maps (via PyDeck), KPI cards, filters, and layout components (`st.columns`, `st.expander`, `st.tabs`).  
- **ML & Statistics Scaffolding**: Code sections to split data, train basic models (e.g., logistic regression, random forest), display performance metrics (accuracy, ROC, confusion matrix) and residual plots.  
- **Commented Guidance (ES/EN)**: Every major block in `app.py` is annotated in Spanish and English, guiding you on where to customize.  
- **Light-Friendly UI (Default)**: Designed for a light background.

---

## Live Preview
View a blank version of this template (no sample data) on Streamlit Community:  
**http://nomoreslides.streamlit.app/**  

> [!TIP] 
> If the app has been idle, you may see:
```
ZZZ This app has gone to sleep due to inactivity. Would you like to wake it back up?
```  
Click **“Yes, get this app back up!”** to continue.  

This preview is for visualization purposes only. To use the template, fork the repository and either run the app locally or deploy it using your own Streamlit account.


---

## Getting Started

### Prerequisites
- **Python 3.8+**  
- **pip**  
- (Optional) **Git** for version control  
- Recommended: a virtual environment (`venv`, `conda`, etc.)

### Installation & Running Locally
1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/no-more-slides.git
   cd no-more-slides
   ```
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```  
   Keep the terminal open after running streamlit run app.py. Any changes you make to app.py will auto-refresh—just press **F5** in your browser to see the updates.

### App Structure & Comments
- **`app.py`**  
  - Sections clearly marked with `# SECTION:` comments (Spanish/English).  
  - Follow “TODO” comments to replace placeholders (name, dataset path, model settings).  
  - Sections include:  
    1. Personal Introduction  
    2. Data Upload & Cleaning  
    3. Exploratory Data Analysis (charts, tables)  
    4. Interactive Dashboards  
    5. ML & Statistical Models  
    6. Conclusions & Insights  

---

## Usage Overview

### Personal Introduction
- Display your name, role/title, location, a brief bio, and clickable badges for GitHub, LinkedIn, or portfolio.  
- Optionally, include a PyDeck map with pins (e.g., hometown, HQ).

### Data Upload & Automated EDA
- Use `st.file_uploader` to accept CSV (or similar).  
- Automatically perform:  
  1. Missing value detection & imputation suggestions.  
  2. Summary statistics table (`st.dataframe`).  
  3. Initial plots: histograms, boxplots, correlation heatmap.  
  4. Cleaned data preview in an interactive table.

### Dashboards & Analysis
- Create KPI cards (`st.metric`) showing total records, null percentages, unique categories.  
- Add user-driven filters (dropdowns, sliders) to update charts dynamically.  
- Display PyDeck or Folium maps for geospatial insights.  
- Organize layout with `st.columns`, `st.expander`, and `st.tabs` for a polished look.

### Machine Learning & Statistics
- Prebuilt code to:  
  1. Split data (train/test).  
  2. Train a model (e.g., logistic regression, random forest).  
  3. Show metrics: accuracy, F1 score, MSE, etc.  
  4. Plot confusion matrix, ROC curve, residuals, and feature importance.  
- Use `st.markdown()` to explain your modeling choices, hyperparameters, and evaluation.

---

## Customization & Theming
This template is designed to work best in light mode for optimal readability. If you're running the app locally or on Streamlit Cloud, make sure to switch to light mode for the best visual experience.

If you prefer dark mode, feel free to adjust component styles in `app.py` if needed (e.g., chart backgrounds, map styles).
By default, the template uses a light theme for readability. To switch to dark mode:

---

## Why “No More Slides”?
### Communication Focus
We believe **effective storytelling** and clear communication of data insights are more important than slide design. By using a unified Streamlit web app, you can:
- Eliminate context switches between code and slides.  
- Keep your audience engaged with **interactive** visualizations.  
- Concentrate on explaining methodology, results, and impact—rather than formatting slides.

> [!IMPORTANT]  
> We are not against slides—many scenarios (board meetings, academic talks) benefit from a traditional deck. If you prefer slides, please continue. But if you want a **single, interactive presentation**, this template is for you.

---

## Contributing
We welcome community contributions!  
1. Fork this repo.  
2. Create a branch:  
   ```bash
   git checkout -b feature/your-idea
   ```  
3. Commit your changes with clear messages.  
4. Push to your fork:  
   ```bash
   git push origin feature/your-idea
   ```  
5. Open a Pull Request against `main`.

> [!NOTE]  
> Any new dependencies should be added to `requirements.txt`. Include tests or examples if possible.

---

## License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Authors  
[![Rocío](https://img.shields.io/badge/@JimenezRoDA-GitHub-181717?logo=github&style=flat-square)](https://github.com/JimenezRoDA)  
[![Xavi](https://img.shields.io/badge/@xavistem-GitHub-181717?logo=github&style=flat-square)](https://github.com/xavistem)

---

![Python](https://img.shields.io/badge/Python-3.12.7-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Finished-brightgreen)

[🔝 Back to top](#table-of-contents)
