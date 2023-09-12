import streamlit as st
import pandas as pd
import similar as simi



def main():
    
    st.title("Student partner")

    name               = st.text_input("Name", "Your name")
    age                = int(st.number_input('Age'))
    gender             = st.text_input("Gender", "Your gender")
    mail               = st.text_input("Mail", "Your Mail Id")
    lang               = st.text_input("Language", "Your language")

    Interest = st.selectbox(
        'Area of Interest',
        ('Machine Learning','Artificial Intelligence', 'Data Science', 'Web - Front end', 'Web - Back end', 'Web - Full stack', 'Competitive programming'))

    linkedin           = int(st.number_input('LinkedIn activity (1-10)'))
    github             = int(st.number_input('Github activity (1-10)'))
    paper              = int(st.number_input('Paper published (1-10)'))


    info = {id:"1001","name":name,"age":age,"gender":gender,"email":mail,"language":lang,"linkedin_act":linkedin,"github_act":github,"paper_published":paper, "interest":Interest}
     
    
    if st.button("Predict"):

        result = simi.find_similar_student(info)
        data = pd.DataFrame.from_dict(result)

        st.table(data[1:])
    
if __name__ == "__main__":
    main()