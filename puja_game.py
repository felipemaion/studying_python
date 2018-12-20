# Ritik - the day dreamer (100 Marks)
#
# Ritik is a man of dreams, he keeps dreaming day and night, wondering about space and time, sci-fi and a lot more. Today is yet another day when he dreamed about a Galactic Grid where he was supposed to rescue his friend Kriti. Now this Grid is slightly unusual consisting of two species Vilgax and Arkaknight.
#
#
# Vilgax is bad and can freeze you for some time whereas Arkaknight is good and lets you jump from one place to another.
#
#
# The Grid is made up of m rows and n columns. Each cell consists of an integer either positive, negative or zero.There are exactly two zeroes one at top-left corner and the other at bottom-right corner of the grid representing initial positions of Ritik and Kriti respectively.
#
#
# A positive integer represents an Arkaknight. It gives you the power to jump from cell to another containing the same integer anywhere within the grid. For example - a cell containing 2 can let you jump to any other cell containing 2 in the grid if there is one.
#
#
# A negative integer represents a Vilgax. It freezes for a certain period of time that is you cannot move for certain units of time represented by the absolute value of the integer present in that cell.For example , a cell containing -3 makes you freeze for 3 units of time in that cell i.e you cannot move or jump to any other cell.
#
#
# Ritik can also move to any cell that share a common wall i.e adjacent to each other ( top, left, right and bottom ) within the grid. It takes one unit of time to jump from one cell to another.
#
# Your task is to tell the minimum units of time taken by Ritik to reach Kriti given the grid of m x n.
#
# Input Format
#
# First line of input contains number of rows  - M.
#
# Second line of input contains number of columns  - N.
#
# Then M lines of input follows each containing N integers respectively.
#
# Note : The Positive integers will range from [ 1, M * N ] both inclusive and negative integers can range from [-1 , -( M * N ) ] both inclusive.
#
# Constraints
#
# 1 <= M <= 1000
#
# 1 <= N <= 1000
#
# Output Format
#
# Print the minimum units of time taken by Ritik to reach Kriti.
#
# Sample TestCase 1
#
# Input
#
# 3
# 3
# 0 2 3 -
# 1 2 -3
# 3 2 0
# Output
# 3