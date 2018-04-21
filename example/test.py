#!/usr/bin/python3
from pyinputedittext import input_edit_text

text_to_edit = 'edit this'

edited_text = input_edit_text('Please edit this text: ', text_to_edit)

print()

print("Text after edit: " + edited_text)
