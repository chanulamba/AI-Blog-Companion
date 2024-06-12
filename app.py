import streamlit as st 
import google.generativeai as genai
from apikey import google_gemini_api_key, openai_api_key
from streamlit_carousel import carousel
from openai import OpenAI
client = OpenAI(api_key=openai_api_key)

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

# setting up the model
model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)


# set app to wide mode
st.set_page_config(layout = "wide")

#title of the app
st.title('Blog Craft: Your AI Writing Companion')

#create a subheader
st.subheader('Now you can craft perfect blogs with the help of AI - Blogcraft is your New AI Blog Campanion')

#sidebar for user input

with st.sidebar:
    st.title("Input Blog Details")
    st.subheader("Enter details of the blog you want to generate")

    #Blog title
    blog_title = st.text_input("Blog Tilte")

    #keywords input
    keywords = st.text_area("keywords (comma seperated)")
    
    # Number of words
    num_words = st.slider("Number of words", min_value = 250, max_value = 1000, step = 250)

    # Number of images
    num_images = st.number_input("Number of images", min_value = 1, max_value = 5, step = 1)

    prompt_parts = [
        f"Generate a comprehensive,engaging blog post relevant to the given title \"{blog_title}\" and Keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. the blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintain a consistent tone throughout."
    ]
    
    
    #submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    #st.image("WhatsApp Image 2024-05-22 at 22.37.17_4d77ebd2.jpg")
    
    response = model.generate_content(prompt_parts)
    '''images = []
    
    for i in range(num_images):
      image_response = client.images.generate(
       model="dall-e-3",
       prompt=f"Generate a Blog Post Image on the title: {blog_title}",
       size="1024x1024",
       quality="standard",
       n=1,
      )
      images.append(image_response.data[0].url)
     
    
    for i in range(num_images):
        st.write(images[i])
        
    
    st.title("Your Blog Post:")'''

    st.write(response.text)

