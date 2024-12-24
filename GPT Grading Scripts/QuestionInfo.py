Question_1 = {
        'Body':"""Swimmers at a water park have a choice of two frictionless water slides. Both slides drop over the same height h: slide 1 is straight while slide 2 is curved, dropping quickly at first and then leveling out. How does the speed v1 of a swimmer reaching the bottom of slide 1 compare with v2, the speed of a swimmer reaching the end of slide 2?""",
        'Rubric':""""""
    }
Question_2 = {
        'Body':"""A small massive ball of mass [m] kg is dropped straight down into a tube containing an ideal spring. The spring has spring constant k = [k] N/m and relaxed length of L0 = [L0] meters. The ball was launched to a height of h = [h] meters above the top of the spring. When the spring was compressed to a length of L = [L] meters, what is the magnitude of velocity v of the ball at that time in units of meters per second?""",
        'Rubric':""
    }
Question_3 = {
        'Body':"""Two icy boulders in Saturn's rings approach each other, collide, and stick together as shown in the figure below. The first has a mass of [m1] kg and velocity of [v1] m/s.The second has a mass of [m2] kg and velocity of [v2] LaTeX: m/s. The angle between the two velocities is theta. Determine the magnitude of their velocity after they collide. Round your answer to the nearest 1 decimal place in units of m/s.""",
        'Rubric':""
    }

Question_1['Rubric'] = """
# Item 1: The student should mention either one of the following: 
  * conservation of energy OR
  * work and kinetic energy theorem 

# Item 2: The student mentioned either one of the following: 
   * No net external non-conservative work is being done, so mechanical energy  is conserved for the system  OR 
   * the slide is frictionless/smooth OR
   * gravity is the only force that does work on the girl. 

# Item 3: The student indicated either one of the following: 
   * potential energy is converted into kinetic energy OR  
   * Work done by gravity/gravitational force is equal to the change in kinetic energy of the girl"""


Question_2['Rubric'] = """
# Item 1: The student wrote down conservation of mechanical energy equation or indicated that mechanical energy can be used to solve the problem 

# Item 2: The potential energy term of the conservation of mechanical energy formula contains both a gravitational potential energy term and an elastic potential energy term.

# Item 3: The gravitational potential energy term contains a modification to the height h, similar to mg(h + L - L_0), and shouldn't be just mgh or mgL
"""

Question_3['Rubric'] = """
# Item 1: The student solution decomposed the initial linear momentum of boulder 2 into its x and y components. 

# Item 2: The student wrote down conservation of linear momentum equation for both the x and y directions independently.

# Item 3: The student used Pythagorean theorem to find the magnitude of the final velocity.
"""

Q_Info = {
    'Q1': Question_1,
    'Q2': Question_2,
    'Q3': Question_3
}