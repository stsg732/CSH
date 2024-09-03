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

# st.selectbox

## 用户选择一个颜色
## 显示用户选择的颜色

## 选择一个复选框

## ex1.
st.header('st.selectbox')
option = st.selectbox(
    "What is your favorite color?",
    ('Blue','Red','Green','Yellow')
)
st.write('Your favorite color is ',option)

## ex2.设置默认值
option = st.selectbox(
    "how would you like to be contacted?",
    ('Email','Home phone','Mobile phone'),
    index = None,
    placeholder = "Select contact method...",
)
st.write('You selected: ',option)

## ex3.多个复选框选项
## 在会话状态中存储部件的初始值
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
## 设定两列
col1,col2=st.columns(2)
## 第一列展示的东西
with col1:
    # 设置一个检查框，设定是否可见
    st.checkbox("Disable selectbox widget",key="disabled")
    # 设定radio选项
    st.radio(
        "Set selectbox label visibility ",
        key = "visibility",
        options = ["visible","hidden","collapsed"],
    )
## 第二列要展示的东西
with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email","Home phone","Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

# st.multiselect（多选）

st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)
st.write('You selected: ',options)

# st.checkbox（勾选组件）

st.header('st.checkbox')
st.write('What would you like to order?')

icecream=st.checkbox('Ice cream')
coffee=st.checkbox('Coffee')
tea=st.checkbox('Tea')

if icecream:
    st.write("Great! Here's some more :icecream:")
if coffee:
    st.write("Okay, here's some coffee :coffee:")
if tea:
    st.write("Here you go :tea:")

# 组件s（用不了）

# st.secrets（用不了）

# st.file_uploader（上传文件的组件）

from io import StringIO

## 上传一个文件
uploaded_file = st.file_uploader("Choose a file")
## 不为空则上传
if uploaded_file is not None:
    # 以字节形式上传
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # 转换为基于字符串的IO
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    # 以字符串形式读取文件
    string_data = stringio.read()
    st.write(string_data)
    # 可用于接受“类文件”对象的任何地方
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

## 多文件上传
uploaded_files = st.file_uploader("Choose a CSV file",accept_multiple_files = True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:",uploaded_file.name)
    st.write(bytes_data)
