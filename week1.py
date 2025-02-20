import streamlit as st
def file_analysis(file):
    text = file.getvalue().decode('utf-8', errors='ignore') 

    lines=text.split('\n')

    character=text.replace(" ","").replace("\n","")

    words=text.split()

    unique_words=set(words)

    special_character=sum(1 for char in text if not char.isalnum() and not char.isspace())

    common_words=max(set(words),key=words.count) if words else "N/A"

    longest_word=max(words,key=len) if words else "N/A"
    return {
        'Total Lines':len(lines),
        'Total Character':len(character),
        'Words':len(words),
        'Special_character':special_character,
        'Unique_words':len(unique_words),
        'Common_words':common_words,
        'Longest_word':longest_word
    }

st.title('File Analyzer Pro')
file = st.file_uploader('Upload a text file')

if file:
    analysis = file_analysis(file)
    st.write(analysis)