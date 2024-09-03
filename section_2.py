import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 标题名称
st.header('st.write')

# 字符串类型
st.write('Hello, *World!* :sunglasses:')

# 数字类型
st.write(1234)

# 字典类型
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write(df)

# 字符串和字典类型相结合
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 图表数据的打印
## 用pandas来构建一个随机数据组
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a','b','c']
)
st.write(c)

