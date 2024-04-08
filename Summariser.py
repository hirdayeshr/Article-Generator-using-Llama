import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaresponse(input_text,no_words,blog_style):
    llms = CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',model_type="llama")


    template = '''Write an article {blog_style} job article for a topic {input_text}with{no_words}words'''
    prompt = PromptTemplate(input_variables=["blog_style", "no_words","input_text"],template=template)
    response=llms(prompt.format(blog_style=blog_style,no_words=no_words,input_text=input_text))
    return(response)

st.header(" Generate an Article")
inpText=st.text_input("Enter Topic")
col1,col2=st.columns([5,5])
with col1:
    noWords=st.text_input("No words")
with col2:
    blogStyle=st.selectbox("Choose one",["Causal","Proffessional","Personalised"])
submit=st.button("Generate Article")
if submit:
    st.write(getLLamaresponse(inpText,noWords,blogStyle))



