"""Build current static masters from editable UFO sources, without legacy archives.

Usage: python tools/build.py --sources sources --output fonts/ttf
The same script lives at font-engineering/src/build_from_ufo.py in the engineering workspace.
"""
import argparse, json, os
from pathlib import Path
from fontmake.font_project import FontProject
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables.ttProgram import Program


def build(sources, output, epoch=1793376000, web_output=None):
    os.environ['SOURCE_DATE_EPOCH']=str(epoch)
    sources=Path(sources);output=Path(output);output.mkdir(parents=True,exist_ok=True)
    web_output=Path(web_output) if web_output else output
    web_output.mkdir(parents=True,exist_ok=True)
    ufos=sorted(sources.glob('ShalymenovBlock-*.ufo'))
    if len(ufos)!=4:raise ValueError('Exactly four current static UFO masters are required')
    FontProject().run_from_ufos([str(p) for p in ufos],output=['ttf'],output_dir=str(output),
        remove_overlaps=False,use_production_names=False,autohint=False,feature_writers=[])
    for source in ufos:
        path=output/(source.stem+'.ttf')
        with TTFont(path,recalcTimestamp=False) as f:
            f['prep']=newTable('prep');f['prep'].program=Program()
            f['prep'].program.fromBytecode(b'\xb8\x01\xff\x85\xb0\x04\x8d')
            f['gasp']=newTable('gasp');f['gasp'].version=1;f['gasp'].gaspRange={65535:15}
            f['maxp'].maxStackElements=max(f['maxp'].maxStackElements,1)
            f['head'].created=f['head'].modified=epoch+2082844800
            f['name'].names=[n for n in f['name'].names if n.platformID==3]
            style=source.stem.split('-')[-1];version=f'{f["head"].fontRevision:.3f}'
            for nid,value in {3:version+';SHAL;'+source.stem,5:'Version '+version,
                             10:'A compact, angular display family with Latin and Cyrillic support.'}.items():
                f['name'].setName(value,nid,3,1,0x409)
            if style in ('Regular','Bold'):
                f['name'].names=[n for n in f['name'].names if n.nameID not in (16,17)]
            f['meta']=newTable('meta');f['meta'].data={'dlng':'Latn, Cyrl','slng':'Latn, Cyrl'}
            f['OS/2'].recalcAvgCharWidth(f);f['OS/2'].recalcUnicodeRanges(f);f['OS/2'].recalcCodePageRanges(f)
            f.save(path);f.flavor='woff2';f.save(web_output/path.with_suffix('.woff2').name)
    return [str(output/(p.stem+'.ttf')) for p in ufos]


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sources',default='font-engineering/sources');p.add_argument('--output',default='font-engineering/.staging/fontmake-audit')
    p.add_argument('--web-output',help='Separate WOFF2 directory; defaults to the TTF directory')
    a=p.parse_args();print(json.dumps(build(a.sources,a.output,web_output=a.web_output),indent=2))
