import re

#Creates a regexp matching pattern for n digits of binary output.
def Create_Search(n:int):
    # Create the regex pattern for each binary digit with optional spaces
    element_pattern = r'\s*[01],?'
    
    # Combine the individual patterns into a single pattern
    combined_pattern = ''.join([element_pattern] * n)

    
    # Create the full pattern with curly braces
    full_pattern = r'\{' + combined_pattern + r'\}'
    
    return full_pattern


#extracts a binary vectory and excludes all the 
def Extract_binary(text, nItems):
    match = re.search(Create_Search(nItems), text)
    if match:
        binary = re.sub(r'[{}\s]', '', match.group(0))
        return binary
    else:
        return None