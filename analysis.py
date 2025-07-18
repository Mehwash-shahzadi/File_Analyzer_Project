import streamlit as st

def file_analysis(file_content):
    # File content is already a string (text)
    data = file_content
    lines = data.split('\n')

    # Words in data
    lower_words = []
    words = data.split()
    for word in words:
        lower_words.append(word.lower())

    # Total characters
    character = 0
    for i in words:
        for j in i:
            character += 1

    # Special characters
    special_character = 0
    for k in words:
        for m in k:
            if not m.isalnum():
                special_character += 1

    # Unique words
    unique_words = []
    for word in lower_words:
        unique_words.append(word)

    # Common words
    def sort_dic(d):
        return d[1]

    common_dic = {}
    for l in lower_words:
        if l not in common_dic:
            common_dic[l] = 1
        else:
            common_dic[l] += 1

    common_words = sorted(common_dic.items(), key=sort_dic)

    # Longest word
    longest_word = []
    for value in lower_words:
        longest_word.append((len(value), value))
    longest_word.sort()

    return {
        'Total_Lines': len(lines),
        'Total_Words': len(words),
        'Total_Character': character,
        'Special_Character': special_character,
        'Unique_Words': len(set(unique_words)),
        'Common_Word': common_words[-1][0] if common_words else "None",
        'Longest_Word': longest_word[-1][1] if longest_word else "None"
    }

st.title("📄 Text File Analysis App")
st.write("Upload a text file to analyze its content.")

uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode() if uploaded_file.type == "text/plain" else uploaded_file.read()
        result = file_analysis(file_content)

        st.subheader("📊 Analysis Results")
        for key, value in result.items():
            st.write(f"**{key.replace('_', ' ')}**: {value}")

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a text file to analyze.")