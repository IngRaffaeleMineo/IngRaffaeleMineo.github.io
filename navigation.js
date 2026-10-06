(()=>{
'use strict';
const SECTION_ROUTES=Object.freeze({
  '/about':'about','/research':'research','/selected-work':'selected','/patents':'patents',
  '/service':'service','/recognition':'recognition','/experience':'experience',
  '/education':'education','/network':'network','/background':'extended',
  '/publications':'publications','/contact':'contact'
});
const SECTION_PATHS=Object.freeze(Object.fromEntries(Object.entries(SECTION_ROUTES).map(([path,id])=>[id,path])));
const ROUTE_TARGETS=Object.freeze([{path:'/',id:'top'},...Object.entries(SECTION_ROUTES).map(([path,id])=>({path,id}))]);
let scrollFrame=0,spyFrame=0,routeLocked=false,unlockTimer=0;
function currentPath(){const path=decodeURIComponent(window.location.pathname||'/').replace(/\/+$/,'');return path||'/'}
function routeId(path){return path==='/'?'top':SECTION_ROUTES[path]}
function headerOffset(){const header=document.querySelector('.site-header');return header?Math.ceil(header.getBoundingClientRect().height)+14:14}
function targetScrollY(id){
  if(id==='top')return 0;
  const target=document.getElementById(id); if(!target)return null;
  const raw=window.scrollY+target.getBoundingClientRect().top-headerOffset();
  const max=Math.max(0,document.documentElement.scrollHeight-window.innerHeight);
  return Math.max(0,Math.min(max,raw))
}
function easeInOutQuint(t){return t<.5?16*t*t*t*t*t:1-Math.pow(-2*t+2,5)/2}
function markActive(path){
  document.querySelectorAll('#navLinks a[data-route]').forEach(link=>{
    if(link.dataset.route===path)link.setAttribute('aria-current','page'); else link.removeAttribute('aria-current')
  })
}
function stopAnimation(sync=true){
  if(scrollFrame){cancelAnimationFrame(scrollFrame);scrollFrame=0}
  if(unlockTimer){clearTimeout(unlockTimer);unlockTimer=0}
  routeLocked=false;
  if(sync)scheduleSpy()
}
function animateTo(id){
  stopAnimation(false);
  const endY=targetScrollY(id); if(endY===null)return;
  const startY=window.scrollY,delta=endY-startY,distance=Math.abs(delta);
  if(distance<2){window.scrollTo({left:0,top:endY,behavior:'auto'});routeLocked=false;scheduleSpy();return}
  routeLocked=true;
  const duration=Math.min(1500,Math.max(720,620+distance*.16));
  let startedAt=null;
  const tick=now=>{
    if(startedAt===null)startedAt=now;
    const progress=Math.min(1,(now-startedAt)/duration);
    window.scrollTo({left:0,top:startY+delta*easeInOutQuint(progress),behavior:'auto'});
    if(progress<1)scrollFrame=requestAnimationFrame(tick);
    else{
      scrollFrame=0;
      window.scrollTo({left:0,top:endY,behavior:'auto'});
      unlockTimer=window.setTimeout(()=>{routeLocked=false;unlockTimer=0;scheduleSpy()},80)
    }
  };
  scrollFrame=requestAnimationFrame(tick)
}
function jumpTo(id){stopAnimation(false);const y=targetScrollY(id);if(y!==null)window.scrollTo({left:0,top:y,behavior:'auto'})}
function syncRouteToScroll(){
  spyFrame=0;if(routeLocked)return;
  const marker=window.scrollY+headerOffset()+Math.min(window.innerHeight*.28,240);
  let active=ROUTE_TARGETS[0];
  for(const item of ROUTE_TARGETS){const element=document.getElementById(item.id);if(element&&element.offsetTop<=marker)active=item}
  if(window.innerHeight+window.scrollY>=document.documentElement.scrollHeight-6)active={path:'/contact',id:'contact'};
  markActive(active.path);
  if(currentPath()!==active.path)history.replaceState({},'',active.path)
}
function scheduleSpy(){if(!spyFrame)spyFrame=requestAnimationFrame(syncRouteToScroll)}
function closeMobileMenu(){
  const menu=document.getElementById('navLinks'),button=document.getElementById('menuBtn');
  if(menu)menu.classList.remove('open'); if(button)button.setAttribute('aria-expanded','false')
}
function handleRouteClick(event){
  if(event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
  const link=event.target.closest('a[data-route]');if(!link)return;
  const path=link.dataset.route,id=routeId(path);if(!id)return;
  event.preventDefault();closeMobileMenu();
  if(currentPath()!==path)history.pushState({},'',path);else history.replaceState({},'',path);
  markActive(path);animateTo(id)
}
function initMobileMenu(){
  const button=document.getElementById('menuBtn'),menu=document.getElementById('navLinks');if(!button||!menu)return;
  button.addEventListener('click',()=>{const open=menu.classList.toggle('open');button.setAttribute('aria-expanded',String(open))})
}
function initInitialRoute(){
  const hashId=window.location.hash.replace(/^#/,'');const hashPath=SECTION_PATHS[hashId];
  if(hashPath){history.replaceState({},'',hashPath);markActive(hashPath);requestAnimationFrame(()=>requestAnimationFrame(()=>jumpTo(hashId)));return}
  const path=currentPath(),id=routeId(path);
  if(id){markActive(path);requestAnimationFrame(()=>jumpTo(id))}else{markActive('/');scheduleSpy()}
}
if('scrollRestoration' in history)history.scrollRestoration='manual';
document.documentElement.style.scrollBehavior='auto';
if(document.body)document.body.style.scrollBehavior='auto';
document.addEventListener('click',handleRouteClick,true);
window.addEventListener('popstate',()=>{const path=currentPath(),id=routeId(path);if(id){markActive(path);animateTo(id)}});
window.addEventListener('scroll',scheduleSpy,{passive:true});
window.addEventListener('resize',scheduleSpy,{passive:true});
window.addEventListener('wheel',()=>{if(routeLocked)stopAnimation()},{passive:true});
window.addEventListener('touchstart',()=>{if(routeLocked)stopAnimation()},{passive:true});
window.addEventListener('keydown',event=>{if(routeLocked&&['ArrowUp','ArrowDown','PageUp','PageDown','Home','End',' '].includes(event.key))stopAnimation()});
initMobileMenu();initInitialRoute();scheduleSpy()
})();