import streamlit as st
import spacy
from spacy import displacy
import en_core_web_sm
from newspaper import Article
from pprint import pprint
nlp = en_core_web_sm.load()
st.title('Assignment')
st.title('NER Demo')
st.info('If using the url use the 1st box or use the 2nd box')
url=st.text_area("Enter the url")
if st.button('sumbit'):
    article = Article(url)
    article.download()
    article.parse()
    print(article.text)
    doc=nlp(article.text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)
text=st.text_area("Enter the para")
if(st.button("Submit")):
    doc = nlp(text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)