const { chromium } = require('playwright-core');
const fs=require('fs');
(async()=>{
  const src=fs.readFileSync('./sa_ict_skills_analytics.html','utf8').replace(/<script src="https:\/\/cdnjs[^>]*><\/script>/,'<script src="file://'+process.cwd()+'/node_modules/chart.js/dist/chart.umd.js"></script>');
  fs.writeFileSync('test.html','<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+src+'</body></html>');
  const exe=process.env.PLAYWRIGHT_BROWSERS_PATH?process.env.PLAYWRIGHT_BROWSERS_PATH+'/chromium':'/opt/pw-browsers/chromium';
  let b; try{ b=await chromium.launch({executablePath:exe}); }catch(e){ b=await chromium.launch(); }
  const errs=[];
  for(const [name,w,h] of [['desk',1440,900],['phone',400,860]]){
    const p=await b.newPage({viewport:{width:w,height:h}});
    p.on('console',m=>{if(m.type()==='error')errs.push(name+': '+m.text());}); p.on('pageerror',e=>errs.push(name+' pageerror: '+e.message));
    await p.goto('file://'+process.cwd()+'/test.html'); await p.waitForTimeout(700);
    const tabs=name==='desk'?['overview','iva','level','skills','recs','method']:['overview'];
    for(const t of tabs){ await p.click('#t-'+t); await p.waitForTimeout(600); await p.screenshot({path:`s-${name}-${t}.png`,fullPage:true}); }
    if(name==='desk'){ await p.click('#t-overview'); await p.click('#ms-JobSector .ms-btn'); await p.click('#ms-JobSector .opt:nth-of-type(3)'); await p.waitForTimeout(500); await p.screenshot({path:'s-desk-filter.png',clip:{x:0,y:0,width:1440,height:420}}); }
    const sw=await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]); console.log(name,'scrollWidth',sw);
  }
  console.log('ERRORS',errs); await b.close();
})();
