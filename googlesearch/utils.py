

"""
A hook for our JSON decoding parser
"""


def decode_hook(parsed_dict):

    class Object(object):

        def __init__(self, parsed_dict):
            self.__dict__.update(**parsed_dict)

    return Object(parsed_dict)
