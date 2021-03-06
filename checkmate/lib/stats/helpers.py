# -*- coding: utf-8 -*-
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

from __future__ import unicode_literals

def directory_splitter(path,include_filename = False):
    if include_filename:
        path_hierarchy = path.split("/")
    else:
        path_hierarchy = path.split("/")[:-1]
    if path.startswith('/'):
        path_hierarchy = path_hierarchy[1:]
    paths = []
    current_path = ''
    for partial_path in path_hierarchy:
        paths.append(current_path)
        if current_path != '':
            current_path+='/'
        current_path+=partial_path
    paths.append(current_path)
    return paths
