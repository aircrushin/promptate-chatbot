from openai import OpenAI
import streamlit as st

MOONSHOT_KEY = "sk-mvGbid4ChELTfaEqhnVfPzLz0ua8nOe82MrsgGiDUzxqOlvw"

openai_api_key = MOONSHOT_KEY
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value=MOONSHOT_KEY)
    "[获取API Key](https://platform.openai.com/account/api-keys)"

st.title("💬 Promptate 聊天机器人")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "您好！我是Promptate的聊天机器人，有什么可以帮助您的?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("请输入您的API KEY")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
