"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Project #4
    Created on Tuesday Feb 27 20:00 2024  
    Last Updated Wednesday Feb 29 00:54

    Description: 
        The program uses list comprehension to create a list of random numbers for various predefined problem sizes.
        The program then sorts each list in order using a custom insertion sort function, 
        measures the time taken for each list to be sorted, 
        then plots the results.
        
    
    Inputs: 
        mySortFunc( someList )
        ( List )
        
        checkSort( someList )
        ( List )

        getTimes( someProblemSizes )
        ( List )

        createPlot( xData, yData )
        ( List, List )
    
    
    Returns: 
        The check sort function returns a boolean
        ( did sort function work? )
        
        The get times function returns: timeList 
        ( our y-axis data for plotting )
        

    Dependencies: random, time, mathhplotlib.pyplot

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""

