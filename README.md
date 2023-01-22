# COMP3940 Exam Practice Generator

## Usage
You can just run `python exam_generator.py`. The output will be a file named `example_test.tex` - you can copy-paste the contents into Overleaf or some other tex editor (Overleaf is a safe bet for all the weird graph drawings but totally up to you).

## Contribution
### Question styles
The questions should be roughly exam level - based on worksheets for example. **Avoid posting exact coursework questions, to avoid leaking them publicly - worksheet style questions are fair game**.

### Git
To keep stuff neat, please make your own branches for each question you write, and push your changes there. Please don't push to main directly (create a PR instead).

### Implementation
There are three files for the three sections of the module:
- `maxflow.py`
- `matchings.py`
- `complexity.py`


If you write questions, please have your function interface like so (just for consistency :) ):

```Python
def practice_question_name(f): 
    code goes here...
```

where `f` is a Python file object.

you can use `f.write` to write your LaTeX directly to the file. Please give it a test run to see that it works on a LaTeX editor before pushing.

Please keep functions in the right Python file.

Once you've written, there are 3 functions in `exam_generator.py` that do all the generation, one for each section. In each of these functions there is an array that looks like this: `questions = [question_1, question_2, ...]`

Please attach the name of your function in this array so that the script calls it during generation.

Think that's all from me

Cheers everyone

Raph :)