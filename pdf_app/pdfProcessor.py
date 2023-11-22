import PyPDF2
import re

# pdf_app/pdf_processor.py
import PyPDF2
import re

def process_pdf(file):
    try:
        text = ""
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

        if validate_pdf(text):
            print("The PDF follows the expected format.")
        
            result = process_text(text)

            return result
        else:
            print("The PDF does not follow the expected format.")
            return "Not a valid format"
    except Exception as e:
        print("The error is: ",e)
        return "error" 

def process_text(text):
    try:
        # Use regular expression to extract question number and sub-question number
        sections = re.split(r'Question\n(\d+)\.(\d+)', ''.join(text))[1:]

        # Initialize an empty list to store the dictionaries
        result = []

        # Iterate through the sections and extract information
        for i in range(0, len(sections), 3):
            question_no = int(sections[i])
            sub_question = int(sections[i + 1])

            # Use regular expression to extract question and answer parts
            match = re.search(r'Question:(.*?)Answer:', sections[i + 2], re.DOTALL)
            question_text2 = match.group(1).replace("\n", " ").strip()[-9:] if match else ''
            pattern_marks = r'\((\d+)\s*mark(s)?\)'
            match_marks = re.search(pattern_marks, question_text2)
            digit = int(match_marks.group(1))

            question_text = match.group(1).replace("\n", " ").strip()[:-9] if match else ''

            match = re.search(r'Answer:(.*?)(?:Question|$)', sections[i + 2], re.DOTALL)
            answer_text = match.group(1).replace("\n", " ").strip() if match else ''

            # Create a dictionary and append it to the result list
            result.append({
                "section": question_no,
                "question_no": sub_question,
                "marks": digit,
                "question": question_text,
                "answer": answer_text
            })
        return result
    except Exception as e:
        print(e)
        return e
    

def validate_pdf (text):
    try:
        # Define a regular expression pattern to match the format
        pattern = r'Question\s*\d+\.\d+\s*Question:\s*(.*?)\(\d+\s*mark[s]?\)\s*Answer:\s*(.*?)\n'
        
        # Use re.findall to find all occurrences of the pattern in the text
        matches = re.findall(pattern, text, re.DOTALL)

        # Return True if at least one match is found, else return False
        return bool(matches)
    except Exception as e:
        print(e)
        return e
    
