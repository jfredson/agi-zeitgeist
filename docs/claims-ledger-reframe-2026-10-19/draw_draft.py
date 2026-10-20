import json,sys,tomllib,glob
sys.path.insert(0,'scripts')
from chart_style import figure,titles,SURFACE,INK,INK_2,GRID,PALETTE
import matplotlib.pyplot as plt
S=sys.argv[1]; OUT=sys.argv[2]
rows=json.load(open(S+'/agi.json'))
DROP={'2010-12-10-legg-human-level-agi-90-percent-by-2045','2019-01-05-altman','2025-01-amodei','2026-02-13-amodei-ninety','2011-06-17-legg'}
def drop(r):
    i=r['id']
    if i.startswith('2019-01-05-altman') or i.startswith('2011-06-17-legg'): return True
    if i=='2010-12-10-legg-human-level-agi-90-percent-by-2045': return True
    if r['year']>=2100: return True
    if r['who']=='amodei' and r['when']=='2026-02-13' and r['year']==2036: return True
    if r['who']=='lecun' and r['when']=='2024-10' : return True
    if r['who']=='kaifulee' and r['year']==2038: return True
    return False
rows=[r for r in rows if not drop(r)]
# Sutskever's 2025 forecast is worded without the keywords; add it from its file.
for f in glob.glob('data/claims/2025-11-25-sutskever*.toml'):
    c=tomllib.load(open(f,'rb'))['claim']
    if c['kind']=='timing': rows.append(dict(id=c['id'],who='sutskever',when=c['when'],year=c['due'],early=c.get('due_early'),prob=False,notbefore=False,pred=c['prediction']))
NAMES={'altman':'Sam Altman','musk':'Elon Musk','amodei':'Dario Amodei','hassabis':'Demis Hassabis','legg':'Shane Legg','suleyman':'Mustafa Suleyman','sutskever':'Ilya Sutskever','lecun':'Yann LeCun','liangwenfeng':'Liang Wenfeng','kaifulee':'Kai-Fu Lee','pichai':'Sundar Pichai'}
def x(w):
    p=w.split('-'); return int(p[0])+(int(p[1])-1)/12 if len(p)>1 else int(p[0])+.5
json.dump(rows,open(S+'/kept.json','w'),indent=1)
# 1. What they say now: each person's latest named year (or range).
latest={}
for r in sorted(rows,key=lambda r:r['when']):
    latest[r['who']]=r
# when several claims share the latest date, prefer the one without "not before" and the earliest year
for who in latest:
    d=latest[who]['when']; same=[r for r in rows if r['who']==who and r['when']==d]
    latest[who]=sorted(same,key=lambda r:(r['notbefore'],r['year']))[0]
order=sorted(latest.values(),key=lambda r:((r['early'] or r['year'])+r['year'])/2)
fig,ax=figure(10,5.6); fig.subplots_adjust(left=0.27,right=0.97,top=0.78,bottom=0.14)
for i,r in enumerate(order):
    lo=r['early'] or r['year']; hi=r['year']
    col=PALETTE[0]
    if r['notbefore']:
        ax.annotate('',(hi+3,i),(hi,i),arrowprops=dict(arrowstyle='-|>',color=PALETTE[1],lw=2))
        ax.plot([hi],[i],'|',ms=12,mew=2.5,color=PALETTE[1])
    elif lo!=hi:
        ax.plot([lo,hi],[i,i],'-',lw=6,color=col,solid_capstyle='round',alpha=.85)
    else:
        ax.plot([hi],[i],'o',ms=9,color=col)
ax.set_yticks(range(len(order))); ax.set_yticklabels([f"{NAMES[r['who']]}, said {r['when']}" for r in order],fontsize=8.5,color=INK)
ax.invert_yaxis(); ax.set_xlim(2025,2046); ax.set_xticks(range(2026,2047,4)); ax.grid(axis='x',color=GRID,lw=.8); ax.set_axisbelow(True)
ax.axvline(2026.8,color=INK_2,lw=.8,ls=':'); ax.text(2026.9,-0.9,'today',fontsize=7.5,color=INK_2)
titles(fig,"What they say now: eight of the eleven who name a year put it by 2031",
 "Each person's most recent dated forecast of AGI, superintelligence or AI better than people at most things, in their own terms.\nA bar is a range they gave; a dot is a single year; an orange arrow is a forecast that it will not come before that year.",
 "DRAFT for John's ruling, 2026-10-19: claims picked by keyword for this picture only.\nFour of the fifteen (Huang, Mensch, Zuckerberg, Nadella) have named no year. Source: agizeitgeist.com/data")
fig.savefig(OUT+'/claims-reframe-now-draft.png',facecolor=SURFACE); plt.close(fig)
# 2. How it has moved: one small panel per person.
people=sorted({r['who'] for r in rows},key=lambda w:-max(x(r['when']) for r in rows if r['who']==w))
people=sorted(people,key=lambda w:min(x(r['when']) for r in rows if r['who']==w)>2020)
fig,axs=figure(11,8.2,nrows=3,ncols=4,sharex=True,sharey=True)
fig.subplots_adjust(left=0.07,right=0.98,top=0.84,bottom=0.08,hspace=.38,wspace=.12)
for a,who in zip(axs.flat,people):
    rs=[r for r in rows if r['who']==who]
    a.plot([2023,2036],[2023,2036],color=GRID,lw=1)
    for r in rs:
        xx=x(r['when'])
        if r['notbefore']:
            a.plot([xx],[r['year']],'^',ms=6,color=PALETTE[1])
        else:
            if r['early']: a.plot([xx,xx],[r['early'],r['year']],'-',lw=3,color=PALETTE[0],alpha=.6)
            a.plot([xx],[r['year'] if not r['early'] else (r['early']+r['year'])/2],'o',ms=4.5,color=PALETTE[0])
    a.set_title(NAMES[who],fontsize=9.5,color=INK,loc='left')
    a.grid(axis='y',color=GRID,lw=.6); a.set_axisbelow(True)
for a in list(axs.flat)[len(people):]: a.set_visible(False)
a=axs.flat[0]; a.set_xlim(2022.5,2027); a.set_ylim(2024,2041); a.set_xticks([2023,2025,2027]); a.set_yticks([2025,2030,2035,2040])
titles(fig,"How it has moved: the dates they give, by when they said them (2023 onward)",
 "Each mark is one dated forecast of AGI, superintelligence or AI better than people at most things, placed at the day it was said and the year it named.\nBlue: the year or range they gave. Orange triangle: a forecast that it will not come before that year. The grey line is 'this year'.",
 "DRAFT for John's ruling, 2026-10-19: claims picked by keyword for this picture only; earlier forecasts (Legg 2010, Hassabis 2011) are left off to keep the scale. Source: agizeitgeist.com/data")
fig.savefig(OUT+'/claims-reframe-moved-draft.png',facecolor=SURFACE); plt.close(fig)
for r in order: print(r['who'],r['when'],r['early'],r['year'],r['notbefore'])
