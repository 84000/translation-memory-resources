#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
import re
import json


# Re-insert metadata from pre_output/tmp file into XML as tags.
def insert_metatags(text, meta_data):
    lines = text.split('\n')
    for num, s in enumerate(lines):
        if '$' in s:
            new = ''
            for chunk in re.split(r'(\$\d+\s*)', lines[num]):
                if '$' in chunk:
                    g_id = re.findall(r'\$\d+', lines[num])
                    new += '<milestone xml:id="'
                    new += meta_data["milestones"][g_id[0]]
                    new += '"/>'
                else:
                    new += chunk
            lines[num] = new
        if '#' in s:
            new = ''
            for chunk in re.split(r'(#\d+)', lines[num]):
                if chunk.startswith('#'):
                    index = chunk.strip("#")
                    g_id = re.findall(r'#\d+', lines[num])
                    new += '<note index="'
                    new += index
                    new += '" xml:id="'
                    new += meta_data["notes"][g_id[0]]
                    new += '"/>'
                else:
                    new += chunk
            lines[num] = new
    lines = '\n'.join(lines)
    return lines


# Convert flags made by TM editors for alternative sources and dubious
# translations into XML tags.
def create_flags_bo(text):
    lines = text.split('\n')
    for num, s in enumerate(lines):
        if re.search(r'>\s*!', s):
            lines[num] = re.sub(r'>\s*!\s*', ' flag="alternateSource">', lines[num])
    lines = '\n'.join(lines)
    return lines


def create_flags_en(text):
    lines = text.split('\n')
    for num, s in enumerate(lines):
        if re.search(r'>\s*%', s):
            lines[num] = re.sub(r'>\s*%\s*', ' flag="dubiousTranslation">', lines[num])
    lines = '\n'.join(lines)
    return lines


# Normalize Tibetan; remove spaces created by pybo and reformat folio refs into
# XML tags
def normalize_tibetan(text):
    segments = re.split(r'(>.*?<)', text)
    for num, s in enumerate(segments):
        if re.search('་', s):  # Find Tibetan strings according to Tsegs
            s2 = re.sub(r'\[(\d+)\.?([ab])]\s?', r'<ref folio="F.\1.\2"/>', s)
            s3 = re.sub(r' (?![a-z])', '', s2)
            segments[num] = re.sub('_', ' ', s3)
    segments = ''.join(segments)
    return segments


# This is the primary function in the script to process all XML files exported
# from InterText in directory "post_input" and write to "post_output"
def postprocess(in_dir, out_dir):
    # get path for XML in post_input
    for file in in_dir.glob('*.xml'):
        if file.is_file():
            if 'bo.en' in file.name:
                # copy over alignment XML file
                copy = file.read_text(encoding='utf-8-sig')
                to_file = out_dir / file.name
                to_file.write_text(copy, encoding='utf-8-sig')

            if '.bo' in file.name and '.en' not in file.name:
                # process source XML file
                text = file.read_text(encoding='utf-8-sig')
                text = create_flags_bo(text)
                text = normalize_tibetan(text)
                to_file = out_dir / file.name
                to_file.write_text(text, encoding='utf-8-sig')

            if 'en' in file.name and '.bo' not in file.name:
                # process translation XML file
                # get filestem to access .json file from 'output/tmp' folder
                file_stem = str(file.name).rstrip('.en.xml')
                # note, rstrip removes any characters in argument string, but this
                # works for 84000 project because all input files end with a number.
                json_file = in_dir.parent / 'pre_output' / 'tmp' / (file_stem + '-bo.json')
                if not json_file.is_file():
                    exit(f'{json_file} is missing.\nExiting')
                read_meta_data = json_file.read_text(encoding='utf-8-sig')
                meta_data = json.loads(read_meta_data)
                text = file.read_text(encoding='utf-8-sig')
                text = insert_metatags(text, meta_data)
                text = create_flags_en(text)
                to_file = out_dir / file.name
                to_file.write_text(text, encoding='utf-8-sig')


if __name__ == '__main__':
    in_dir = Path('post_input')
    in_dir.mkdir(exist_ok=True)

    out_dir = Path('post_output')
    out_dir.mkdir(exist_ok=True, parents=True)
    # empty post_output folder at each run
    for o in out_dir.parent.glob('*.xml'):
        o.unlink()
    for o in out_dir.glob('*.xml'):
        o.unlink()

    postprocess(in_dir, out_dir)
