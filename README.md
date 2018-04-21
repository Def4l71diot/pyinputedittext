# PyInputEditText
Cross-platform package that allows editing text in console (input() with default value for editing)

WARNING: might not work in some IDEs, as they don't use the terminal native to the os. In those cases you should launch your script from terminal (i.e. `python3 myscript.py`) 

# Usage

```python
from pyinputedittext import input_edit_text

text_to_edit = 'Edit this'

edited_text = input_edit_text('Please edit this text: ', text_to_edit)

print(edited_text)
```
