# import streamlit as st
# from PIL import Image

# img = Image.open("bgImg.jpg")

# def main():
#     st.image(
#         img, 
#         width = 1000,
#         channels="RGB"
#     )
    
#     st.markdown(
#         """
#         <style>
#         body {
#             background-image: url('bgImg.jpg');
#             background-size: cover;
#         }
#         .content {
#             text-align: center;
#             padding: 220px; 
#             color: white;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Add content to the Streamlit app
#     st.markdown(
#         """
#         <div class="content">
#             <h1>Welcome to My Website</h1>
#             <p>This is some content on my website.</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()
