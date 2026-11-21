from playwright.sync_api import sync_playwright
import re,json
import os
U=os.environ.get('SITE_URL','file://'+os.path.abspath('../site/index.html'))
res={'links':[], 'effects':[], 'dead':[], 'skipped':[]}
with sync_playwright() as p:
    b=p.chromium.launch(channel=os.environ.get('BROWSER_CHANNEL') or None,args=['--autoplay-policy=no-user-gesture-required','--allow-file-access-from-files'])
    ctx=b.new_context(viewport={'width':1280,'height':800});pops=[];ctx.on('page',lambda g:pops.append(g.url))
    pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(U);pg.wait_for_timeout(3500)
    # ---- A. static link audit
    L=pg.evaluate("""()=>[...document.querySelectorAll('a')].map(a=>({t:(a.textContent||'').trim().slice(0,28),h:a.getAttribute('href'),tg:a.target,rel:a.rel,ok:a.hasAttribute('href')}))""")
    ids=set(pg.evaluate("[...document.querySelectorAll('[id]')].map(e=>e.id)"))
    bad=[]
    for l in L:
        h=l['h']
        if not h or h=='#':bad.append(('empty/#',l['t']))
        elif h.startswith('#') and h[1:] not in ids:bad.append(('missing anchor',h))
        elif h.startswith('http') and not (l['tg']=='_blank' and 'noopener' in l['rel']):bad.append(('external without noopener',h))
        elif h.startswith('mailto:') and not re.match(r'^mailto:[^@]+@[^@]+\.\w+$',h):bad.append(('bad mailto',h))
        elif h.startswith('tel:') and not re.match(r'^tel:\+\d{10,13}$',h):bad.append(('bad tel',h))
        elif h.startswith('https://wa.me/') and not re.match(r'^https://wa\.me/917339132560(\?text=.+)?$',h):bad.append(('bad wa',h))
    print('LINKS total',len(L),'| problems:',bad or 'none')
    print('external domains:',sorted({re.sub(r'^https://([^/?]+).*',r'\1',l['h']) for l in L if l['h'] and l['h'].startswith('http')}))
    # ---- B. click-effect audit on one page (no reloads)
    import time;t0=time.time()
    pg.evaluate("""()=>{window.__m=0;new MutationObserver(m=>{window.__m+=m.length}).observe(document.documentElement,{subtree:true,childList:true,attributes:true,characterData:true});document.documentElement.style.scrollBehavior='auto'}""")
    n=pg.evaluate("document.querySelectorAll('a[href],button,summary').length");tested=0;seen=set()
    for i in range(n):
        if time.time()-t0>235:res['skipped'].append(('time-limit','from index %d'%i));break
        info=pg.evaluate("""(i)=>{const e=document.querySelectorAll('a[href],button,summary')[i];if(!e)return null;const r=e.getBoundingClientRect(),cs=getComputedStyle(e);return {t:(e.getAttribute('aria-label')||e.textContent||'').trim().slice(0,30),id:e.id,tag:e.tagName,h:e.getAttribute('href')||'',vis:!e.hidden&&!e.closest('[hidden]')&&cs.visibility!=='hidden'&&cs.display!=='none',dis:e.disabled===true}}""",i)
        if not info or not info['vis'] or info['dis']:res['skipped'].append((info and info['tag'],info and (info['id'] or info['t'])));continue
        y=pg.evaluate("(i)=>{const e=document.querySelectorAll('a[href],button,summary')[i];e.scrollIntoView({block:'center',behavior:'instant'});return Math.floor((scrollY+e.getBoundingClientRect().top)/500)}",i)
        pg.wait_for_timeout(300 if y in seen else 1500);seen.add(y)
        pg.evaluate("window.__m=0;window.__y=scrollY;window.__h=location.hash");np=len(pops)
        try:pg.evaluate("(i)=>document.querySelectorAll('a[href],button,summary')[i].click()",i);pg.wait_for_timeout(450)
        except Exception:res['dead'].append((info['tag'],info['t'],'click error'));continue
        eff=pg.evaluate("({m:window.__m,dy:Math.abs(scrollY-window.__y),h:location.hash!==window.__h,dlg:document.querySelectorAll('dialog[open]').length})")
        ok=eff['m']>0 or eff['dy']>5 or eff['h'] or eff['dlg'] or len(pops)>np or info['h'].startswith(('mailto:','tel:'))
        (res['effects'] if ok else res['dead']).append((info['tag'],info['id'] or info['t'],info['h'][:24]));tested+=1
        pg.keyboard.press('Escape')
    print('CLICK AUDIT: visible controls tested',tested,'| with effect',len(res['effects']),'| NO visible effect:',res['dead'])
    print('skipped (hidden at load; covered by flow tests):',len(res['skipped']),[x[1] for x in res['skipped']][:25])
    print('page errors during audit:',errs)
    b.close()
