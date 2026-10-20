import re,sys
import os
S=os.path.dirname(__file__)+'/'
cream,ember=open(S+'wortmarke-pfade.txt').read().split('\n')[:2]
pts=[tuple(map(int,p.split(','))) for p in re.findall(r'-?\d+,-?\d+',cream+ember)]
xs=[p[0] for p in pts];ys=[p[1] for p in pts];pad=6
vb=f'{min(xs)-pad} {min(ys)-pad} {max(xs)-min(xs)+2*pad} {max(ys)-min(ys)+2*pad}';print('viewBox',vb)
mark='M251,118 L116,338 L92,382 L160,350 L184,336 L250,225 L325,352 L270,356 L425,409Z'
t=open('src/index.template.html').read()
t=t.replace('viewBox="70 150 1614 180"',f'viewBox="{vb}"').replace('{{MARK}}',mark).replace('{{WORD_CREAM}}',cream).replace('{{WORD_EMBER}}',ember)
open('index.html','w').write(t)
