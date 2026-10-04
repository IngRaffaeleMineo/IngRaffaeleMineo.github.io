const P=window.PROFILE_DATA;
function esc(s=''){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}
function setText(id,v){const e=document.getElementById(id);if(e)e.textContent=v}
function renderLinks(){document.getElementById('socialLinks').innerHTML=P.links.map(x=>`<a href="${esc(x.url)}" target="_blank" rel="me noopener">${esc(x.label)}</a>`).join('')}
function renderMotto(){const el=document.getElementById('heroMotto');if(!el)return;const raw=String(P.motto||'');const emoji='🙃';const text=raw.replace(/\s*🙃\s*$/,'');el.textContent=text;if(raw.includes(emoji)){const s=document.createElement('span');s.className='motto-emoji';s.textContent=' '+emoji;el.appendChild(s)}}
function renderResearch(){document.getElementById('researchGrid').innerHTML=P.researchAreas.map(x=>`<article class="research-card"><h3>${esc(x.title)}</h3><p>${esc(x.text)}</p></article>`).join('')}
function renderResearchTrajectory(){document.getElementById('researchTrajectory').innerHTML=P.researchTrajectory.map(x=>`<article class="research-phase"><div class="phase-period">${esc(x.period)}</div><div><h4>${esc(x.title)}</h4><p>${esc(x.text)}</p></div></article>`).join('')}
function renderSelected(){document.getElementById('selectedGrid').innerHTML=P.selectedWorks.map(x=>`<article class="work-card"><span class="tag">${esc(x.label)}</span><h3>${esc(x.title)}</h3><p>${esc(x.venue)} - ${esc(x.year)}</p>${x.link?`<a href="${esc(x.link)}" target="_blank" rel="noopener external">Publication</a>`:`<span class="note">Publication record</span>`}</article>`).join('')}
function renderTimeline(id,items){document.getElementById(id).innerHTML=items.map(x=>`<div class="timeline-item"><div class="timeline-period">${esc(x.period)}</div><div><h3>${esc(x.title||x.degree)}</h3><h4>${esc(x.org)}</h4><p>${esc(x.text||x.detail||'')}</p></div></div>`).join('')}
function renderService(){document.getElementById('serviceGrid').innerHTML=Object.entries(P.service).map(([title,items])=>`<section class="service-card"><h3>${esc(title)}</h3><ul class="clean-list">${items.map(i=>`<li>${esc(i)}</li>`).join('')}</ul></section>`).join('')}
function renderChips(id,items){document.getElementById(id).innerHTML=items.map(x=>`<span class="chip">${esc(x)}</span>`).join('')}
function renderPatents(){document.getElementById('patentGrid').innerHTML=P.patentHighlights.map(x=>`<article class="patent-card"><h3>${esc(x.title)}</h3><div class="status">${esc(x.status)}</div><p>${esc(x.text)}</p></article>`).join('')}
function renderRecognition(){document.getElementById('recognitionGrid').innerHTML=P.recognition.map(x=>`<article class="recognition-card"><div class="recognition-year">${esc(x.year)}</div><h3>${esc(x.title)}</h3><h4>${esc(x.org)}</h4><p>${esc(x.text)}</p></article>`).join('')}
const pubList=document.getElementById('pubList'),pubSearch=document.getElementById('pubSearch'),pubTopic=document.getElementById('pubTopic'),pubType=document.getElementById('pubType'),pubYear=document.getElementById('pubYear');
function authorMarkup(s){return esc(s).replace(/Raffaele Mineo|R\. Mineo/g,'<strong>Raffaele Mineo</strong>')}
function renderPubs(){
  const q=pubSearch.value.trim().toLowerCase(),typ=pubType.value,yr=pubYear.value,topic=pubTopic.value;
  const rows=P.publications.filter(p=>{
    const topicMeta=(P.publicationTopics||[]).find(t=>t.key===p.topic);
    const hay=[p.title,p.authors,p.venue,p.acronym,p.type,p.year,topicMeta?.title].join(' ').toLowerCase();
    return(!q||hay.includes(q))&&(!typ||p.type===typ)&&(!yr||String(p.year||'')===yr)&&(!topic||p.topic===topic)
  });
  document.getElementById('pubCount').textContent=`${rows.length} item${rows.length===1?'':'s'}`;
  const groups=(P.publicationTopics||[]).map(t=>({
    meta:t,
    items:rows.filter(p=>p.topic===t.key).sort((a,b)=>(b.year||0)-(a.year||0))
  })).filter(g=>g.items.length);
  pubList.innerHTML=groups.map(g=>`<section class="pub-topic"><div class="pub-topic-head"><div><h3>${esc(g.meta.title)}</h3><p>${esc(g.meta.text)}</p></div><span>${g.items.length}</span></div>${g.items.map(p=>`<article class="pub"><div class="pub-year">${p.year||'-'}</div><div><div class="pub-title">${esc(p.title)}${p.jointFirst?'<span class="pub-badge">joint first author</span>':''}</div><div class="pub-authors">${authorMarkup(p.authors||'')}</div><div class="pub-meta">${esc(p.acronym||p.venue)}${p.acronym&&p.venue&&p.acronym!==p.venue?' - '+esc(p.venue):''} - ${esc(p.type)}</div></div>${p.link?`<a class="pub-link" href="${esc(p.link)}" target="_blank" rel="noopener external">Open</a>`:''}</article>`).join('')}</section>`).join('')
}
function initPubFilters(){
  const topics=P.publicationTopics||[];
  pubTopic.innerHTML='<option value="">All research topics</option>'+topics.map(x=>`<option value="${esc(x.key)}">${esc(x.title)}</option>`).join('');
  const types=[...new Set(P.publications.map(p=>p.type).filter(Boolean))].sort();
  pubType.innerHTML='<option value="">All output types</option>'+types.map(x=>`<option>${esc(x)}</option>`).join('');
  const years=[...new Set(P.publications.map(p=>p.year).filter(Boolean))].sort((a,b)=>b-a);
  pubYear.innerHTML='<option value="">All years</option>'+years.map(x=>`<option>${x}</option>`).join('');
  [pubSearch,pubTopic,pubType,pubYear].forEach(el=>el.addEventListener('input',renderPubs));
  [pubTopic,pubType,pubYear].forEach(el=>el.addEventListener('change',renderPubs))
}
function renderExtended(){document.getElementById('teachingList').innerHTML=P.teaching.map(x=>`<li>${esc(x)}</li>`).join('');document.getElementById('credentialsList').innerHTML=P.credentials.map(x=>`<li>${esc(x)}</li>`).join('');document.getElementById('languagesList').innerHTML=P.languages.map(x=>`<li>${esc(x)}</li>`).join('');document.getElementById('technicalList').innerHTML=Object.entries(P.technical).map(([k,v])=>`<p><strong>${esc(k)}:</strong> ${esc(v)}</p>`).join('')}
function boot(){
  setText('heroName',P.name);
  setText('heroRole',P.role);
  setText('heroAffiliation',P.affiliation);
  setText('heroCopy',P.researchStatement);
  renderMotto();
  setText('location',P.location);
  setText('emailText',P.email);
  document.getElementById('emailLink').href='mailto:'+(P.emailHref||P.email.replace('[at]','@'));
  renderLinks();
  renderResearch();
  renderResearchTrajectory();
  renderSelected();
  renderTimeline('experienceTimeline',P.experience);
  renderTimeline('educationTimeline',P.education);
  renderService();
  renderRecognition();
  renderChips('membershipChips',P.memberships);
  renderChips('collabChips',P.collaborations);
  renderPatents();
  initPubFilters();
  renderPubs();
  renderExtended();
  document.getElementById('yearNow').textContent=new Date().getFullYear();
}
boot();
