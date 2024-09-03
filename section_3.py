import streamlit as st

# st.markdown

st.markdown("*Streamlit* is **really** ***cool***.")

# 这里我们可以按照这个来进行输入，文字和颜色一起作为一个对象来输入
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# 可以作为一个变量进行传入并输出字符串变量
multi = '''If you end a line with two spaces,
a soft return is used for the next line.
Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# 加入文本介绍区域
md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")
# 加入代码行
st.code(f"""
import streamlit as st

#结果
st.markdown('''{md}''')
""")

st.markdown(md)

# emoji地址：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/


# st.caption

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


# st.code

## 放置可复制的代码块
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language = 'python')


# st.divider

## 显示水平规则

# 输入一段文本
st.write("This is some text.")
# 输入一个滑块，这里设定最大值和最小值，小括号内为默认范围
st.slider("This is a slider", 0, 100, (25, 75))
# 设定一个水平线，分割线
st.divider()
# 输入一段文本
st.write("This text is between the horizontal rules.")
# 输入另外一个文本
st.divider()


# st.echo

with st.echo():
    st.write('This code will be printed')

## 创建一个应用程序，其中包含“你好，约翰”，然后是“完成！”
## 使用st.echo()使中间那段代码再应用程序中可见

def get_user_name():
    return 'John'


with st.echo():
    # 该代码内的所有内容都将打印到屏幕上并被执行

    def get_punctuation():
        return '!!!'


    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# 回到不打印到屏幕的状态
foo = 'bar'
st.write('Done')


# st.latex()

## 数学公式表达:https://katex.org/docs/supported.html

st.latex(r'''
    a + ar +a r^2 + a r^3 + \cdots + a r^{n-1} = 
    \sum_{k=0}^{n-1} ar^k = 
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


# st.text

## 编写固定宽度和预格式化文本
st.text('This is some text.')

# https://github.com/stsg732/CSH

# st.slider

from datetime import time, datetime

## 添加一个隔断线
st.header('st.slider')

## ex1.添加一个小一号的标题
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ",age, 'years old.')

## ex2.
st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('values:', values)

## ex3.
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value = (time(11,30),time(12,45))
)
st.write("You're scheduled for: ",appointment)

## ex4.
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020,1,1,9,30),
    format = "MM/DD/YY - hh:mm"
)
st.write("Start time:",start_time)

# st.line_chart

## 使用numpy随机出一些数字，并用其创建一个pandas数据库
## 创建并显示折线图
import pandas as pd
import numpy as np

st.header('Line chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.line_chart(chart_data)