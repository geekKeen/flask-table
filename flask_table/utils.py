# -*- coding: utf8 -*-
import re

_camelcase_re = re.compile(r'([A-Z]+)(?=[a-z0-9])')


def camel_to_snake_case(name):
    def _join(match):
        word = match.group()

        if len(word) > 1:
            return ('_%s_%s' % (word[:-1], word[-1])).lower()

        return '_' + word.lower()

    return _camelcase_re.sub(_join, name).lstrip('_')


if __name__ == "__main__":
    name = "HTMLparser"
    print camel_to_snake_case(name)  # html_parser
