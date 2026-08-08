# IBM Applied Data Science Capstone - SpaceX Falcon 9

**Author:** Khalel A. Kh. A. Alnajem  
**Course:** IBM Applied Data Science Capstone (Coursera)

## Project objective

This capstone studies SpaceX Falcon 9 launch history to understand the factors associated with first-stage landing success and to build classification models that predict whether the first stage will land successfully. The business motivation is that first-stage reuse is a major driver of launch-cost savings.

## End-to-end workflow

1. Collect launch data using the SpaceX REST API.
2. Collect historical launch records with web scraping.
3. Clean and wrangle the data with Pandas and NumPy.
4. Perform exploratory data analysis with visualization and SQL.
5. Analyze launch-site geography with Folium.
6. Build an interactive Plotly Dash dashboard.
7. Train and evaluate classification models with Scikit-learn.
8. Communicate the results in a final presentation.

## Repository files

- `01_SpaceX_Data_Collection_API.ipynb` - API collection workflow.
- `02_SpaceX_Web_Scraping.ipynb` - Wikipedia scraping workflow.
- `03_SpaceX_Data_Wrangling.ipynb` - cleaning, landing labels and feature preparation.
- `04_SpaceX_EDA_SQL.ipynb` - SQL queries used in the capstone.
- `05_SpaceX_EDA_Visualization.ipynb` - visual exploratory analysis.
- `06_SpaceX_Folium_Interactive_Map.ipynb` - launch-site and proximity mapping.
- `07_spacex_dash_app.py` - interactive dashboard application.
- `08_SpaceX_Machine_Learning_Prediction.ipynb` - classification workflow and model comparison.

## Main findings

- Landing performance improves markedly as flight experience increases.
- KSC LC-39A is one of the strongest-performing launch sites and has a landing-success ratio of about 76.9% in the course dashboard dataset.
- Orbit, payload mass, launch site and booster generation are useful predictors of landing success.
- Payloads in the middle range (roughly 2,000-5,500 kg) show many successful outcomes in the dashboard analysis.
- Logistic Regression, SVM, Decision Tree and KNN were compared after standardization and hyperparameter tuning. The Decision Tree reached 83.33% test accuracy in the course lab configuration and was selected as the best-performing model for the final report.

## SQL highlights

- NASA (CRS) missions carried a total payload of **45,596 kg** in the SQL lab dataset.
- Average payload for the `F9 v1.1` booster family was approximately **2,534.7 kg**.
- The first successful ground-pad landing in the SQL dataset occurred on **2015-12-22**.

## Tools

Python, Pandas, NumPy, Requests, BeautifulSoup, SQL/SQLite, Matplotlib, Seaborn, Folium, Plotly Dash and Scikit-learn.

## Final research question

**Can historical Falcon 9 launch information be used to predict whether the first stage will land successfully?**
