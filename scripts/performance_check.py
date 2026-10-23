from playwright.sync_api import sync_playwright
from pathlib import Path
import json
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 page=browser.new_page(viewport={'width':1440,'height':1000})
 page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1600)
 client=page.context.new_cdp_session(page);client.send('Emulation.setCPUThrottlingRate',{'rate':4})
 page.evaluate('''()=>{window.frameTimes=[];window.longTasks=[];window.running=true;let previous=performance.now();function frame(now){window.frameTimes.push(now-previous);previous=now;if(window.running)requestAnimationFrame(frame)}requestAnimationFrame(frame);new PerformanceObserver(list=>{for(const entry of list.getEntries())window.longTasks.push({start:entry.startTime,duration:entry.duration})}).observe({type:'longtask',buffered:false})}''')
 page.context.tracing.start(screenshots=True,snapshots=True)
 for i in range(10):page.mouse.wheel(0,85);page.wait_for_timeout(100)
 page.wait_for_timeout(1200)
 perf=page.evaluate('''()=>{window.running=false;const values=window.frameTimes.slice(2).sort((a,b)=>a-b);return {cpuThrottle:4,scope:'headless desktop Chrome, scroll choreography, not a physical phone',frames:values.length,medianFrameMs:values[Math.floor(values.length*.5)],p95FrameMs:values[Math.floor(values.length*.95)],framesOver34ms:values.filter(v=>v>34).length,longTasks:window.longTasks}}''')
 page.context.tracing.stop(path='screenshots/scroll-trace.zip')
 Path('research/performance-results.json').write_text(json.dumps(perf,indent=2));print(json.dumps(perf))
 browser.close()
