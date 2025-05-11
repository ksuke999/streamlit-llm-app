from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)


import streamlit as st
st.title("LLMアプリ")
st.write("##### 動作モード1: 健康に関する専門家")
st.write("入力フォームに質問を入力し、「相談」ボタンを押すと、健康に関する専門家としての回答が得られます。")
st.write("##### 動作モード2: お金に関する専門家")
st.write("入力フォームに質問を入力し、「相談」ボタンを押すと、お金に関する専門家としての回答が得られます。")

selected_item = st.radio(
    "専門家を選択してください",
    ["健康に関する専門家", "お金に関する専門家"]
)

st.divider()

if selected_item == "健康に関する専門家":
    input_message = st.text_input(label="健康に関する質問を入力してください")
else:
    input_message = st.text_input(label="お金に関する質問を入力してください")

if st.button("相談"):
    st.divider()

    if input_message:
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。"),
            HumanMessage(content=input_message)
        ]
        response = llm.predict_messages(messages)
        st.write(str(response.content))
    else:
        st.error("質問を入力してから、「相談」ボタンを押してください。")
