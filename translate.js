(()=>{
'use strict';
const HOST_ID='google_translate_element';
const GOOGLE_TRANSLATE_SCRIPT='https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
function host(){return document.getElementById(HOST_ID)}
function showFallback(){
  const element=host();if(!element)return;
  element.innerHTML='';
  const link=document.createElement('a');
  link.className='translate-fallback';
  link.href='https://translate.google.com/';
  link.target='_blank';link.rel='noopener';
  link.textContent='Translate';link.title='Open Google Translate';
  element.appendChild(link)
}
window.googleTranslateElementInit=function(){
  const element=host();if(!element)return;
  try{
    if(!window.google||!google.translate||!google.translate.TranslateElement){showFallback();return}
    element.innerHTML='';
    new google.translate.TranslateElement({
      pageLanguage:'en',autoDisplay:false,multilanguagePage:true,
      layout:google.translate.TranslateElement.InlineLayout.SIMPLE
    },HOST_ID)
  }catch(error){showFallback()}
};
function loadGoogleTranslator(){
  if(!host())return;
  if(window.google&&google.translate&&google.translate.TranslateElement){window.googleTranslateElementInit();return}
  if(document.querySelector('script[data-google-website-translator]'))return;
  const script=document.createElement('script');
  script.src=GOOGLE_TRANSLATE_SCRIPT;script.async=true;script.defer=true;
  script.dataset.googleWebsiteTranslator='true';script.onerror=showFallback;
  document.head.appendChild(script)
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',loadGoogleTranslator,{once:true});
else loadGoogleTranslator()
})();