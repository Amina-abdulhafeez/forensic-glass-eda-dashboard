import os

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Forensic Glass EDA Dashboard",
    page_icon="🔬",
    layout="wide"
)

sns.set_theme(style="whitegrid")


# --------------------------------------------------
# Load dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    columns = [
        "sample_id",
        "refractive_index",
        "sodium",
        "magnesium",
        "aluminum",
        "silicon",
        "potassium",
        "calcium",
        "barium",
        "iron",
        "glass_type"
    ]

    possible_paths = [
        "data/glass.data.txt",
        "data/glass.data",
        "glass.data.txt",
        "glass.data"
    ]

    file_path = None

    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    if file_path is None:
        st.error("Dataset file not found. Please upload glass.data.txt or glass.data.")
        st.stop()

    df = pd.read_csv(file_path, header=None, names=columns)

    glass_type_names = {
        1: "Building Windows Float",
        2: "Building Windows Non-Float",
        3: "Vehicle Windows Float",
        5: "Containers",
        6: "Tableware",
        7: "Headlamps"
    }

    df["glass_type_name"] = df["glass_type"].map(glass_type_names)

    return df


df = load_data()

numeric_features = [
    "refractive_index",
    "sodium",
    "magnesium",
    "aluminum",
    "silicon",
    "potassium",
    "calcium",
    "barium",
    "iron"
]


# --------------------------------------------------
# Dashboard title
# --------------------------------------------------
st.title("🔬 Forensic Glass Classification EDA Dashboard")

st.markdown(
    """
    This dashboard analyzes forensic glass samples using chemical composition features.
    The goal is to explore patterns, distributions, relationships, and differences between glass types.
    """
)


# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

if st.sidebar.button("Reset / Clear Filters"):
    st.session_state.clear()
    st.rerun()

glass_types = sorted(df["glass_type_name"].dropna().unique())

selected_glass_types = st.sidebar.multiselect(
    "Select Glass Type",
    options=glass_types,
    default=glass_types
)

sample_id_range = st.sidebar.slider(
    "Select Sample ID Range",
    min_value=int(df["sample_id"].min()),
    max_value=int(df["sample_id"].max()),
    value=(int(df["sample_id"].min()), int(df["sample_id"].max()))
)

ri_range = st.sidebar.slider(
    "Select Refractive Index Range",
    min_value=float(df["refractive_index"].min()),
    max_value=float(df["refractive_index"].max()),
    value=(float(df["refractive_index"].min()), float(df["refractive_index"].max()))
)

selected_feature = st.sidebar.selectbox(
    "Select Chemical Feature for Analysis",
    options=numeric_features,
    index=1
)

search_sample = st.sidebar.text_input(
    "Search Sample ID",
    placeholder="Example: 10"
)


# --------------------------------------------------
# Apply filters
# --------------------------------------------------
filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["glass_type_name"].isin(selected_glass_types)
]

filtered_df = filtered_df[
    (filtered_df["sample_id"] >= sample_id_range[0]) &
    (filtered_df["sample_id"] <= sample_id_range[1])
]

filtered_df = filtered_df[
    (filtered_df["refractive_index"] >= ri_range[0]) &
    (filtered_df["refractive_index"] <= ri_range[1])
]

if search_sample.strip() != "":
    filtered_df = filtered_df[
        filtered_df["sample_id"].astype(str).str.contains(search_sample.strip())
    ]

if filtered_df.empty:
    st.warning("No data found for the selected filters. Please reset or change filters.")
    st.stop()


# --------------------------------------------------
# KPI cards
# --------------------------------------------------
st.subheader("Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric("Total Samples", len(filtered_df))
kpi2.metric("Glass Types", filtered_df["glass_type_name"].nunique())
kpi3.metric("Avg Refractive Index", round(filtered_df["refractive_index"].mean(), 5))
kpi4.metric("Highest Sodium", round(filtered_df["sodium"].max(), 2))
kpi5.metric("Highest Calcium", round(filtered_df["calcium"].max(), 2))


# --------------------------------------------------
# Dataset overview
# --------------------------------------------------
with st.expander("View Dataset and Cleaning Summary"):
    st.write("Filtered Dataset Preview")
    st.dataframe(filtered_df.head(20), use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.write("Dataset Shape")
    col1.write(filtered_df.shape)

    col2.write("Missing Values")
    col2.write(filtered_df.isnull().sum())

    col3.write("Duplicate Rows")
    col3.write(filtered_df.duplicated().sum())


# --------------------------------------------------
# Dashboard tabs
# --------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Distribution",
        "Comparison",
        "Relationships",
        "Outliers",
        "Correlation"
    ]
)


# --------------------------------------------------
# Tab 1: Distribution charts
# --------------------------------------------------
with tab1:
    st.subheader("Glass Type Distribution")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Pie Chart: Glass Type Percentage")
        pie_data = filtered_df["glass_type_name"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(
            pie_data.values,
            labels=pie_data.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title("Percentage Distribution of Glass Types")
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        st.markdown("### Count Plot: Number of Samples by Glass Type")

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(
            data=filtered_df,
            y="glass_type_name",
            order=filtered_df["glass_type_name"].value_counts().index,
            ax=ax
        )
        ax.set_title("Count of Glass Types")
        ax.set_xlabel("Number of Samples")
        ax.set_ylabel("Glass Type")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("### Histogram: Distribution of Selected Chemical Feature")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(
        data=filtered_df,
        x=selected_feature,
        kde=True,
        bins=20,
        ax=ax
    )
    ax.set_title(f"Histogram of {selected_feature}")
    ax.set_xlabel(selected_feature)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# Tab 2: Comparison charts
# --------------------------------------------------
with tab2:
    st.subheader("Chemical Composition Comparison")

    st.markdown("### Bar Chart: Average Chemical Feature by Glass Type")

    avg_data = (
        filtered_df.groupby("glass_type_name")[selected_feature]
        .mean()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    avg_data.plot(kind="barh", ax=ax)
    ax.set_title(f"Average {selected_feature} by Glass Type")
    ax.set_xlabel(f"Average {selected_feature}")
    ax.set_ylabel("Glass Type")
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("### Line Chart: Selected Feature by Sample ID")

    line_df = filtered_df.sort_values("sample_id")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=line_df,
        x="sample_id",
        y=selected_feature,
        marker="o",
        ax=ax
    )
    ax.set_title(f"{selected_feature} Trend by Sample ID")
    ax.set_xlabel("Sample ID")
    ax.set_ylabel(selected_feature)
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("### Area Chart: Cumulative Selected Feature by Sample ID")

    area_df = filtered_df.sort_values("sample_id").copy()
    area_df[f"cumulative_{selected_feature}"] = area_df[selected_feature].cumsum()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.fill_between(
        area_df["sample_id"],
        area_df[f"cumulative_{selected_feature}"],
        alpha=0.5
    )
    ax.plot(
        area_df["sample_id"],
        area_df[f"cumulative_{selected_feature}"]
    )
    ax.set_title(f"Cumulative {selected_feature} Trend")
    ax.set_xlabel("Sample ID")
    ax.set_ylabel(f"Cumulative {selected_feature}")
    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# Tab 3: Relationship charts
# --------------------------------------------------
with tab3:
    st.subheader("Relationships Between Chemical Features")

    col1, col2 = st.columns(2)

    with col1:
        scatter_x = st.selectbox(
            "Select X-axis Feature",
            options=numeric_features,
            index=1
        )

    with col2:
        scatter_y = st.selectbox(
            "Select Y-axis Feature",
            options=numeric_features,
            index=6
        )

    st.markdown("### Scatter Plot: Relationship Between Two Numeric Features")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=filtered_df,
        x=scatter_x,
        y=scatter_y,
        hue="glass_type_name",
        ax=ax
    )
    ax.set_title(f"{scatter_x} vs {scatter_y}")
    ax.set_xlabel(scatter_x)
    ax.set_ylabel(scatter_y)
    ax.legend(title="Glass Type", bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# Tab 4: Outlier and spread charts
# --------------------------------------------------
with tab4:
    st.subheader("Outlier and Distribution Analysis")

    st.markdown("### Box Plot: Spread and Outliers by Glass Type")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(
        data=filtered_df,
        x="glass_type_name",
        y=selected_feature,
        ax=ax
    )
    ax.set_title(f"Box Plot of {selected_feature} by Glass Type")
    ax.set_xlabel("Glass Type")
    ax.set_ylabel(selected_feature)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("### Violin Plot: Distribution Density by Glass Type")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.violinplot(
        data=filtered_df,
        x="glass_type_name",
        y=selected_feature,
        ax=ax
    )
    ax.set_title(f"Violin Plot of {selected_feature} by Glass Type")
    ax.set_xlabel("Glass Type")
    ax.set_ylabel(selected_feature)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# Tab 5: Correlation heatmap
# --------------------------------------------------
with tab5:
    st.subheader("Correlation Analysis")

    st.markdown("### Heatmap: Correlation Between Numerical Features")

    corr = filtered_df[numeric_features].corr()

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )
    ax.set_title("Correlation Matrix of Chemical Features")
    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# Key insights
# --------------------------------------------------
st.subheader("Key Insights")

most_common_type = filtered_df["glass_type_name"].value_counts().idxmax()

st.markdown(
    f"""
    - The dashboard currently shows **{len(filtered_df)} filtered samples**.
    - The selected chemical feature is **{selected_feature}**.
    - The most common glass type in the filtered data is **{most_common_type}**.
    - The highest value of **{selected_feature}** is **{round(filtered_df[selected_feature].max(), 3)}**.
    - The lowest value of **{selected_feature}** is **{round(filtered_df[selected_feature].min(), 3)}**.
    - The heatmap helps identify relationships between chemical composition features.
    """
)


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Exploratory Data Analysis Dashboard Project | Forensic Glass Dataset")
