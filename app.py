# Core Pkgs
import streamlit as st


# Addtional Pkgs


# Functions

def main():
    """
    All your code goes here
    """
    st.title("Hello Streamlit")

    st.text("Hello world this is a text")

    st.text("This is cool")

    name = "John"

    st.text(f"Hello {name}")

    st.text("=========================")

    # Header
    st.header("This is a header")

    # SubHeader
    st.subheader("This is a subheader")

    # Markdown
    st.markdown("## This is markdown")


if __name__ == '__main__':
    main()
