# Forensic Glass Classification EDA Dashboard

## Project Overview

This project is an Exploratory Data Analysis Dashboard based on a forensic glass dataset.  
The dataset contains 214 glass samples with chemical composition features and a glass type label.

The purpose of this dashboard is to analyze the distribution, comparison, relationships, and patterns in different glass types using data visualization.

## Dataset

The dataset used in this project is:

`glass.data`

or

`glass.data.txt`

The file is placed inside the `data/` folder.

Important: The dataset file name has not been renamed, as required in the project instructions.

## Dataset Schema

The dataset has the following columns:

| Column Name | Description |
|---|---|
| sample_id | Unique ID of each glass sample |
| refractive_index | Refractive index of the glass sample |
| sodium | Sodium chemical composition value |
| magnesium | Magnesium chemical composition value |
| aluminum | Aluminum chemical composition value |
| silicon | Silicon chemical composition value |
| potassium | Potassium chemical composition value |
| calcium | Calcium chemical composition value |
| barium | Barium chemical composition value |
| iron | Iron chemical composition value |
| glass_type | Target class/category of glass |

## Glass Type Categories

| Glass Type | Meaning |
|---|---|
| 1 | Building Windows Float |
| 2 | Building Windows Non-Float |
| 3 | Vehicle Windows Float |
| 5 | Containers |
| 6 | Tableware |
| 7 | Headlamps |

## Tools and Libraries Used

The following tools and libraries are used in this project:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Dashboard Features

The dashboard includes:

- Dataset overview
- Data cleaning summary
- Missing value check
- Duplicate row check
- KPI summary cards
- Interactive sidebar filters
- Glass type filter
- Sample ID range filter
- Refractive index range filter
- Chemical feature selector
- Search sample ID option
- Reset filters button

## KPI Cards

The dashboard displays the following KPI cards:

- Total Samples
- Total Glass Types
- Average Refractive Index
- Highest Sodium Value
- Highest Calcium Value

## Visualizations Included

The dashboard includes the required chart types:

| Chart Type | Purpose |
|---|---|
| Pie Chart | Shows percentage distribution of glass types |
| Histogram | Shows distribution of numerical chemical features |
| Line Chart | Shows trend of selected feature by sample ID |
| Bar Chart | Compares average chemical values by glass type |
| Scatter Plot | Shows relationship between two numerical variables |
| Box Plot | Shows spread and outliers |
| Heatmap | Shows correlation between numerical features |
| Area Chart | Shows cumulative trend |
| Count Plot | Shows frequency of glass types |
| Violin Plot | Shows distribution density by glass type |

## Chart Selection Explanation

Charts were selected according to the purpose of visualization:

- Pie chart is used for part-to-whole distribution.
- Histogram is used for numerical distribution.
- Bar chart is used for comparing values between groups.
- Scatter plot is used to observe relationships between two numerical variables.
- Box plot and violin plot are used to compare distributions and detect outliers.
- Heatmap is used to observe correlation between numerical features.

This follows the chart selection guide provided by the instructor.

## How to Run the Project

First, install the required libraries:

```bash
pip install -r requirements.txt