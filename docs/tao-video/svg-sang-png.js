const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({deviceScaleFactor:1});
 const dir='imgs/', out='build_video/png/'; fs.mkdirSync(out,{recursive:true});
 for (const f of ['hero','frame','iris','chu-de','poster']){
   const svg=fs.readFileSync(dir+f+'.svg','utf8');
   const m=svg.match(/viewBox="[\d.\s-]*?([\d.]+)\s+([\d.]+)"/); let w=+m[1],h=+m[2]; const s=Math.min(2400/w,2400/h); w=Math.round(w*s);h=Math.round(h*s);
   await p.setViewportSize({width:w,height:h});
   await p.setContent(`<html><head><style>html,body{margin:0}svg{width:${w}px;height:${h}px;display:block}</style></head><body>${svg.replace(/<\?xml[^>]*>/,"")}</body></html>`, {waitUntil:"networkidle"});
   await p.waitForTimeout(500);
   await p.screenshot({path:out+f+'.png'}); console.log(f,w,h);
 }
 await b.close();})();
