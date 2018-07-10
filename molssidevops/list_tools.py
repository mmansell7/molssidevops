def mean(num_list):
    """
    Calculates the mean of a list of numbers

    Parameters
    ----------
    num_list: list (int or float)


    Returns
    -------
    ret: int or float
        The mean of the list


    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    try:
        return sum(num_list) / len(num_list)
    except TypeError as err:
        msg = 'Input must be a list of int or float'
        raise TypeError(err.__str__() + '\n' + msg)
    except ZeroDivisionError as err:
        raise ZeroDivisionError(err)
