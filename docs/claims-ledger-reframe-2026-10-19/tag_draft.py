import tomllib,glob,re,json,sys
KEY=re.compile(r"AGI|general intelligence|human-level|human level|superintelligence|smarter than|better than humans|country of geniuses|powerful AI|surpass|as smart as|humanlike|Nobel|90% of|overwhelms|PhD level|better than almost all|smarter than any",re.I)
NOT=re.compile(r"\bwill not\b|\bnot before\b|\bnot in 20|\bnot within\b|\bnot come\b|certainly not",re.I)
out=[]
for f in sorted(glob.glob('data/claims/*.toml')):
    c=tomllib.load(open(f,'rb'))['claim']
    if c['kind']!='timing' or not KEY.search(c['prediction']): continue
    out.append(dict(id=c['id'],who=c['speaker_id'],when=c['when'],year=c['due'],early=c.get('due_early'),
      prob=bool(c.get('has_probability')),notbefore=bool(NOT.search(c['prediction'])),pred=c['prediction'][:150]))
json.dump(out,open(sys.argv[1],'w'),indent=1)
for r in out: print(r['who'],r['when'],r['early'],r['year'],'NB' if r['notbefore'] else '','P' if r['prob'] else '',r['pred'][:90],sep=' | ')
