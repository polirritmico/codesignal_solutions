# My solutions to Codesignal questions

This are my solutions for the Codesignal questions. Initially, my focus was on
writing functional code just to pass the tests. However, after tackling a few
questions, I decided to shift my focus towards crafting clean and elegant code.
My goal was to create a small library for learning, practicing, and referencing
good coding and language-specific practices.

I'm not shure if I completely achieved this, but I am very happy with most of
the answers provided.

---------------------------------------------------------------------------------

Additionally, after working through numerous problems, I developed this simple
script to automate the layout generation for each new question.

## setPython:

A small BASH script to automate the environment setup for each question.
This script asumes that the template files are located into the `Python` folder:

> - `Python/template.py`
> - `Python/template_test.py`

It should generate the `currentQuestion.py` and `test_currentQuestion.py` files
with the content from the layout and the imports needed in the test file. Also
it should make the `__main__.py` link that points to `currentQuestion.py`.

```command
$ ./setPython -h
```

```
Usage: ./setPython NAME
Options:
-r NAME → Restore 'NAME.py' and 'test_NAME.py'
-e edit with nvim
-c || -d → Clean
-m → move to 'Python' folder
```

