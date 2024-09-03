import pandas as pd
def get_data_form_excel():
    df = pd.read_excel(
        io = "C:/Users/86134/Desktop/实时看板-模拟数据.xlsx",
        engine = "openpyxl",
    )
    df["小时"] = pd.to_datetime(df["时间"],format="%H:%M:%S").dt.hour
    return df

df = get_data_form_excel()
print(df)
print(df.dtypes)

# 数据处理
df["时间"] = pd.to_datetime(df.时间,format = '%H:%M:%S')

# 网页标题

import streamlit as st
import plotly.express as px
## 设置网页信息
st.set_page_config(page_title="销售数据大屏",page_icon=":chart_decreasing:",layout="wide")

# 侧边栏和多选框

st.sidebar.header("请在这里筛选:")
city = st.sidebar.multiselect(
    "选择城市：",
    options=df["城市"].unique(),
    default=df["城市"].unique(),
)

customer_type = st.sidebar.multiselect(
    "选择顾客类型：",
    options=df["顾客类型"].unique(),
    default=df["顾客类型"].unique(),
)

gender = st.sidebar.multiselect(
    "选择性别：",
    options=df["性别"].unique(),
    default=df["性别"].unique(),
)

df_selection = df.query(
    "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
)

# 主页面
st.title(":bar_chart:销售数据大屏")
st.markdown("##")

# 计算核心指标：销售总额、平均评分、星级、平均销售额数据
total_sales = int(df_selection["总价"].sum())
average_rating = round(df_selection["评分"].mean(),1)
star_rating = ":star:" * int(round(average_rating,0))
average_sale_by_transaction = round(df_selection["总价"].mean(),2)

# 三列布局
left_columns, middle_columns, right_columns = st.columns(3)

# 添加相关信息
with left_columns:
    st.subheader("销售总额：")
    st.subheader(f"RMB {total_sales:,}")
with middle_columns:
    st.subheader("平均评分：")
    st.subheader(f" {average_rating} {star_rating}")
with right_columns:
    st.subheader("平均销售额：")
    st.subheader(f"RMB {average_sale_by_transaction}")

# 分隔符
st.markdown("""---""")

# 主页面图表

# 各类商品销售情况(柱状图)
sales_by_product_line = (
    df_selection.groupby(by=["商品类型"])['总价'].sum().sort_values()
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="总价",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>每种商品销售总额</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False)
)

# 每小时销售情况(柱状图)
df_selection['小时'] = df_selection['时间'].dt.hour  # 只需小时部分，不需要分钟和秒
sales_by_hour = df_selection.groupby(by=["小时"])['总价'].sum().reset_index()

fig_hourly_sales = px.bar(
    sales_by_hour,
    x="小时",  # 使用"小时"列作为x轴
    y="总价",
    title="<b>每小时销售总额</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear", showgrid=False),  # 可能不需要tickmode="linear"，因为默认就是
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False)
)

# 使用Streamlit显示图表
left_columns, right_columns = st.columns(2)
left_columns.plotly_chart(fig_product_sales, use_container_width=True)
right_columns.plotly_chart(fig_hourly_sales, use_container_width=True)

# 隐藏streamlit默认格式信息
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style,unsafe_allow_html=True)
