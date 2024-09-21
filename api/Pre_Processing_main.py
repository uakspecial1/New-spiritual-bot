#!/usr/bin/env python
# coding: utf-8

# In[20]:



#Pre-Processing code for PDF files 



import re
from PyPDF2 import PdfReader

def extract_content(path):
    reader = PdfReader(path)
    return " ".join(page.extract_text() for page in reader.pages).strip()

def clean_text(text):
    # Remove "***Om Shanti***" and similar patterns
    text = re.sub(r'\*\*.*?\*\*', '', text)
    # Remove "Om Shanti" in all its forms
    text = re.sub(r'Om Shanti', '', text, flags=re.IGNORECASE)
    # Remove page numbers and patterns like 'x/x'
    text = re.sub(r'\b\d+/\d+\b', '', text)
    # Remove any extra spaces left after cleaning
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_details(text):
    # Extracting date
    date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    
    # Extracting Essence, Question, Answer, Essence of Dharna, Blessing, and Slogan
    essence_match = re.search(r'Essence:(.*?)Question:', text, re.DOTALL | re.MULTILINE)
    question_match = re.search(r'Question:(.*?)Answer:', text, re.DOTALL | re.MULTILINE)
    answer_match = re.search(r'Answer:(.*?)Essence for dharna:', text, re.DOTALL | re.MULTILINE)
    dharna_match = re.search(r'Essence for dharna:(.*?)Blessing:', text, re.DOTALL | re.MULTILINE)
    blessing_match = re.search(r'Blessing:(.*?)Slogan:', text, re.DOTALL | re.MULTILINE)
    slogan_match = re.search(r'Slogan:(.*?)(\*+.*)?$', text, re.DOTALL | re.MULTILINE)
    
    essence = essence_match.group(1).strip() if essence_match else "Essence not found"
    question = question_match.group(1).strip() if question_match else "Question not found"
    answer = clean_text(answer_match.group(1).strip()) if answer_match else "Answer not found"
    dharna = dharna_match.group(1).strip() if dharna_match else "Essence of Dharna not found"
    blessing = blessing_match.group(1).strip() if blessing_match else "Blessing not found"
    slogan = slogan_match.group(1).strip() if slogan_match else "Slogan not found"
    
    return {
        "Date": date_match.group() if date_match else "Date not found",
        "Essence": essence,
        "Question": question,
        "Answer": answer,
        "Essence for Dharna": dharna,
        "Blessing": blessing,
        "Slogan": slogan
    }

# Path to your PDF file
path = r"C:\Users\Dell\OneDrive\Documents\Major Project Spiritual Bot\preprocessing final\data\sakarmurliAug26.pdf"

text = extract_content(path)
details = extract_details(text)

# Print the extracted details
for key, value in details.items():
    print(f"{key}: {value}")


# In[19]:


#Pre-Processing for HTML files 


import re
from bs4 import BeautifulSoup

# Function to read HTML file and extract text data
def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='windows-1252') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        cleaned_paragraphs = [p.replace('\xa0', ' ') for p in paragraphs]
        return cleaned_paragraphs
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return []

# Function to remove unwanted text from a line
def remove_unwanted_text(text):
    unwanted_patterns = [r'ओम शान्ति', r'अव्यक्त बापदादा', r'मधुबन']  # Add more unwanted patterns if needed
    for pattern in unwanted_patterns:
        text = re.sub(pattern, '', text)
    text = text.strip()  # Remove leading and trailing whitespace
    return text

# Function to extract the date from a line
def extract_date(text):
    # Remove any extra characters around the date
    text = re.sub(r'[^\d\-\/]', '', text)  # Remove non-digit and non-date separators
    
    date_patterns = [
        r'\b\d{2}[-/]\d{2}[-/]\d{2}\b',  # DD-MM-YY or DD/MM/YY
        r'\b\d{2}[-/]\d{2}[-/]\d{4}\b',  # DD-MM-YYYY or DD/MM/YYYY
        r'\b\d{4}[-/]\d{2}[-/]\d{2}\b',  # YYYY-MM-DD or YYYY/MM/DD
        r'\b\d{4}[-/]\d{2}\b'            # YYYY-MM or YYYY/MM
    ]
    for pattern in date_patterns:
        date_match = re.search(pattern, text)
        if date_match:
            return date_match.group()
    return None

# Function to extract the second sentence and use it as the title
def extract_title(paragraphs):
    sentences = []
    for paragraph in paragraphs:
        sentences.extend(re.split(r'(?<=[.!?])\s+', paragraph.strip()))
    if len(sentences) > 1:
        return sentences[1]  # Return the second sentence as the title
    return None

# Function to clean and normalize text
def clean_text(text_list):
    cleaned_list = []
    for text in text_list:
        text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space
        text = text.replace('\n', ' ').replace('\t', '')  # Remove newlines and tabs
        cleaned_list.append(text)
    return cleaned_list

# Example usage
path = r"C:\Users\Dell\OneDrive\Documents\Major Project Spiritual Bot\preprocessing\data\AMurli20Feb01English.htm"
text_array = read_html_file(path)
cleaned_text_list = clean_text(text_array)

# Remove unwanted text from the first line and extract the date
date = None
if cleaned_text_list:
    date_line = remove_unwanted_text(cleaned_text_list[0])
    date = extract_date(date_line)
    if date:
        cleaned_text_list[0] = date  # Replace the first line with just the date
    else:
        print("No date found in the first line.")

# Extract the second sentence as the title
title = extract_title(cleaned_text_list)

# Ensure title is not included in the content
if title and cleaned_text_list:
    content = [line for line in cleaned_text_list[1:] if line != title]
else:
    content = cleaned_text_list[1:]  # Skip the first line since it's only the date now

# Output the extracted information
print("Date:", date)
print("Title:", title)
print("Content:")
for line in content:
    print(line)


# In[21]:


# Merged Code for PDF and HTML files Pre-Processing
import os
import re
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Function to read and clean HTML file content
def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='windows-1252') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        cleaned_paragraphs = [p.replace('\xa0', ' ') for p in paragraphs]
        return cleaned_paragraphs
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return []

# Function to clean and normalize text
def clean_text(text_list):
    cleaned_list = []
    for text in text_list:
        text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space
        text = text.replace('\n', ' ').replace('\t', '')  # Remove newlines and tabs
        cleaned_list.append(text)
    return cleaned_list

# Function to remove unwanted text from a line (for HTML)
def remove_unwanted_text(text):
    unwanted_patterns = [r'ओम शान्ति', r'अव्यक्त बापदादा', r'मधुबन']  # Add more unwanted patterns if needed
    for pattern in unwanted_patterns:
        text = re.sub(pattern, '', text)
    text = text.strip()
    return text

# Function to extract date from a line (for HTML)
def extract_date(text):
    text = re.sub(r'[^\d\-\/]', '', text)  # Remove non-digit and non-date separators
    date_patterns = [
        r'\b\d{2}[-/]\d{2}[-/]\d{2}\b',
        r'\b\d{2}[-/]\d{2}[-/]\d{4}\b',
        r'\b\d{4}[-/]\d{2}[-/]\d{2}\b',
        r'\b\d{4}[-/]\d{2}\b'
    ]
    for pattern in date_patterns:
        date_match = re.search(pattern, text)
        if date_match:
            return date_match.group()
    return None

# Function to extract the second sentence and use it as the title (for HTML)
def extract_title(paragraphs):
    sentences = []
    for paragraph in paragraphs:
        sentences.extend(re.split(r'(?<=[.!?])\s+', paragraph.strip()))
    if len(sentences) > 1:
        return sentences[1]
    return None

# PDF-specific functions
def extract_content_from_pdf(path):
    reader = PdfReader(path)
    return " ".join(page.extract_text() for page in reader.pages).strip()

def clean_pdf_text(text):
    text = re.sub(r'\*\*.*?\*\*', '', text)
    text = re.sub(r'Om Shanti', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+/\d+\b', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_details_from_pdf(text):
    date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    essence_match = re.search(r'Essence:(.*?)Question:', text, re.DOTALL | re.MULTILINE)
    question_match = re.search(r'Question:(.*?)Answer:', text, re.DOTALL | re.MULTILINE)
    answer_match = re.search(r'Answer:(.*?)Essence for dharna:', text, re.DOTALL | re.MULTILINE)
    dharna_match = re.search(r'Essence for dharna:(.*?)Blessing:', text, re.DOTALL | re.MULTILINE)
    blessing_match = re.search(r'Blessing:(.*?)Slogan:', text, re.DOTALL | re.MULTILINE)
    slogan_match = re.search(r'Slogan:(.*?)(\*+.*)?$', text, re.DOTALL | re.MULTILINE)
    
    return {
        "Date": date_match.group() if date_match else "Date not found",
        "Essence": essence_match.group(1).strip() if essence_match else "Essence not found",
        "Question": question_match.group(1).strip() if question_match else "Question not found",
        "Answer": clean_pdf_text(answer_match.group(1).strip()) if answer_match else "Answer not found",
        "Essence for Dharna": dharna_match.group(1).strip() if dharna_match else "Essence of Dharna not found",
        "Blessing": blessing_match.group(1).strip() if blessing_match else "Blessing not found",
        "Slogan": slogan_match.group(1).strip() if slogan_match else "Slogan not found"
    }

# Main function to handle both PDF and HTML files
def process_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.pdf':
        print("Processing PDF file...")
        text = extract_content_from_pdf(file_path)
        details = extract_details_from_pdf(text)
        # Output the extracted details
        for key, value in details.items():
            print(f"{key}: {value}")
    elif file_extension.lower() in ['.html', '.htm']:
        print("Processing HTML file...")
        text_array = read_html_file(file_path)
        cleaned_text_list = clean_text(text_array)
        
        # Remove unwanted text and extract date from the first line
        date = None
        if cleaned_text_list:
            date_line = remove_unwanted_text(cleaned_text_list[0])
            date = extract_date(date_line)
            if date:
                cleaned_text_list[0] = date
            else:
                print("No date found in the first line.")
        
        # Extract title from the second sentence
        title = extract_title(cleaned_text_list)
        
        # Remove title from content
        if title and cleaned_text_list:
            content = [line for line in cleaned_text_list[1:] if line != title]
        else:
            content = cleaned_text_list[1:]

        # Output the pre-processed details
        print("Date:", date)
        print("Title:", title)
        print("Content:")
        for line in content:
            print(line)
    else:
        print("Unsupported file type.")

# Example usage
file_path = r"C:\Users\Dell\OneDrive\Documents\Major Project Spiritual Bot\preprocessing final\data\AMurli18Feb93.htm" # Change this to your file path
process_file(file_path)


# In[ ]:




