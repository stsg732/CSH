import streamlit as st

st.write('Hello world!')

# st.button(按钮组件)
## 一般情况下输出Goodbye
## 按下按钮，显示Why hello there

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


# st.header(标题)
## 以标题格式显示文本

st.header('This is a header with a divider', divider = 'rainbow')
st.header('_Streamlit_ is :sunglasses:')


