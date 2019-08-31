
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 

@author: sam
"""

from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('.'))
template = env.get_template("my_html_template.html")

template_vars = template_vars = {"today_date": "8/31/2019",
                 "needed_table": ci_df.to_html()}

html_out = template.render(template_vars)

with open("cisheet_exp.html", "w") as file:
    file.write(html_out)