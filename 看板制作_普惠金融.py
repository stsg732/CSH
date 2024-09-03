import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.path import Path

# 数据导入

df = pd.read_excel("C:/Users/86134/Desktop/普惠金融_看板数据.xlsx")
print(df.head())

# 网页标题

## 设置网页信息
st.set_page_config(page_title="普惠金融数据大屏",page_icon=":card_index_dividers",layout="wide")

# 侧边栏和多选框
st.sidebar.header("请在这里筛选:")
year = st.sidebar.multiselect(
    "选择年份：",
    options=df["年份"].unique(),
    default=df["年份"].unique(),
)
area = st.sidebar.multiselect(
    "选择地区：",
    options=df["地区"].unique(),
    default=df["地区"].unique(),
)

df_selection1 = df.query(
    "地区 == @area"
)
df_selection2 = df.query(
    "年份 == @year & 地区 == @area"
)

# 主页面
st.title(":card_index_dividers:普惠金融数据大屏")
st.markdown("##")

# 计算核心指标
PCDI_rating = round(df_selection2["居民人均可支配收入(元/人)"].mean(),1)
GDP_rating = round(df_selection2["人均GDP"].mean(),1)

# 两列布局
left_columns, right_columns = st.columns(2)

# 添加信息
with left_columns:
    st.subheader("居民人均可支配收入：")
    st.subheader(f"RMB {PCDI_rating:,}")
with right_columns:
    st.subheader("人均GDP：")
    st.subheader(f"RMB {GDP_rating:,}")

# 分隔符
st.markdown("""---""")

# 主页面图表

years = df_selection2['年份']
dfii_values = df_selection2.groupby(by=["年份"])['中国数字金融发展指数'].mean()
dfii_cover_values = df_selection2.groupby(by=["年份"])['数字金融覆盖广度'].mean()
dfii_depth_values = df_selection2.groupby(by=["年份"])['数字金融使用深度'].mean()
dfii_digital_values = df_selection2.groupby(by=["年份"])['数字化支持服务程度'].mean()

years = dfii_values.index

fig = go.Figure()

fig.add_trace(go.Scatter(x=years, y=dfii_values,
                         mode='lines+markers',
                         name='中国数字金融发展指数',
                         line=dict(color='blue', width=2)))

fig.add_trace(go.Scatter(x=years, y=dfii_cover_values,
                         mode='lines+markers',
                         name='数字金融覆盖广度',
                         line=dict(color='green', width=2)))

fig.add_trace(go.Scatter(x=years, y=dfii_depth_values,
                         mode='lines+markers',
                         name='数字金融使用深度',
                         line=dict(color='red', width=2)))

fig.add_trace(go.Scatter(x=years, y=dfii_digital_values,
                         mode='lines+markers',
                         name='数字化支持服务程度',
                         line=dict(color='yellow', width=2)))

fig.update_layout(title='数字普惠金融指数及其一级分指数增长',
                  xaxis_title='年份',
                  yaxis_title='指数值',
                  legend=dict(x=1, y=0,
                              bgcolor='rgba(255, 255, 255, 0.8)',
                              bordercolor='rgba(0,0,0,0)'),
                  margin=dict(l=20, r=20, t=30, b=20),
                  plot_bgcolor='white')


df_selection2['财政支持'] = pd.to_numeric(df_selection2['财政支持'], errors='coerce')



# 使用Streamlit显示图表
top_columns = st.columns(1)
top_columns[0].plotly_chart(fig, use_container_width=True)