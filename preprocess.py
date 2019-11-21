#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
import re
import json

from botok import Text


def plaintext_sent_par(units):
    out = []
    for u in units:
        unit = " ".join([word.text.replace(' ', '_') for word in u[1]])
        unit = unit.replace('_[', ' [').replace(']_', '] ')
        # cleanup extra spaces
        unit = re.sub(r'([^།])\s*_\s*([^།])', r'\1 \2', unit)
        unit = unit.replace('།_།_', '།_།')
        out.append(unit)
    return out


def prepare_source(dump):
    dump = re.sub(r'\[[0-9]+[ab]\.[0-9]\]', '', dump)
    dump = re.sub(r'{.*?}', '', dump)
    # segment in sentences
    text = Text(dump)
    config = {"profile": "GMD"}
    sentences = text.custom_pipeline(
        "basic_cleanup",
        "sentence_tok",
        "dummy",
        plaintext_sent_par,
        tok_params=config,
    )
    return '\n'.join(sentences)


def prepare_target(dump):
    # temporarily remove line returns
    # because it would confuse hunalign to have sentences split over multiple lines(verses)
    dump = dump.replace('\n', ' ')
    dump = re.sub(r'\s+', ' ', dump)
    # split in sentences using periods and excl. marks
    dump = dump.replace('. ', '.\n')
    dump = dump.replace('! ', '!\n')
    sentences = dump.split('\n')
    milestones = {}
    notes = {}
    mstone = 1
    for num, s in enumerate(sentences):
        if '<milestone' in s:
            new = ''
            for chunk in re.split(r'(<milestone [0-9a-zA-Z\-]+>)', sentences[num]):
                if '<milestone' in chunk:
                    m_id = re.findall(r'<milestone ([0-9a-zA-Z\-]+)>', sentences[num])
                    id = f'${mstone}'
                    milestones[id] = m_id[0]
                    mstone += 1
                    new += id
                else:
                    new += chunk
            sentences[num] = new

        if '<ref' in s:
            sentences[num] = re.sub(r'<ref [A-Za-z]\.([0-9]+\.[ab])>', r'[\1]', sentences[num])

        if '<note' in s:
            new = ''
            for chunk in re.split(r'(<note #[0-9]+ [0-9a-zA-Z\-]+>)', sentences[num]):
                if '<note' in chunk:
                    n = re.findall(r'<note (#[0-9]+) ([0-9a-zA-Z\-]+)>', sentences[num])
                    n_ref, n_id = n[0]
                    notes[n_ref] = n_id
                    new += n_ref
                else:
                    new += chunk

            sentences[num] = new
    sentences = ' '.join(sentences)
    return sentences, {'notes': notes, 'milestones': milestones}


def preprocess(in_dir, out_dir):
    # get source/target paths
    pairs = [(d, d.parent / d.name.replace('bo', 'en')) for d in in_dir.glob('*bo.txt')]
    if not pairs:
        exit('Nothing to process.\nExiting')
    for source, target in pairs:
        if not source.is_file():
            exit(f'{source} is missing.\nExiting')
        if not target.is_file():
            exit(f'{target} is missing.\nExiting')

        # process source
        s_sents = prepare_source(source.read_text(encoding='utf-8-sig'))
        s = out_dir.parent / source.name
        s.write_text(s_sents, encoding='utf-8-sig')

        # process target
        sents, metadata = prepare_target(target.read_text(encoding='utf-8-sig'))
        s = out_dir.parent / target.name
        s.write_text(sents, encoding='utf-8-sig')

        m = out_dir / (source.stem + '.json')
        m.write_text(json.dumps(metadata), encoding='utf-8-sig')


if __name__ == '__main__':
    in_dir = Path('pre_input')
    in_dir.mkdir(exist_ok=True)

    out_dir = Path('pre_output/tmp')
    out_dir.mkdir(exist_ok=True, parents=True)
    # empty pre_output folder at each run
    for o in out_dir.parent.glob('*.txt'):
        o.unlink()
    for o in out_dir.glob('*.txt'):
        o.unlink()

    preprocess(in_dir, out_dir)
