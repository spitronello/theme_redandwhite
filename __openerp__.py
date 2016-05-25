# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Red and white theme",
    "version": "0.1",
    "author": "BisneSmart Team,"
              "BisneSmart",
    "contributors": [
        "Gonzalo Borras <gborras@bisnesmart.com>",
        "Ruben Cabrera <rcabrera@bisnesmart.com>",
        "Equipo Odoo <odoo@bisnesmart.com>",
    ],
    "website": "http://www.bisnesmart.com",
    "depends": [
        "website",
        'website_less',
    ],
  'data': [
    'views/assets.xml',
    #'views/external_layout/redandwhite_header.xml',
    'views/snippets.xml',
  ],
  'category': 'Theme/Creative',

    "installable": True,
    "application": True,
}
