import os.path
import glob
import markdown2
import jinja2

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def f(name: str) -> str:
    return os.path.join(BASE_DIR, name)


with open(f('index.template.html'), 'r') as template_source, \
        open(f('index.html'), 'w') as output:
    template = jinja2.Template(template_source.read())
    output.write(template.render(version='1.0.0'))

with open(f('releases.template.html'), 'r') as template_source, \
        open(f('releases.html'), 'w') as output:
    release_files = glob.glob(os.path.join(BASE_DIR, 'releases', '*.md'))
    releases = []
    for release_file in release_files:
        file_name = os.path.splitext(os.path.basename(release_file))[0]
        releases.append({
            'version': file_name,
            'content': markdown2.markdown(open(release_file).read()),
        })
    # releases = [os.path.splitext(os.path.basename(fname))[0] for fname in release_files]
    template = jinja2.Template(template_source.read())
    output.write(template.render(releases=releases))
