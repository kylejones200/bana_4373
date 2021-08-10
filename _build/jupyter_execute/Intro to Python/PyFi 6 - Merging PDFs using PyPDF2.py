#!/usr/bin/env python
# coding: utf-8

# # Summary
# 
# Python can work with PDF documents to: extract data, extract tables, remove pages, or merge documents. The Python library that is most often used for analysis is called PyPDF2.
# 
# After completing this tutorial, you will know:
# * How to use Pandas DataFrames to open \*.csv and \*.xlsx files
# * How to apply functions to DataFrames to calcuate the mean and standard deviation
# * How to make basic plots
# 
# Let’s get started.
# 
# # Tutorial Overview
# This tutorial is divided into 1 part:
# 1. Worked Example

# # Worked Example

# In[1]:


import PyPDF2
from pathlib import Path

def PDFmerge(pdfs, output):
        
    pdf_write_object = PyPDF2.PdfFileWriter()
    
    for pdf in pdfs:
        pdf_read_object = PyPDF2.PdfFileReader(pdf)
        for page in range(pdf_read_object.numPages):
            pdf_write_object.addPage(pdf_read_object.getPage(page))

    final_file_object = open(output, 'wb')
    pdf_write_object.write(final_file_object)
    final_file_object.close() 
        
def main(input_folder, output_name):

    pathlist = Path(input_folder).glob('*.pdf')

    pdfs = [str(i) for i in pathlist]
    print(pdfs)
    PDFmerge(pdfs, output_name)
    
    
if __name__ == '__main__':
    main(input_folder='pdfs', output_name='pdfs/pdf_filename.pdf')


# # Extensions
# 
# This section lists some ideas for extending the tutorial that you may wish to explore.
# * Describe three examples when PyPDF2 could be applied for your work.
# 
# # Further Reading
# This section provides more resources on the topic if you are looking to go deeper.
# 
# ## Books
# * Automate the boring stuff, by Al Sweigart. See Chapter 15. https://automatetheboringstuff.com
# 
# ## APIs
# * PyPDF2. https://pythonhosted.org/PyPDF2/
#     
# # Summary
# 
# In this tutorial, you were introduced to the PyPDF2 library. Specifically, you learned:
# * How to use PyPDF2 to open and merge PDF documents.
# 
# 

# In[ ]:




