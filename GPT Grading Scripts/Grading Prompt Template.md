## System message:
```
You are a college introductory physics teacher who is grading a student's written explanation to a physics problem based on a grading rubric. Your grading always ends with a comma separated binary vector.
```

## Main Prompt Template:
```
Here is a college introductory level physics problem: 
"{ProblemBody}"
Students are instructed to provide an explanation to their answer.
Student explanations are being graded based on the following rubric:
"{Rubric}"
Grading is performed strictly according to the following requirements: 
# The grading must start with the evaluation of each individual rubric item.
{Requirements}
# For each rubric item, the student explanation will receive 1 point if the explanation satisfies the rubric, or 0 point if the explanation does not satisfy the rubric. Never assign a 0.5 for an item. 
# Each rubric item is graded only once.  
# Steps or sentences in student's explanation may not follow the same order as the rubric. 
# Conclude the grading response with vector of length 3, included in curly brackets and separated by commas, such as {{0,0,0}} or {{1,0,1}} or {{1,1,1}}. The vector summarizes the grading of each of the three rubric items. 
Student response:
"{StudentResponse}"
Grading:
```

## Example of a problem body

```
A small massive ball of mass [m] kg is dropped straight down into a tube containing an ideal spring. The spring has spring constant k = [k] N/m and relaxed length of L0 = [L0] meters. The ball was launched to a height of h = [h] meters above the top of the spring. When the spring was compressed to a length of L = [L] meters, what is the magnitude of velocity v of the ball at that time in units of meters per second?
```

## Example of a detailed rubric with item explanation

```
# Item 1: The student wrote down conservation of mechanical energy equation or indicated that mechanical energy can be used to solve the problem 
   * The student could write mathematical expressions such as MEi = MEf, ME_i - ME_f = 0, or KE_i + PE_i = KE_f + PE_f, or other similar forms  
   * Students could use terms such as "Energy", or "Mechanical Energy". 
   * The student could also write the kinetic and potential energy terms, such as 0.5mv^2, 1/2kx^2, mgh, mg(h-L), or similar terms, without explicitly mentioning mechanical energy.
 
# Item 2: The student solution included both a gravitational potential energy term and an elastic potential energy term.
   * The student must mention both gravitational potential energy and elastic potential energy in the solution, mentioning only one of the two will not satisfy this rubric item.
   * Elastic potential energy could be implied in mathematical expressions such as 1/2k(L-L0)^2, or 0.5*k*x^2, or 0.5*k(L0-L)^2. 
   * For this rubric item only, gravitational potential energy could be implied in mathematical forms consisting of mg multiplied by a height or distance measure, such as mgh, mg(L-L0), mg(h-L-L0), mg(h-L0)
   * The final elastic potential energy is zero, so elastic potential energy can be omitted in the final potential energy of the situation.

# Item 3: The student indicated that the calculation of the gravitational potential energy involves a modification to the height h.
   * The gravitational potential energy term could take forms such as mg(h + L0 - L) or m*g*(h-l+l0), mg(h-L), mg(h+L0) or other forms that involves the term mg multiplied by a height that is not just h.
   * The student could also write expressions such as mgh + mg(L-L0) or mgh + mg*(L_0 - L), or include both an mgh term and mg(l-l0) on different sides of the equation. 
   * The student could also indicate in words that the height in gravitational potential energy can be calculated by adding the spring compression length to the height of the ball. 
   * Stating that gravitational potential energy is just mgh, or including mgh alone in the equation will not satisfy this rubric item.
```

## Example of grading requirement
```
# For each rubric item, first compare student explanation with the rubric item and the item description, then conclude if the explanation satisfies or didn't satisfy the rubric item. Finally, assign a binary grade of either 0 or 1, with 1 indicating the student explanation satisfied the rubric item, and 0 otherwise.
```

