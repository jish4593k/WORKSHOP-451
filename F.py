import streamlit as st
import fitz  # PyMuPDF for PDF handling
import torch
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import numpy as np


def main():
    st.header('PDF Chat App')
    
   
    pdf_file = st.file_uploader("Upload your PDF here", type='pdf')

    if pdf_file is not None:
       
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        
       
        "
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text += page.get_text()
       
        sentences = text.split(". ")

       r
        tensor_sentences = torch.tensor(sentences)

     
        embeddings = torch.mean(torch.rand(len(sentences), 300), dim=1)

        
        sns.set_theme()
        st.subheader("Random Data Visualization")
        random_data = np.random.randn(100, 2)
        sns.scatterplot(x=random_data[:, 0], y=random_data[:, 1])
        st.pyplot()
 
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt")])
        st.write(f"Selected File: {file_path}")

       
        st.subheader("Processed Text:")
        st.write(sentences)

       t
        query = st.text_input("Ask a question:")
        if query:
            st.write(f"You asked: {query}")

        pdf_document.close()

if __name__ == '__main__':
    main()
