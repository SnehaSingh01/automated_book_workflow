# automated_book_workflow


This project is a complete pipeline that helps automate the creation and editing of book chapters using AI, human feedback, and export tools. It's great for authors, editors, or anyone curious about combining AI with writing.

What It Does
This tool takes a chapter from a book, rewrites it using AI, reviews and edits it, and then lets a human user do the final review. After that, the final version can be exported as a PDF or Word file. There's also a smart search option to help you find past versions based on what you're looking for.

Main Features
Scrapes a chapter from a book (from a source like Wikisource)

Rewrites the chapter using an AI writer

Reviews the AI-written draft using another AI reviewer

Allows human editing through a user-friendly interface

Saves the final version in a versioned database

Lets you export the final text as a PDF or .docx file

Includes a smart search to help you find older versions using a query

How to Run It
Make sure you have Python installed.

Set up a virtual environment if you want (recommended).

Install the required libraries using this command:

pip install -r requirements.txt

Run the main automation script:

python main.py

To open the user interface for human editing:

streamlit run ui/editor_ui.py

After human editing, export the file by clicking the PDF or Word download buttons in the interface.

Folder Structure
scraping/: Code that fetches the book chapter

ai_agents/: AI writer and reviewer code

ui/: Streamlit user interface for editing

output/: Stores all the generated text files and exported files

versioning/: Manages version history with ChromaDB

rl_search/: Search functionality based on user queries

main.py: Runs the full automation pipeline

Who Can Use This
Writers looking for AI writing support

Editors who want to speed up their workflow

Students building a writing or AI project

Beginners who want to learn about combining web scraping, AI, and interfaces

Final Notes
This project is a mix of AI creativity and human judgment. It gives you full control while using AI to save time and effort. You can keep improving it by adding more chapters, better AI models, or more export options.
