import datetime
import os.path
import glob
import markdown2
import jinja2

from typing import List

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def f(name: str) -> str:
    return os.path.join(BASE_DIR, name)


def release_files() -> List[str]:
    return sorted(glob.glob(os.path.join(BASE_DIR, 'releases', '*.md')), reverse=True)


def current_release(releases: List[str]) -> str:
    names = [release_name(release) for release in releases]
    released = [release for release in names if 'release' in release]
    return released[0] if len(released) > 0 else names[-1]


def release_name(release: str) -> str:
    return os.path.splitext(os.path.basename(release))[0]


def release_version(release: str) -> str:
    return release[:5]


with open(f('index.template.html'), 'r') as template_source, \
        open(f('index.html'), 'w') as output:
    template = jinja2.Template(template_source.read())
    version = release_version(current_release(release_files()))
    output.write(template.render(version=version))

with open(f('releases.template.html'), 'r') as template_source, \
        open(f(os.path.join('releases', 'planned', 'planned.md')), 'r') as planned, \
        open(f('releases.html'), 'w') as output:
    releases = []
    for release_file in release_files():
        name = release_name(release_file)
        location = name[6:]
        releases.append({
            'version': release_version(name),
            'location': location,
            'content': markdown2.markdown(open(release_file).read()),
        })
    # releases = [os.path.splitext(os.path.basename(fname))[0] for fname in release_files]
    template = jinja2.Template(template_source.read())
    output.write(template.render(releases=releases,
                                 planned=markdown2.markdown(planned.read()),
                                 now=datetime.datetime.utcnow()))
