from flask import Flask, redirect, url_for, render_template, request, session
import os
from sql_queries import get_id, get_chinese, get_english
from sql_queries_quiz import get_answers_after, check_answer, get_question_after, get_table_length
from sql_queries_grammar import get_meaning, get_structure, get_structure_odr, get_data
from sql_queries_writing import get_data1
from random import shuffle

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

app.config['SECRET_KEY'] = 'KeyToGo'



# /////////////////////////////////////////////////////////////

@app.route('/')
def index():
    return render_template('index_real.html')


@app.route('/vocabulary')
def vocabulary():
    return render_template('index_vocab.html', visibility="hidden", visibility3='hidden')

@app.route('/vocabulary-quiz')
def vocabulary_quiz():
    start_quiz()
    return render_template('index_vocab_quiz.html', visibility="hidden", visibility3='hidden')

def show_table(table):
    return render_template('index_vocab.html', table1=get_id(table), table2=get_chinese(table),
                           table3=get_english(table), visibility="visible", visibility2="hidden", visibility3='hidden')


@app.route('/vocabulary-common-verbs')
def show_table_comon_verbs():
    return show_table('common_verbs')


@app.route('/vocabulary-common-adjectives')
def show_table_common_adjectives():
    return show_table('common_adjectives')


@app.route('/vocabulary-common-adverbs')
def show_table_common_adverbs():
    return show_table('common_adverbs')


@app.route('/vocabulary-table-daily-life')
def show_table_daily_life():
    return show_table('daily_life')


@app.route('/vocabulary-table-dress-style')
def show_table_dress_and_style():
    return show_table('dress_and_style')


@app.route('/vocabulary-table-cultural-life')
def show_table_culture():
    return show_table('cultural_life')


@app.route('/vocabulary-table-identity')
def show_table_identity():
    return show_table('identity_and_relationships')


@app.route('/vocabulary-table-social-media')
def show_table_social_media():
    return show_table('social_media')


@app.route('/vocabulary-table-local-area')
def show_table_local_area():
    return show_table('local_area')


@app.route('/vocabulary-table-weather-phrases')
def show_table_weather_phrases():
    return show_table('weather_phrases')


@app.route('/vocabulary-table-asking-for-directions')
def show_table_asking_for_directions():
    return show_table('asking_for_directions')


@app.route('/vocabulary-table-dealing-with-problems')
def show_table_dealing_with_problems():
    return show_table('dealing_with_problems')


@app.route('/vocabulary-table-school')
def show_table_school():
    return show_table('school')


@app.route('/vocabulary-table-future-aspirations')
def show_table_future_aspirations():
    return show_table('future_aspirations')


@app.route('/vocabulary-table-international-and-global')
def show_table_international_and_global():
    return show_table('international_and_global')






# /////////////////////////////////////////////////////////////

def start_quiz():
    session['question'] = 1
    session['answers'] = 1
    session['total'] = 1
    session['correct'] = 0

def get_next(answer, table_name):
    session['question'] = session['question'] + 1
    session['answers'] = session['answers'] + 1
    session['total'] += 1
    if check_answer(session['question']-1, answer, table_name):
        session['correct'] += 1

def question_form(question, answers):
    answers_list = [answers[0], answers[1], answers[2], answers[3]]
    shuffle(answers_list)
    return render_template('index_vocab_quiz.html', answers_list= answers_list, question=question[0],
                           visibility2='hidden', visibility='visible', visibility3='hidden')

def begin(table, route):
    if session['question'] > get_table_length(table) - 1 and get_question_after(table)!='null':
        return render_template('index_vocab_quiz.html', total=session['total'], correct=session['correct'],
                               visibility3='visible', visibility="hidden", visibility2='hidden', route=route)
    if request.method == 'POST':
        answer = request.form.get('ans_text')
        get_next(answer, table)
        result_question = get_question_after(table, session['question'])
        result_answers = get_answers_after(table, session['answers'])
    else:
        result_question = get_question_after(table, session['question'])
        result_answers = get_answers_after(table, session['answers'])
    return question_form(result_question, result_answers)

@app.route('/vocabulary-quiz-dress-style', methods=['POST', 'GET'])
def test1():
    route = '/vocabulary-quiz-dress-style'
    table = "dress_and_style_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-identity', methods=['POST', 'GET'])
def test2():
    route = '/vocabulary-quiz-identity'
    table = "identity_and_relationships_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-cultural-life', methods=['POST', 'GET'])
def test3():
    route = "/vocabulary-quiz-cultural-life"
    table = "cultural_life_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-social-media', methods=['POST', 'GET'])
def test4():
    route = '/vocabulary-quiz-social-media'
    table = "social_media_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-local-area', methods=['POST', 'GET'])
def test5():
    route = '/vocabulary-quiz-local-area'
    table = "local_area_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-weather-phrases', methods=['POST', 'GET'])
def test6():
    route = '/vocabulary-quiz-weather-phrases'
    table = "weather_phrases_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-asking-for-directions', methods=['POST', 'GET'])
def test7():
    route = '/vocabulary-quiz-asking-for-directions'
    table = "asking_for_directions_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-dealing-with-problems', methods=['POST', 'GET'])
def test8():
    route = '/vocabulary-quiz-dealing-with-problems'
    table = "dealing_with_problems_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-school', methods=['POST', 'GET'])
def test9():
    route = '/vocabulary-quiz-school'
    table = "school_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-future-aspirations', methods=['POST', 'GET'])
def test10():
    route = '/vocabulary-quiz-future-aspirations'
    table = "future_aspirations_quiz"
    return begin(table, route)

@app.route('/vocabulary-quiz-international-and-global', methods=['POST', 'GET'])
def test11():
    route = '/vocabulary-quiz-international-and-global'
    table = "international_and_global_quiz"
    return begin(table, route)



# ////////////////////////////////////////////////////////////////
@app.route('/grammar')
def grammar():
    return render_template('index_grammar.html', visibility="hidden", visibility3='hidden', table_grammar1=get_structure("grammar_list", 1),
                           table_grammar2=get_structure("grammar_list", 2), table_grammar3=get_structure("grammar_list", 3),
                           table_grammar4=get_structure("grammar_list", 4), table_grammar5=get_structure("grammar_list", 5),
                           table_grammar6=get_structure("grammar_list", 6), table_grammar7=get_structure("grammar_list", 7),
                           table_grammar8=get_structure("grammar_list", 8),table_grammar9=get_structure("grammar_list", 9),
                           table_grammar10=get_structure("grammar_list", 10), )

@app.route('/grammar-flashcards')
def grammar_flashcards():
    return render_template('index_grammar_flashcards.html', structures=get_structure_odr("grammar_list"),
                           meanings=get_meaning("grammar_list"), cards=get_data())


@app.route('/about-the-project')
def about_the_project():
    return render_template('index_about.html')


# /////////////////////////////////////////////
@app.route('/writing')
def writing():
    return render_template('index_writing.html', data=get_data1())


if __name__ == "__main__":
    app.run(debug=True)


