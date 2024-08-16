import streamlit as st
import google.generativeai as genai

#api_key = st.secrets["GOOGLE_API_KEY"]

#genai.configure(api_key= "api_key")

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Madiha Bibi")
    st.subheader("Frontend Developer")
with col2:
    st.image("images/myimage.png")

st.title(" ")

persona = """
        You are Madiha AI bot. You help people answer questions about your self (i.e Madiha)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Madiha: 
         
        Madiha has studied computer Software engineering and now searching job as a frontend Developer.
        Murtaza obtained his Bachelor’s degree in Software Engineering from Pakistan. She likes to think logically and help people and businesses.

        Madiha love to play cricket in childhood and now watch matches on TV. She is introvert but happy with like minded people gatherings. Now she started learning Python and AI.
 
        Madiha's Linkedin: www.linkedin.com/in/madiha-bibi-035356274
        Madiha's Email: madihabibi7@gmail.com 
        Madiha's Github :https://github.com/madiha786
        """
st.title("Madiha's AI Bot") 
st.write("Ask Anything about me")
st.write("")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
   prompt = persona + "Here is the question the user asked" + user_question
   response = model.generate_content(prompt)
   st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.title("About Me")
    st.write("I have studied Software engineering. I worked as a frontend developer for 3 months under mentoship. Now i am learning Python and AI")
    
with col2:
    st.image("images/project_img.png")    


st.write(" ")

#st.title("My Setup")
#st.image("images/setup.jpg")

st.write(" ")
st.title("")
st.title("My Skills")
st.slider("HTML", 0,100,80)
st.slider("CSS", 0,100,80)
st.slider("Wordpress", 0,100,70)
st.slider("Bootstrap", 0,100,80)
st.slider("Javascript", 0,100,60)
st.slider("Python", 0,100,60)

st.write(" ")
st.file_uploader("Upload a file")

st.title(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/Screenshot 2024-05-15 174529.png")
    

with col2:
    
    st.image("images/Screenshot 2024-07-08 234916.png")
   


with col3:
   
    st.image("images/project_img.png")

st.write(" ")
st.title("Contact")
st.subheader("For any inquiries, please contact me at")
st.subheader("madihabibi7@gmail.com")
