

def convert_from_term_code(term_code) -> str:
    """
    >>> convert_from_term_code(2202)
    'Winter 2020'
    >>> convert_from_term_code(2204)
    'Spring 2020'
    """
    term_name = ""
    if (str(term_code).endswith('2')):
        term_name = "Winter"
    elif (str(term_code).endswith('4')):
        term_name = "Spring"
    else:
        # Not a valid term_code
        assert(False)
        return

    year_mil = ""
    if (str(term_code).startswith('2')):
        year_mil = "20"

    return term_name + ' ' + year_mil + str(term_code)[1:-1]
