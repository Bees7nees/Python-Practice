'''
As per the freeCodeCamp.org course on Python:

I will be using numerical methods to approximate solutions to mathematical problems that
are difficult or impossible to solve analytically.

In this project, I will explore the numerical method of bisection to find the square root
of a number by iteratively narrowing down the possible range of values that contain
the square root.
'''

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calculates the square root of a given number using the bisection method.

    Parameters:
    square_target (number): The number to find the square root of.
    tolerance (float): The maximum difference between the current guess and the actual square root.
                       Default is 1e-7.
    max_iterations (int): The maximum number of iterations to perform. Default is 100.

    Returns:
    The calculated square root of the given number.

    Raises:
    ValueError: If the given number is negative.
    """
    # Check if the target number is negative
    if square_target < 0:
        # Raise an error for negative square targets
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Handle special case where the target number is 1
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')

    # Handle special case where the target number is 0
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize the lower and upper bounds for the bisection method
        low = 0
        high = max(1, square_target)

        root = None  # Variable to store the calculated square root

        # Perform the bisection method for a maximum of max_iterations
        for _ in range(max_iterations):
            # Calculate the midpoint
            mid = (low + high) / 2
            square_mid = mid**2  # Square the midpoint e.g. mid = 2, square_mid = 2^2 = 4

            # Check if the squared midpoint is within the tolerance
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            # Adjust the bounds based on the squared midpoint
            elif square_mid < square_target:
                # e.g. If square_target = 16 and square_mid = 4, then mid = 2 is too low
                low = mid
            else:
                # e.g. If square_target = 16 and square_mid = 25, then mid = 5 is too high
                high = mid

        # If root is not found, raise an error
        if root is None:
            raise ValueError(f'Failed to find square root of {square_target} within {max_iterations} iterations')
        else:
            # Output the calculated square root
            print(f'The square root of {square_target} is {root}')

    return root

N = 16
square_root_bisection(N)
