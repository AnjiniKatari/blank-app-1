import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report 


#intro 
st.sidebar.title("California - Real Estate Agency")
page = st.sidebar.selectbox("Select Page", ["Introduction", "Visualization", "Automated Report"])
df = pd.read_csv("housing.csv")

st.write("\n\n\n")

if page == "Introduction":
    st.subheader("01 Introduction")
    st.markdown("#### Display ds")
    st.dataframe(df)
    st.markdown("##### Statistic about the dataset")
    st.dataframe(df.describe())
elif page == "Visualization":
    st.subheader("02 Data Viz")

    st.markdown("##### Bar Chart - Seaborn")

    ## start with creating the empty frame that receives the plot
    fig_bar, ax_bar = plt.subplots(figsize=(12,6))
    ## create the plot, in this case with seaborn 
    sns.barplot(data=df,x="ocean_proximity",y="median_house_value")
    ## render the plot in streamlit 
    st.pyplot(fig_bar)


    st.markdown("##### Bar Chart - Streamlit")
    st.bar_chart(data=df,x="ocean_proximity",y="median_house_value")

    st.markdown("##### Correlation matrix")

    corr_df = df.drop(["ocean_proximity"],axis=1)


    user_selection = st.multiselect("Select the variables that you want for the corr matrix",list(corr_df.columns),["latitude","longitude"])
    st.write(user_selection)

    corr_user_selection = corr_df[user_selection]

    ## start with creating the empty frame that receives the plot
    fig_corr, ax_corr = plt.subplots(figsize=(18,14))
    ## create the plot, in this case with seaborn 
    sns.heatmap(corr_user_selection.corr(),annot=True,fmt=".2f",cmap='coolwarm')
    ## render the plot in streamlit 
    st.pyplot(fig_corr)

elif page == "Automated Report":
    st.subheader("03 Automated Report")
    if st.button("Generate Report"):
        with st.spinner("Generating report..."):
            profile = ProfileReport(df,title="California Housing Report", explorative=True, minimal=True)
            st_profile_report(profile)






#load ds