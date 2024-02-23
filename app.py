from image_generator import ImageGenerator
import streamlit as st

if __name__ == '__main__':

    html_temp = """
    
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Text-to-Image Generation</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    with st.form(key='columns_in_form'):
        prompt = st.text_input('Enter the prompt:')
        col1, col2 = st.columns(2)

        with col1:
            image_size = st.selectbox('Image Size', ['1024x1024', '512x512', '256x256'])

        with col2:
            num_of_images = st.selectbox('Number of Images', [1, 2, 3, 4])

        generate = st.form_submit_button(label='Generate Image')

        if generate:
            image_generator = ImageGenerator()
            images = image_generator.generate_image(prompt=prompt, image_size=image_size, image_quality="standard", num_of_images=num_of_images)

            col1, col2 = st.columns(2)

            with col1:
                st.image(images[0], use_column_width=True)
                if len(images) > 2:
                    st.image(images[2], use_column_width=True)

            with col2:
                if len(images) > 1:
                    st.image(images[1], use_column_width=True)
                if len(images) > 3:
                    st.image(images[3], use_column_width=True)
