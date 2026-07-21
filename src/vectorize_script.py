import os
from dotenv import load_dotenv
from vectorize_book import vectorize_book_and_store_to_db , vectorize_chapters

load_dotenv()

CLASS_SUBJECT_NAME = os.getenv('CLASS_SUBJECT_NAME')

subject_db_name = CLASS_SUBJECT_NAME + "_db_vector"

vectorize_book_and_store_to_db(
    CLASS_SUBJECT_NAME , subject_db_name
)

vectorize_chapters(CLASS_SUBJECT_NAME)