# Sample data, grading setup and analysis code for AI grading paper 

*Full paper title: Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback*
  
arXiv link: https://arxiv.org/abs/2412.06910

## Naming Conventions:
In the paper, the three questions are referred to as Q1, Q2 and Q3. In the analysis scripts, Q2 is referred to as Q10, and Q3 as Q8. Q1 was the first question being graded, so it doesn't have a specific name. The naming convention is caused by historical reasons, and is retained so that the code can be re-run as is.

## Contents:
1. **GPT Grading Scripts:** Contains python notebooks that are used for grading each of the three problems tested in the paper. Also contains python modules that are useful for carrying out AI grading.
    * Notebooks:
       - chatAPI_grading_withModules: This grades Question 1, the default question.
       - Grading_Final_Q10: This grades Question 2, the second question in the paper.
       - Grading_Final_Q8: This grades Question 3, the third question in the paper.
    * Utilities:
      - calc_price.py: Function to help calculate the cost of each grading action based on the model and publicly available cost information
      - pickle_tools.py: GPT connection objects cannot be serialized (pickled) and stored, unfortunately. So the common "dill" package will bug out when trying to store custom objects. I wrote those functions to pickle a list of python objects by name, excluding the objects that involve Azure communication, and then restored the saved objects automatically after opening a new session. Super useful for code development over a period of time.
      - print_response.py: functions to print GPT response
      - binary_output.py: functions to extract grading output such as "{1,0,1}" from the GPT grading response.
3. 

