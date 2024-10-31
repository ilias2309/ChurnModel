import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Exploratory Data Analysis")

st.sidebar.title("Upload Data")

# Creating tabs for different sections
tab1, tab2, tab3 = st.tabs(["Data Info", "Numeric Features", "Categorical Features"])

uploaded_data = st.sidebar.file_uploader("Choose a CSV file")

@st.cache_data
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

if uploaded_data is not None:
    df = load_data(uploaded_data)

    with tab1:
        if uploaded_data is not None:
            st.header("Meta-data")

            # Calculating necessary values
            row_count = df.shape[0]
            column_count = df.shape[1]
            duplicate_row_count = df.duplicated().sum()
            missing_value_row_count = df[df.isna().any(axis=1)].shape[0]

            # Splitting the layout into two columns
            col1, col2 = st.columns(2)

            with col1:
                # Displaying meta-data in a markdown table on the left
                st.subheader("Dataset Overview")
                table_markdown = f"""
                | Description | Value | 
                |---|---|
                | Number of Rows | {row_count} |
                | Number of Columns | {column_count} |
                | Number of Duplicated Rows | {duplicate_row_count} |
                | Number of Rows with Missing Values | {missing_value_row_count} |
                """
                st.markdown(table_markdown)

            with col2:
                # Displaying columns' data types on the right
                st.subheader("Columns Data Types")
                columns = list(df.columns)
                column_info_table = pd.DataFrame({
                    "Column": columns,
                    "Data Type": df.dtypes.tolist()
                })
                st.dataframe(column_info_table, hide_index=True)

        with tab2:
                if uploaded_data is not None:
                    # Finding numeric features in the dataframe
                    numeric_cols = df.select_dtypes(include='number').columns.tolist()
                    # Adding a selection-box widget
                    selected_num_col = st.selectbox("Which numeric column do you want to explore?", numeric_cols)

                    # Displaying summary statistics for the selected numeric column
                    if selected_num_col:
                        st.write(f"Summary statistics for {selected_num_col}:")
                        st.write(df[selected_num_col].describe())

                        # Plotting a histogram for the selected numeric column
                        st.write(f"Histogram for {selected_num_col}:")
                        plt.figure(figsize=(10, 6))
                        plt.hist(df[selected_num_col].dropna(), bins=30, edgecolor='k')
                        plt.xlabel(selected_num_col)
                        plt.ylabel('Frequency')
                        plt.title(f'Distribution of {selected_num_col}')
                        st.pyplot(plt)

        with tab3:
            if uploaded_data is not None:
                # Finding categorical features in the dataframe
                categorical_cols = df.select_dtypes(include='object').columns.tolist()
                selected_cat_col = st.selectbox("Which categorical column do you want to explore?", categorical_cols)

                # Displaying value counts for the selected categorical column
                if selected_cat_col:
                    st.write(f"Value counts for {selected_cat_col}:")
                    st.write(df[selected_cat_col].value_counts())

                    # Plotting a bar chart for the selected categorical column
                    st.write(f"Bar chart for {selected_cat_col}:")
                    plt.figure(figsize=(10, 6))
                    df[selected_cat_col].value_counts().plot(kind='bar', edgecolor='k')
                    plt.xlabel(selected_cat_col)
                    plt.ylabel('Count')
                    plt.title(f'Distribution of {selected_cat_col}')
                    st.pyplot(plt)
