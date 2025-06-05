# No More Slides  
*An all-in-one Streamlit template for data professionals to present entire projects without slides*

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Live Preview](#live-preview)  
   - [Important Notice](#important-notice)  
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
8. [Tips, Notes & Important](#tips-notes--important)  
9. [Contributing](#contributing)  
10. [License](#license)  
11. [Authors](#authors)  

---

## Introduction
**No More Slides** is an MIT-licensed, open-source Streamlit template designed for any data-focused role—Data Analyst, Data Scientist, Data Engineer, ML Engineer, BI Developer, etc.—to **present an entire project** (introduction, data cleaning, EDA, dashboards, ML, statistics, conclusions) within a single web app. Instead of building multiple slide decks, use this template to keep your audience engaged and focus on **communicating your insights**, not formatting slides.

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
- **Light-Friendly UI (Default)**: Designed for a light background. Optional dark mode via Streamlit’s theme settings.  

---

## Live Preview
View a blank version of this template (no sample data) on Streamlit Community:  
**http://nomoreslides.streamlit.app/**  

<details>
  <summary>Important Notice</summary>

  [!IMPORTANT]  
  If the app has been idle, you may see:  
  ```
  ZZZ This app has gone to sleep due to inactivity. Would you like to wake it back up?
  ```  
  Click **“Yes, get this app back up!”** to continue.  

  **Tip:** To avoid waiting, deploy locally using the steps below.
</details>

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
   Keep the terminal open—any edits in `app.py` auto-refresh in your browser when you press **F5**.

> [!TIP]  
> The two-step install/run process ensures instant local previews without cloud delays.

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

> [!NOTE]  
> You can adjust map style (light/dark), marker colors, and initial view in the `st.pydeck_chart()` call.

### Data Upload & Automated EDA
- Use `st.file_uploader` to accept CSV (or similar).  
- Automatically perform:  
  1. Missing value detection & imputation suggestions.  
  2. Summary statistics table (`st.dataframe`).  
  3. Initial plots: histograms, boxplots, correlation heatmap.  
  4. Cleaned data preview in an interactive table.

> [!TIP]  
> Extend cleaning functions for other file types (Excel, JSON) or custom transformations.

### Dashboards & Analysis
- Create KPI cards (`st.metric`) showing total records, null percentages, unique categories.  
- Add user-driven filters (dropdowns, sliders) to update charts dynamically.  
- Display PyDeck or Folium maps for geospatial insights.  
- Organize layout with `st.columns`, `st.expander`, and `st.tabs` for a polished look.

> [!NOTE]  
> For complex dashboards, consider modularizing code into separate Python modules.

### Machine Learning & Statistics
- Prebuilt code to:  
  1. Split data (train/test).  
  2. Train a model (e.g., logistic regression, random forest).  
  3. Show metrics: accuracy, F1 score, MSE, etc.  
  4. Plot confusion matrix, ROC curve, residuals, and feature importance.  
- Use `st.markdown()` to explain your modeling choices, hyperparameters, and evaluation.

> [!TIP]  
> Swap in any library (scikit-learn, XGBoost, LightGBM, TensorFlow) by importing at the top of the ML section.

---

## Customization & Theming
By default, the template uses a light theme for readability. To switch to dark mode:

1. Create or edit `.streamlit/config.toml`:
   ```toml
   [theme]
   base="dark"
   ```
2. Adjust component styles in `app.py` if needed (e.g., chart backgrounds, map styles).

> [!TIP]  
> If you prefer dark mode, update PyDeck’s `map_style` to `"mapbox://styles/mapbox/dark-v10"` and adjust any light-colored text or backgrounds.

---

## Why “No More Slides”?
### Communication Focus
We believe **effective storytelling** and clear communication of data insights are more important than slide design. By using a unified Streamlit web app, you can:
- Eliminate context switches between code and slides.  
- Keep your audience engaged with **interactive** visualizations.  
- Concentrate on explaining methodology, results, and impact—rather than formatting slides.

> [!NOTE]  
> We are not against slides—many scenarios (board meetings, academic talks) benefit from a traditional deck. If you prefer slides, please continue. But if you want a **single, interactive presentation**, this template is for you.

---

## Tips, Notes & Important
> [!TIP]  
> **App Wake-Up**: When using Streamlit Community, if the app sleeps, click “Yes, get this app back up!” to wake it.

> [!NOTE]  
> **Bilingual Comments**: All code in `app.py` is annotated in Spanish and English. Feel free to remove or translate as needed.

> [!IMPORTANT]  
> **Instant Refresh**: Keep your terminal open after `streamlit run app.py`. Hit **F5** in the browser after any code change to see updates immediately.

> [!TIP]  
> **Large Datasets**: For files >100 MB, consider sampling or preprocessing offline—large DataFrames can slow Streamlit’s display.

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
*(Add your name, role, and contact info here)*  

-  
-  
