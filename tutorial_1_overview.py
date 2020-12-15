import os
import pandas as pd
import streamlit as st
import plotly.express as px


def read_company_info():
    company_info_path = os.path.join('.','data', 'tse_company_info.csv')
    df = pd.read_csv(company_info_path, index_col=0)
    return df 


company_info_df = read_company_info()

# """
# # データ表示
# """

# company_info_df

st.markdown('''
# データ表示
''')
st.dataframe(company_info_df)

st.title('時価総額')

fig = px.bar(company_info_df.sort_values('時価総額', ascending=False).iloc[:100], x='名前', y='時価総額')
# fig
st.plotly_chart(fig)
