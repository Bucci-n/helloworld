import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})


df2 = pd.DataFrame(
# numbyで正規分布の乱数生成。以下は平均0,分散1
    np.random.randn(200,3),
#abc のカラムを作る
    columns=['a','b','c']
)
#altairで散布図作ってる
c = alt.Chart(df2).mark_circle().encode(
#x軸にa、y軸にb、サイズをcで定義するツールチップ（ツールヒント）も出す
    x='a',y='b',size='c', color='c',tooltip=['a','b','c']
)


st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write('こんにちは、世界！')

st.header('Display nubers')
st.write(1234)

st.header('Display DataFrame')
st.write(df)

st.header('Display multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dateframe')

st.header('Display Chart')
st.write(c)

