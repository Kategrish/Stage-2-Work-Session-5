def generate_lesson_html(lesson_title):
    html_text_1 = '''
<div class="lesson">
    <h2>''' + lesson_title
    html_text_2 = '''</h2>
<div class="notes">'''
    lesson_html = html_text_1 + html_text_2
    return lesson_html

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <div class="subhead">''' + concept_title
    html_text_2 = '''</div>
    <p>
    ''' + concept_description
    html_text_3 = '''
    </p>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text
    

def get_lesson_by_number(text, lesson_number):
        counter = 0
        while counter < lesson_number:
                counter = counter + 1
                next_lesson_start = text.find('Lesson')
                next_lesson_end   = text.find('Lesson', next_lesson_start + 1)
                if next_lesson_end >= 0:
                    lesson = text[next_lesson_start:next_lesson_end]
                else:
                    next_lesson_end = len(text)
                    if len(text) == 0:
                        return False
                    else:
                        lesson = text[next_lesson_start:]
                text = text[next_lesson_end:]
        return lesson




my_text = """Lesson 1: Introduction to 'Serious' Programming
TITLE: Computers and Computer Programming
DESCRIPTION: Computers are just machines. But unlike other machines like toasters or fridges, which are designed to do only a few things, computers can do anything. And they can do so with the help of programs, which tells them what to do. Without being programmed computers can do nothing so a program has to be a sequence of steps with instructions for a computer to do something useful. 
TITLE: Programming Languages
DESCRIPTION: For organizing program instructions we need special programming languages. And like human languages programming languages have grammar too. But unlike human languages  grammar grammar in programming is very strict and lacks any ambiguity. In languages like English, people can understand sentences that aren't grammatically correct or ambiguous sentences depending on the situation. Computers can't. If you make even a smallest mistake in the syntax, your code will not run.
TITLE: Python
DESCRIPTION: Python is a programming language. It also has a very strict grammar. For example, an  expression like 2 + 2 can be executed by Python, but 2 + 2 + can't because it's not part of the language. 
Lesson 2: Variables and Strings
TITLE: Variables in Python
DESCRIPTION: Programmers use variables to give names to values. Variables store the value of important data. They also make programs easier to understand. For example, looking at the code print 299792458 * 1.0 / 1000000000 * 100 it is hard to tell what 299792458 is and why these numbers are multiplied. But if we say that 299792458 is the speed of light and the code calculates how far light travels in centimeters in one nanosecond everything gets much clearer. 
TITLE: Assignment
DESCRIPTION: So to tell Python that 299792458 is the speed of light we need to assign a variable to this value. We can do so by writing speed_of_light = 299792458. The equals sign in this code 'takes the value of' not 'is the same as' like in maths. 
We can reassign a variable to a different value later in our code. Moreover, variables can be used in their own assignment expressions: for example, days = days + 1.
TITLE: Strings
DESCRIPTION: A string in Python is a sequence of characters surrounded by quotes. It's important to remember how strings behave in Python. For example, if we run print 4 + 4 the output will be 8. But the code '4' + '4' will give 44. Plus operator concatenates strings. 
Lesson 3: Input -> Function -> Output
TITLE: Functions
DESCRIPTION: Functions, or procedures, are like small programs in code that are aimed at specific tasks. When given parameters they run and return a value to the main program. Functions are really useful because they help to divide our code into blocks, which can be developed independently. Functions once defined can be reused again and again. 
TITLE: Making and using functions
DESCRIPTION: To make a function we need to start a line with a keyword def and then give the function a name followed by the function parameters in parentheses and a colon. Parameters are the values you pass to the function when you use (call) it later in your code. We also have to write a block ('body') of the function where we specify what to do with the input parameters. 
For example, the following code returns the next number:
def next_number(x):
	answer = x + 1
    	return answer
After you have defined a function, you can use it (call it) at any time, in any place of your code. To use a function we write the name of the function followed by the value or values in parentheses:
print next_number(45)
>>>46
The return keyword tells Python what the output must be. Without it the output will be:
>>>None
Lesson 4: Control Flow & Loops
TITLE: If Statement
DESCRIPTION: Programming languages provide various structures. One of the most widely used is decision making structure. It is usually formed with the keyword if followed by a test expression which sets a condition. The output of the test expression is a Boolean value (either True or False). In the indented block after the statement there is code that will run if the outcome is True. 
TITLE: While Loops
DESCRIPTION: While loops are similar to decision structures (they also have a condition) but they allow to execute a block of code any number of times as long as the test expression is true. While loops are really useful when we need to do a lot of repeated actions. They could save a lot of time to a programmer. A simple example of this structure can be:
i = 1
while i  <  10:
	print 'i is now ' + i
	i = i + 1
Running this code Python will print out numbers from 1 to 9. Notice that the body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates. Otherwise the loop will repeat forever, which is called an infinite loop.
"""

def get_lesson_title(lesson):
    start_location = lesson.find('Lesson ')
    end_location = lesson.find('TITLE:')
    lesson_title = lesson[start_location : end_location-1]
    return lesson_title

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

def make_list(text):
    my_list = []
    counter = 1
    lesson = get_lesson_by_number(text, counter)
    while lesson != False:        
        my_list.append(lesson)
        counter = counter + 1
        lesson = get_lesson_by_number(text, counter)
    return my_list

def generate_concepts_html(text):    
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)        
    return all_html

def generate_all_html(text):
    my_list = make_list(my_text)
    html = ''
    for e in my_list:
        lesson_title = get_lesson_title(e)
        lesson_html = generate_lesson_html(lesson_title)
        concepts_html = generate_concepts_html(e)
        html = html + lesson_html + concepts_html + '''
    </div>
</div>'''
    return html


print generate_all_html(my_text)



