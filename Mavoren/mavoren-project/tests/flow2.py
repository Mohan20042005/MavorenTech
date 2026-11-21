from playwright.sync_api import sync_playwright
import os
U=os.environ.get('SITE_URL','file://'+os.path.abspath('../site/index.html'))
R=[]
def chk(name,ok,extra=''):R.append((name,bool(ok)));print(('PASS ' if ok else 'FAIL ')+name,extra)
with sync_playwright() as p:
    b=p.chromium.launch(channel=os.environ.get('BROWSER_CHANNEL') or None,args=['--autoplay-policy=no-user-gesture-required','--allow-file-access-from-files'])
    ctx=b.new_context(viewport={'width':1280,'height':800});pops=[];ctx.on('page',lambda g:pops.append(g.url));pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(U);pg.wait_for_timeout(3500)
    pg.evaluate("document.documentElement.style.scrollBehavior='auto'")
    # pricing cards
    cards=pg.eval_on_selector_all('.pc2','e=>e.length');okc=0;oks=0
    for i in range(cards):
        pg.evaluate("(i)=>document.querySelectorAll('.pc2')[i].scrollIntoView({block:'center'})",i);pg.wait_for_timeout(200)
        pg.evaluate("(i)=>document.querySelectorAll('.pc2 a.bp')[i].click()",i);pg.wait_for_timeout(120)
        nm=pg.eval_on_selector_all('.pc2 h3','(e)=>e.map(x=>x.textContent)')[i];okc+=nm.split(' (')[0][:8] in pg.inner_text('#chipt')
        pg.evaluate("(i)=>document.querySelectorAll('.pc2 summary')[i].click()",i);oks+=pg.evaluate("(i)=>document.querySelectorAll('.pc2 details')[i].open",i)
    chk('pricing "Get a quote" buttons fill the enquiry (%d cards)'%cards,okc==cards,'%d/%d'%(okc,cards));chk('"What\'s included" toggles open',oks==cards,'%d/%d'%(oks,cards))
    # tiers filter
    ok=True
    for t,n in (('starter',3),('business',2),('pro',3),('commerce',1),('care',2),('all',11)):
        pg.evaluate("(t)=>document.querySelector('.tb[data-t='+t+']').click()",t);ok&=pg.eval_on_selector_all('.pc2','e=>e.filter(x=>!x.hidden).length')==n
    chk('tier filter buttons show the right cards',ok)
    # tier-card rows (services section)
    rows=pg.eval_on_selector_all('.tl2 a','e=>e.length');k=0
    for i in range(rows):
        pg.evaluate("(i)=>document.querySelectorAll('.tl2 a')[i].click()",i);pg.wait_for_timeout(80);k+=len(pg.inner_text('#chipt'))>3
    chk('service rows inside the 3 tier cards (%d) prefill the enquiry'%rows,k==rows,'%d/%d'%(k,rows))
    # finder + estimator
    pg.evaluate("document.querySelector('#plan').scrollIntoView()");pg.wait_for_timeout(300)
    pg.evaluate("document.querySelector('#chipx').click()")
    for nm,v in (('fb','health'),('fn','multi'),('fm','yes')):pg.evaluate("(a)=>{const i=document.querySelector('input[name='+a[0]+'][value='+a[1]+']');i.checked=true;i.dispatchEvent(new Event('change',{bubbles:true}))}",[nm,v])
    chk('package finder shows a result',pg.inner_text('#fr').startswith('Our suggestion'),pg.inner_text('#fr').split('\n')[1])
    pg.evaluate("document.querySelector('#fr a').click()");chk('finder result button fills the enquiry','Healthcare' in pg.inner_text('#chipt'))
    pg.fill('#ep','MAVOREN30');pg.click('#eb');chk('estimator Apply works','4,899' in pg.inner_text('#eo') or '30%' in pg.inner_text('#epm'))
    pg.evaluate("document.querySelector('#em').click()");chk('estimator maintenance checkbox adds a row','maintenance' in pg.inner_text('#eo').lower())
    pg.evaluate("document.querySelector('#eq').click()");chk('estimator "Request this quote" fills the enquiry','Business' in pg.inner_text('#chipt') or 'Landing' in pg.inner_text('#chipt'))
    # form steps
    pg.evaluate("document.querySelector('#enquire').scrollIntoView()");pg.wait_for_timeout(300)
    pg.fill('[name=name]','Test User');pg.fill('[name=biz]','Cafe X');pg.fill('[name=email]','a@b.co');pg.fill('[name=wa]','9876543210')
    pg.click('#nx');s2=pg.is_visible('[name=cat]');pg.click('#bk');chk('Next / Back buttons move between steps',s2 and pg.is_visible('[name=name]'))
    pg.click('#nx');pg.select_option('[name=cat]',index=1);pg.select_option('[name=budget]',index=2);pg.click('#nx');pg.fill('[name=desc]','Menu website with ordering.')
    pg.click('#sb');pg.wait_for_selector('#cf[open]');chk('submit opens the confirmation dialog with the message','Hello Mavoren' in pg.inner_text('#cfm'))
    pg.click('#cfe');chk('"Edit enquiry" closes the dialog',pg.eval_on_selector('#cf','e=>!e.open'))
    pg.click('#sb');pg.wait_for_selector('#cf[open]');n=len(pops)
    with pg.context.expect_page() as np:pg.click('#cfo')
    chk('"Open WhatsApp" opens wa.me with the message (new tab opened, link correct)',len(pops)>n and pg.get_attribute('#cfo','href').startswith('https://wa.me/917339132560?text=') and pg.is_visible('#done'))
    pg.click('[data-copy-from]');pg.wait_for_timeout(400);chk('"Copy message" gives feedback',pg.inner_text('#toast') in ('Copied to clipboard','Copy failed'),pg.inner_text('#toast'))
    pg.click('#ed');chk('"Edit enquiry" on the success panel returns to the form',pg.is_visible('[name=name]'))
    # search dialog
    pg.click('#sbtn');chk('search opens',pg.eval_on_selector('#sd','e=>e.open'));pg.click('#sx');chk('search Close button works',pg.eval_on_selector('#sd','e=>!e.open'))
    # theme
    pg.emulate_media(color_scheme='light');pg.wait_for_timeout(300);d1=pg.evaluate('document.documentElement.dataset.theme');pg.emulate_media(color_scheme='dark');pg.wait_for_timeout(300);chk('theme follows the device setting live (no toggle button)',d1=='light' and pg.evaluate('document.documentElement.dataset.theme')=='dark' and pg.locator('#th').count()==0)
    # video pause
    pg.evaluate("window.scrollTo(0,0)");pg.wait_for_timeout(500);pg.click('#vp');a=pg.evaluate("document.querySelector('#hv').paused");pg.click('#vp');pg.wait_for_timeout(500);chk('Pause / Play background button',a and not pg.evaluate("document.querySelector('#hv').paused"))
    # ad
    pg.evaluate("window.scrollTo(0,innerHeight*2.5)");pg.wait_for_timeout(1500);chk('offer popup appears after 2 screens',pg.eval_on_selector('#ad','e=>!e.hidden'))
    pg.click('.ad [data-copy]');pg.wait_for_timeout(300);chk('popup "Copy code" works',pg.inner_text('.ad [data-copy]')=='Copied' or 'Copied' in pg.inner_text('#toast') or 'failed' in pg.inner_text('#toast'),pg.inner_text('#toast'))
    pg.click('#adx');pg.wait_for_timeout(700);chk('popup close (x) works',pg.eval_on_selector('#ad','e=>e.hidden'))
    # back to top
    pg.evaluate("window.scrollTo(0,2500)");pg.wait_for_timeout(500);pg.click('#bt');pg.wait_for_timeout(1500);chk('back-to-top returns to the top',pg.evaluate('scrollY')<2)
    # faq/insights toggles
    ok=True
    for sel in ('#faq summary','#insights summary'):
        pg.evaluate("(s)=>document.querySelector(s).scrollIntoView({block:'center'})",sel);pg.click(sel);ok&=pg.evaluate("(s)=>document.querySelector(s).parentElement.open",sel)
    chk('FAQ and blog accordions expand',ok)
    # mobile menu
    m=ctx.new_page();m.set_viewport_size({'width':375,'height':800});m.goto(U);m.wait_for_timeout(3000);m.evaluate("document.documentElement.style.scrollBehavior='auto'")
    links=m.eval_on_selector_all('#nv a[href^="#"]','e=>e.map(x=>x.getAttribute("href"))');good=0
    for h in links:
        m.click('#mb');m.wait_for_timeout(250);opened=m.get_attribute('#mb','aria-expanded')=='true'
        m.click('#nv a[href="%s"]'%h);m.wait_for_timeout(500);good+=opened and m.get_attribute('#mb','aria-expanded')=='false' and m.evaluate("location.hash")==h
    chk('mobile menu opens and every item navigates then closes (%d items)'%len(links),good==len(links),'%d/%d'%(good,len(links)))
    m.click('#mb');m.keyboard.press('Escape');chk('mobile menu closes with Escape',m.get_attribute('#mb','aria-expanded')=='false')
    print('\nSUMMARY: %d/%d checks passed | page errors: %s'%(sum(o for _,o in R),len(R),errs or 'none'));b.close()
