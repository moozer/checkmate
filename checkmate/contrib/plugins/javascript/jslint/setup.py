"""
This file is part of checkmate, a meta code checker written in Python.

Copyright (C) 2015 Andreas Dewes, QuantifiedCode UG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from .analyzer import JSLintAnalyzer
from .issues_data import issues_data

analyzers = {
    'jslint' :
        {
            'title' : 'JSLint',
            'class' : JSLintAnalyzer,
            'language' : 'javascript',
            'issues_data' : issues_data,
        },
}