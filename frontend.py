import streamlit as st
from backend_update import generate_blog  # Assuming your main code is in agent.py
import os

st.set_page_config(page_title="AI Blog Agent", layout="centered")

st.title("✍️ Multi-Agent Blog Generator")
st.write(
    "Enter a topic, and our LangGraph agents will research, write, and illustrate a complete blog post."
)

topic = st.text_input(
    "What should the blog be about?",
    placeholder="e.g., The future of Data Science in 2026",
)

if st.button("Generate Blog"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner(
            "Agents are researching, writing, and generating images... This may take a minute or two."
        ):
            try:
                # Call your LangGraph workflow
                final_markdown = generate_blog(topic)

                st.success("Blog generated successfully!")

                # Render the markdown directly in the UI
                st.markdown(final_markdown, unsafe_allow_html=True)

                # Provide a download button
                st.download_button(
                    label="Download Markdown File",
                    data=final_markdown,
                    file_name="generated_blog.md",
                    mime="text/markdown",
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
