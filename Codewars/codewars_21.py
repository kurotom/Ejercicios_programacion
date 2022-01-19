# -*- coding: utf-8 -*-
"""
You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.

"""

regex = (
    '^'                # start line
    '(?=.*\d)'         # must contain one digit from 0-9
    '(?=.*[a-z])'      # must contain one lowercase characters
    '(?=.*[A-Z])'      # must contain one uppercase characters
    '([0-9a-zA-Z]+)'   # permitted characters (alphanumeric only)
    '{6}'              # length at least 6 chars
    '$'                # end line
)

regex('fjd3IR9')      # True
#regex('ghdfj32')      # False
#regex('DSJKHD23')     # False
#regex('dsF43')        # False
#regex('4fdg5Fj3')     # True
