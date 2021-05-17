import streamlit as st
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.title('Spelling checker')


user_input = st.text_input('Enter some text')

zen = TextBlob(user_input)

words = zen.words

for sentence in zen.sentences:
    st.write(sentence)

# st.write(words)
# words = ["Data Scence", "Mahine Learnin"]
corrected_words = []
new_text = []
for i in words:
    corrected_words.append(TextBlob(i))
# print("Wrong words :", words)
# print("Corrected Words are :")
for i in corrected_words:
    new_text = i.correct()
    st.write(new_text)
# st.write(zen.sentences)






# Create some sample text
#  text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# st.pyplot()


