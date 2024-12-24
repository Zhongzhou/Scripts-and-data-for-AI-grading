import pandas as pd

def Calc_Price_oneGrading(aiMessage, modelUsed : str):
    #can write some data verification here. need to pull the first level names from pricingModel
    pricingModel = {
        'gpt35' : {
            'input' : 0.002,
            'output' : 0.002
        },
        'gpt4o' : {
            'input' : 0.005,
            'output' : 0.015
        }
    }

    modelNames = list(pricingModel.keys())

    if modelUsed not in modelNames:
        raise ValueError(f"Error: {modelUsed} is not a recognized model name. \nValid model names are {modelNames}")

    usageData = aiMessage.usage_metadata
    cost = usageData['input_tokens']/1000 * pricingModel[modelUsed]['input'] + usageData['output_tokens']/1000 * pricingModel[modelUsed]['output']
    return(round(cost, 6))

def Calc_Price(grading_outcomes : pd.Series, modelUsed : str):
    return(
        grading_outcomes.apply(lambda x: Calc_Price_oneGrading(x, modelUsed= modelUsed)).sum()
    )