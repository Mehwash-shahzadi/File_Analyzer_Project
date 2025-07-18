# # %%
# import streamlit as st
# st.title('File Analyzer')
# def file_analysis(file_path):
#     with open(file_path,'r') as f:
#         data=f.read()
#         lines=data.split('\n')

#         #words in data
#         lower_words=[]
#         words=data.split()
#         for word in words:
#             lower_words.append(word.lower())

#         #total character   
#         character=0
#         for i in words:
#             for j in i:
#                 character+=1

#         #special character
#         special_character=0
#         for k in words:
#             for m in k :
#                 if not m.isalnum():
#                     special_character+=1
#         #uniue words
#         unique_words=[]
#         for word in lower_words:
#             unique_words.append(word)

        

#         #common words
#         def sort_dic(d):
#             return d[1]

#         common_dic={}
#         for l  in lower_words:
#             if l not in common_dic:
#                 common_dic[l]=1
#             else:
#                 common_dic[l]+=1
        
#         common_words=sorted(common_dic.items(),key=sort_dic)
            


#         #Longest word
#         longest_word=[]
#         for value in lower_words:
#             longest_word.append((len(value),value))
#         longest_word.sort()    

#     return {
#         'Total_Lines':len(lines),
#         'Total_Words':len(words),
#         'Total_Character':character,
#         'Special_Character':special_character,
#         'Unique_Words':len(set(unique_words)),
#         'common_words':common_words[-1][0],
#         'Longest_Word':longest_word[-1][1]
#     }
    
# file_path=input('enter the file_path')
# result=file_analysis(file_path)
# for key,value in result.items():
#     print(f'{key} : {value}')


# import streamlit as st

# st.title('📄 File Analyzer')

# # Upload a file
# uploaded_file = st.file_uploader("Upload a text file", type=['txt'])

# if uploaded_file is not None:
#     # Read file
#     data = uploaded_file.read().decode('utf-8')
#     lines = data.split('\n')

#     # Process words
#     words = data.split()
#     lower_words = [word.lower() for word in words]

#     # Total characters
#     character = sum(len(word) for word in words)

#     # Special characters
#     special_character = sum(1 for word in words for char in word if not char.isalnum())

#     # Unique words
#     unique_words = set(lower_words)

#     # Most common word
#     word_count = {}
#     for word in lower_words:
#         word_count[word] = word_count.get(word, 0) + 1
#     common_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

#     # Longest word
#     longest_word = max(lower_words, key=len)

#     # Display results
#     st.subheader("📊 Analysis Results")
#     st.write(f"**Total Lines:** {len(lines)}")
#     st.write(f"**Total Words:** {len(words)}")
#     st.write(f"**Total Characters (excluding spaces):** {character}")
#     st.write(f"**Special Characters:** {special_character}")
#     st.write(f"**Unique Words:** {len(unique_words)}")
#     st.write(f"**Most Common Word:** `{common_words[0][0]}` (appeared {common_words[0][1]} times)")
#     st.write(f"**Longest Word:** `{longest_word}`")

#     # Optional: Show full file content
#     with st.expander("📄 Show File Content"):
#         st.text(data)

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

# Streamlit app
st.title("📄 Text File Analysis App")
st.write("Upload a text file to analyze its content.")

# File uploader
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    try:
        # Read the file content as text
        file_content = uploaded_file.read().decode() if uploaded_file.type == "text/plain" else uploaded_file.read()
        result = file_analysis(file_content)

        # Display results
        st.subheader("📊 Analysis Results")
        for key, value in result.items():
            st.write(f"**{key.replace('_', ' ')}**: {value}")

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a text file to analyze.")