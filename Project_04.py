"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Project #4
    Created on Tuesday Feb 27 20:00 2024  
    Last Updated Wednesday Feb 29 00:44

    Description: 
        The program uses list comprehenion to create a list of random numbers for various predefined problem sizes.
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




#----project imports section




import time, random
import matplotlib.pyplot as plt




#----function definitions section




def mySortFunc( someList ):
    
    """
    
    Description
    ----------
    The insertionSort() function inserts candidate to the left
    in ascending order. By the time we are at the last index, 
    all previous items are in order, and the final index can be
    placed anywhere that it belongs in the list, starting at the end,
    and walking down, we find where it belongs and insert it.
    
    Parameters
    ----------
        someList : 
            List of integers
            This is a list of random numbers for any problem size.

    Returns
    -------
    None.

    """
    
    for i in range( 1, len( someList ) ):
        
        # candidate will be the item we will be inserting where it belongs to its left
        candidate = someList[ i ]
        
        # the final j is where candidate will be inserted
        j = i - 1
        
        while ( j >= 0 and someList[ j ] > candidate ):
            
            # we have double values until we insert, at which point we replace the first of the two
            someList[ j + 1 ] = someList[ j ]
            
            j = j - 1
            
        someList[ j + 1 ] = candidate
        
        # do this for each index 

# end insertion sort func


def checkSort( someList ):
    
    """
    
    Description
    ----------
    checkSort() loop can ends by returning true or false, depending on item order of the passed-in list
   
    Parameters
    ----------
        someList : 
            List of random integers
            The List of random numbers we will be sorting
    
    Returns
    -------
        bool
            True if the list is in ascending order, False if not.

    """
    
    print( "Is the List sorted?" )
    
    for i in range( len( someList ) ): 
        
        # make sure we are'nt checking 0 or check fails every time
        if i > 0:
            
            if someList[ i - 1 ] > someList[ i ]:
            # search for values that are out of order, if found, list not in order
                return False
            
            if i == len( someList ) - 1:
            # We've reached the end of list, all previous numbers in order 
                return True
            
# end of checkSort() function


def getTimes( someProblemSizes ) :
    
    """
    
    Description
    ----------    
    getTimes() creates a List of random numbers for each of the problem sizes containing 
    the coresponding problem size. Each problem is then sorted while being timed. A list is created 
    of the time taken for each size. When all sorting is completed, the timeList is returned,
    and used for plotting.
    
    Parameters
    ----------
        someProblemSizes : 
            List of integers
            A value for each of problem sizes.
        
    Returns
    -------
        timeList : 
            List of floats
            The times that we will be plotting on the y-axis

    """
    
    timeList = [ ]
    
    for i in range( len( someProblemSizes ) ):
        
        # define initial seed value
        random.seed( 22, int )
        
        # create list of random numbers
        L = [ random.randint(0, 999) for t in range( someProblemSizes[ i ]) ]
        
        # start timer
        start = time.monotonic()
        
        # sort
        mySortFunc( L )
        
        # end timer when sorting is complete
        end = time.monotonic()
        
        # measure & store time
        elapsedTime = end - start
        
        # y value of plot
        timeList.append( elapsedTime )
        
        print( elapsedTime )
        print( checkSort( L ) )
        
    # return the list to plot
    return timeList

# end getTimes() func


def createPlot( xData, yData ):
    
    """
    
    Description
    ----------  
    createPloat() uses mathPlot to create a chart representing the time taken to sort our given problem sizes.

    Parameters
    ----------
        
        xData : 
            List of integers
            Our problem sizes
            
        yData : 
            List of floats
            Our y-axis values for plotting

    Returns
    -------
    None.

    """
    
    # string values for x ticks
    Ns = [ str( t ) for t in xData ]
    plt.title( "Insertion Sorting - Various List Sizes" )
    plt.xlabel( 'Amount of Random Numbers in List' )
    plt.ylabel( 'Time Elapsed' )
    plt.xscale( "log" )
    plt.xticks( xData, Ns )
    plt.scatter( xData, yData )
    plt.plot( xData, yData )
    plt.savefig( "Scott Quashen_Project_4.png", dpi=600 )
    plt.show()

# end createPlot() func




#--------------------------main code section

# dev name
print( "Scott Quashen..." + time.asctime() )

# define the problem sizes
problemSizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

# create lists, sort them, measure elapsed time, and return our lists of data for use in plotting
t = getTimes( problemSizes )

# handle the plotting of previously gathered data
createPlot( problemSizes, t )




#------end 
















