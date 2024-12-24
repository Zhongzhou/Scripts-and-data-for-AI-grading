### This module is used for prompt engineering. It prints the response and grading text one by one, formatting it in a readable format. 

def print_oneRow(row, response_colName, grading_colName):
    print(f"Response {row.name + 1}:\n {row[response_colName]}\n")
    print('-'*100)
    print(f"Grading {row.name + 1}: {row[grading_colName]}\n")
    print("="*100)


def print_gradingOutcome(df, grading_colName, response_colName = 'response'):
    df[[response_colName, grading_colName]].apply(lambda x:print_oneRow(x, response_colName, grading_colName), axis = 1)


def print_oneFeedback(row, response_colName, feedback_colName, grade_colName):
    print(f"Response {row.name + 1}:\n {row[response_colName]}\n")
    print('-'*100)
    print(f'Score {row.name + 1}: {row[grade_colName]}')
    print("-"*100)
    print(f"Feedback {row.name + 1}: {row[feedback_colName]}\n")
    print("="*100)

def print_feedback(df, feedback_colName, grade_colName, response_colName = 'response'):
    df[[response_colName, feedback_colName, grade_colName]].apply(lambda x:print_oneFeedback(x, response_colName, feedback_colName, grade_colName), axis = 1)