import jinja2
import os.path


def f(name: str) -> str:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_dir, name)


with open(f('index.template.html'), 'r') as template_source, \
        open(f('index.html'), 'w') as index:
    template = jinja2.Template(template_source.read())
    index.write(template.render(version='1.0.0'))
