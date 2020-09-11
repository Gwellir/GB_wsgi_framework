from jinja2 import Template
import os


def render(template_name, folder='mysite/templates', **kwargs):
    templ_file = os.path.join(folder, template_name)
    with open(templ_file, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
