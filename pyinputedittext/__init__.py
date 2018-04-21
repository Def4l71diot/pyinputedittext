# define method signature, so IDEs like PyCharm can provide code completion(IntelliSense)
def input_edit_text(prompt, text_to_edit=''):
    pass


try:
    from .unix import input_edit_text
except ImportError:
    from .windows import input_edit_text
