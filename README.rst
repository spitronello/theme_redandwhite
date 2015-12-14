.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Red and white theme.
===========================

This Module installs a red (#ff1919) and white bootstrap theme, it modifies
default header and footer and defines the "card snippet".

Configuration
=============

Dependencies:
-------------
The module website_less needs to be installed for this theme to work properly.
If this is the first theme you install, follow these steps to enable theme
layer dependencies:

- sudo apt-get install -y npm
- sudo ln -s /usr/bin/nodejs /usr/bin/node
- sudo npm install -g less less-plugin-clean-css

The website_less module can be found here:

- https://www.odoo.com/apps/8.0/website_less/

There is no public repo for that module, AFAIK, if you find it, please give us
a hint.

After installing dependencies, install theme_redandwhite as you would with any
other odoo module and that's it.

Customization
-------------
-Social media button links are hardcoded in redandwhite_header and
redandwhite_footer files, edit the img tags so they point to your desired URLs.

-The theme was created from a custom design and its aim is following blueprints
instead of making it fully customizable. If you come up with any ideas to make
this theme more attractive for general use, please share them, we will really
appreciate your feedback.

Known issues
============

Thi is a work in progress, if you find any issues, please refer to next point.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/bisnesmart/theme_redandwhite>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us solving it by providing a detailed and welcomed feedback
`here <https://github.com/bisnesmart/theme_redandwhite/issues>`_.

Credits
=======

Contributors
------------
- bisneSmart.


Maintainer
----------

- bisneSmart.
