import docx


def modify_text(doc_name):
    # Open the Word document
    doc = docx.Document(doc_name)

    # Loop through the paragraphs in the document
    for para in doc.paragraphs:
        # Get the text of the paragraph
        text = para.text
        # Modify the text
        text = text.upper()
        # Set the modified text back to the paragraph
        para.text = text

    # Save the modified document
    doc.save(doc_name)


# Test the function
modify_text("test.docx")
