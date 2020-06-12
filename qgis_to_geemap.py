"""This script is used to convert Earth Engine QGIS examples to geemap.
"""

import os
import geemap
from pathlib import Path


def conversion(in_file, out_file):
    in_file = os.path.abspath(in_file)
    out_file = os.path.abspath(out_file)
    out_dir = os.path.dirname(out_file)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_lines = []
    with open(in_file) as f:
        in_lines = f.readlines()

        for line in in_lines:
            if line.strip().startswith('# GitHub URL'):
                pass
            elif line.strip() != 'from ee_plugin import Map':
                out_lines.append(line)
            else:
                out_lines.append('import geemap\n')
                out_lines.append('\n# Create a map centered at (lat, lon).\n')
                out_lines.append(
                    'Map = geemap.Map(center=[40, -100], zoom=4)\n')
    out_lines.append('\n# Display the map.')
    out_lines.append('\nMap\n')

    with open(out_file, 'w') as f:
        f.writelines(out_lines)


def conversion_dir(in_dir, out_dir):

    in_dir = os.path.abspath(in_dir)
    out_dir = os.path.abspath(out_dir)

    in_files = list(Path(in_dir).rglob('*.py'))

    for index, in_file in enumerate(in_files):
        in_file = str(in_file)
        if in_file.endswith('qgis_basemaps.py') or in_file.endswith('convert_js_to_python.py'):
            continue

        print('Processing {}/{}: {}...'.format(index + 1, len(in_files), in_file))
        out_file = in_file.replace(in_dir, out_dir)
        parent_dir = os.path.dirname(out_file)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        conversion(in_file, out_file)


out_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

qgis_repo_url = 'https://github.com/giswqs/qgis-earthengine-examples'
qgis_repo_name = os.path.basename(qgis_repo_url)
qgis_repo_dir = os.path.join(out_dir, qgis_repo_name)

if not os.path.exists(qgis_repo_dir):
    geemap.clone_github_repo(
        qgis_repo_url, os.path.join(out_dir, qgis_repo_dir))

conversion_dir(qgis_repo_dir, os.getcwd())
