$ErrorActionPreference = 'Stop'
$out = $PSScriptRoot

# Phase headers (shared across all workflows)
$phases = @(
  @{Name='CONCEPT';         Color='#6366F1'},
  @{Name='PRODUCTION';      Color='#2563EB'},
  @{Name='POST-PRODUCTION'; Color='#0891B2'},
  @{Name='REVIEW &amp; QA'; Color='#16A34A'},
  @{Name='DISTRIBUTION';    Color='#D97706'},
  @{Name='POST-LAUNCH';     Color='#DC2626'}
)

# Workflow data. Each workflow has 6 phases of (steps[], crew[]).
$workflows = @(
  @{
    Id='A'; File='A-viral-hook'; Title='Viral Hook Clip / Meme';
    Meta='Social &amp; Viral Content  &#183;  5&#8211;15 seconds';
    Critic='Karen X. Cheng &quot;3-second test&quot;  &#183;  target hold-rate &gt;65% at 3s';
    CriticSub='Iterate next post based on first-24h retention curve';
    Steps=@(
      @('Trend mining (sounds,','formats, memes)','Hook copy + 3 visual','beats'),
      @('Shoot or AI-generate','vertical 9:16 clip'),
      @('Cut, captions,','sound sync','Auto-caption pass'),
      @('Mute test','Hook test','A/B title + cover'),
      @('Post at peak time','Cross-post TikTok,','Reels, Shorts'),
      @('24h retention curve','Hold-rate, comments','Iterate next post')
    );
    Crews=@(
      @('Trend Researcher','Copywriter','Social Strategist'),
      @('Creator / Talent','AI Generator Op'),
      @('Editor','Captioner'),
      @('Social Strategist','Creator'),
      @('Social Strategist'),
      @('Data Analyst','Community Mgr')
    )
  },
  @{
    Id='B'; File='B-ugc-ad'; Title='UGC-Style Performance Ad';
    Meta='Marketing &amp; Advertising  &#183;  15&#8211;45 seconds';
    Critic='Andrew Foxwell ad-account audit  &#183;  hook-rate &gt;30%, CTR &gt;1.5%, +ROAS';
    CriticSub='Refresh fatigued ads at 2&#215; frequency; iterate creatives weekly';
    Steps=@(
      @('Creative brief +','hook variants','Creator casting +','product shipping'),
      @('Creator self-shoots','5-10 raw variants'),
      @('Edit + end-card CTA','Multi-aspect 1:1,','9:16, 4:5 cuts'),
      @('FTC #ad disclosure','IP + music license','Brand safety check'),
      @('Upload Meta /','TikTok Ads Manager','Set budget + audience'),
      @('ROAS, CTR,','hook-rate','Kill losers,','scale winners')
    );
    Crews=@(
      @('Perf Marketer','Copywriter','UGC Casting'),
      @('UGC Creator'),
      @('Editor','Motion Designer'),
      @('Legal / Clearance','Brand Manager'),
      @('Media Buyer','Perf Marketer'),
      @('Perf Marketer','Data Analyst')
    )
  },
  @{
    Id='C'; File='C-animated-explainer'; Title='Animated Explainer';
    Meta='Educational  &#183;  60&#8211;180 seconds';
    Critic='Cathy Moore action-mapping audit  &#183;  target completion &gt;70%';
    CriticSub='Julie Dirksen learning-design review on retention curves';
    Steps=@(
      @('Discovery + learning','objectives','Script (problem -&gt;','solve -&gt; CTA)','Storyboard + style'),
      @('VO record in booth','2D animate scenes','Original score + SFX'),
      @('Edit, color,','final mix at -16 LUFS'),
      @('SME accuracy check','Brand sign-off','WCAG 2.2 captions'),
      @('Landing page embed','YouTube + Wistia','Sales decks'),
      @('Completion rate','On-page conversion','Recut weak segments')
    );
    Crews=@(
      @('Instructional Designer','SME','Scriptwriter','Storyboard Artist'),
      @('VO Artist','2D Animator','Composer'),
      @('Editor','Re-recording Mixer'),
      @('SME','Brand Manager','Accessibility Spec'),
      @('Marketing Manager','SEO Specialist'),
      @('Marketing Analyst','Instructional Designer')
    )
  },
  @{
    Id='D'; File='D-personalized-birthday'; Title='Personalized Birthday Video';
    Meta='Personalized &amp; Custom  &#183;  15&#8211;60 seconds';
    Critic='DMA audit + GDPR/CCPA privacy review  &#183;  share-rate &gt;25%';
    CriticSub='Gifted videos go viral when share-rate exceeds 25%';
    Steps=@(
      @('Variable template','(name, age, photo)','Data schema +','intake form'),
      @('User submits assets','Render personalized','variant per user'),
      @('Automated face /','name / audio detect','Loudness scan'),
      @('Spot-check 1 in 50','Abuse / consent','check'),
      @('Email / WhatsApp /','in-app delivery','Instant per user'),
      @('Open, share, re-gift','NPS, template winners','A/B optimize')
    );
    Crews=@(
      @('Template Designer','Personalization Eng','UX Designer'),
      @('Personalization Eng','AI Voice Operator'),
      @('AI QA Reviewer'),
      @('Trust &amp; Safety','Personalization Eng'),
      @('CRM Specialist','Backend Engineer'),
      @('Product Analyst','CRM Specialist')
    )
  },
  @{
    Id='E'; File='E-ai-short-film'; Title='AI Multi-Scene Short Film';
    Meta='Storytelling &amp; Entertainment  &#183;  1&#8211;5 minutes';
    Critic='Runway AI Film Festival jury  &#183;  Curious Refuge community critique';
    CriticSub='Paul Trillo / Karen X. Cheng peer review on craft and consistency';
    Steps=@(
      @('Logline + treatment','Scene breakdown','Storyboard','Character bible +','locked seeds'),
      @('Scene generation','passes (rough -&gt; final)','Voice + lip-sync','Original score'),
      @('Edit, color grade','VFX cleanup','Upscale to 4K'),
      @('Director&#39;s notes','C2PA provenance','AI disclosure'),
      @('Festival submissions','YouTube + curated','platforms'),
      @('Festival feedback','Audience Q&amp;A','Director&#39;s cut v2')
    );
    Crews=@(
      @('Writer / Director','Storyboard Artist','Concept Artist','AI Avatar Designer'),
      @('AI Prompt Engineer','AI Generator Op','AI QA Reviewer','Voice Cloner','Composer'),
      @('Editor','Colorist','VFX Compositor'),
      @('Director','Editor','Legal Reviewer'),
      @('Producer','Festival Strategist'),
      @('Director','Producer')
    )
  },
  @{
    Id='F'; File='F-corporate-training'; Title='Corporate Training Video';
    Meta='Professional &amp; Business  &#183;  3&#8211;10 minutes';
    Critic='ATD peer review  &#183;  completion &gt;85%, L2 quiz &gt;80%';
    CriticSub='Cathy Moore action-mapping; Kirkpatrick L1&#8211;L4 evaluation';
    Steps=@(
      @('Needs analysis +','learning objectives','Compliance review','Script + scenarios'),
      @('Shoot presenter or','render avatar','Screen-recordings','+ animations'),
      @('Edit, captions','(mandatory)','Audio description'),
      @('SME accuracy','Compliance sign-off','WCAG 2.2 check'),
      @('Upload to LMS','Assign cohort','Track completion'),
      @('Completion %','Quiz scores','Behavior change','30/60/90 reviews')
    );
    Crews=@(
      @('Instructional Designer','Compliance Officer','SME','Scriptwriter'),
      @('Presenter / Avatar','DoP','Screen-Recordist','Motion Designer'),
      @('Editor','Captioner','Accessibility Spec'),
      @('SME','Compliance Officer','Accessibility Spec'),
      @('LMS Specialist','L&amp;D Lead'),
      @('L&amp;D Analyst','Instructional Designer')
    )
  },
  @{
    Id='G'; File='G-music-video'; Title='Music Video (Live + AI VFX)';
    Meta='Storytelling / Music  &#183;  1&#8211;4 minutes';
    Critic='MTV VMA / UKMVA jury benchmarks  &#183;  Hype Williams craft refs';
    CriticSub='Chartmetric streaming-lift attribution; Spotify Canvas test';
    Steps=@(
      @('Treatment from song','Artist + label meet','Locations + casting','Shot list + lookbook'),
      @('Shoot day(s)','AI VFX plate','generation (style','transfer, world)'),
      @('Edit to music','Color grade, VFX','Sound mix to master'),
      @('Artist + label','approval','Sample clearance,','sync rights'),
      @('YouTube premiere','Vevo + Shorts','cutdowns'),
      @('Views, retention','Chart impact','Cutdown strategy')
    );
    Crews=@(
      @('MV Director','Producer','Choreographer','DoP'),
      @('DoP','Camera Op','Gaffer / Grip','AI Generator Op','Talent / MUA'),
      @('Editor','Colorist','VFX Compositor','Re-recording Mixer'),
      @('Music Supervisor','Label A&amp;R','Legal'),
      @('Label Digital','Social Strategist'),
      @('Label Analyst','Social Strategist')
    )
  },
  @{
    Id='H'; File='H-ai-avatar'; Title='AI Avatar Talking-Head';
    Meta='Avatar &amp; Talking Head  &#183;  30&#8211;120 seconds';
    Critic='Hany Farid deepfake rigor  &#183;  Nina Schick synthetic-media ethics';
    CriticSub='Partnership on AI Synthetic Media Framework audit; C2PA provenance';
    Steps=@(
      @('Use case + brand','persona for avatar','Script + tone'),
      @('Build / pick avatar','+ voice','Render TTS + lip-sync'),
      @('B-roll overlays','Captions + brand','template'),
      @('Pronunciation pass','Brand check','AI disclosure +','C2PA label'),
      @('LinkedIn, help','center, intranet,','email'),
      @('Engagement metrics','Comprehension','survey','Persona refinement')
    );
    Crews=@(
      @('Brand Strategist','Avatar Designer','Scriptwriter'),
      @('AI Avatar Designer','Voice Designer','AI Generator Op','Lip-Sync Specialist'),
      @('Motion Designer','Editor'),
      @('Brand Manager','Legal Reviewer'),
      @('Marketing','Comms'),
      @('Comms Analyst')
    )
  },
  @{
    Id='I'; File='I-documentary'; Title='Documentary &quot;Explained&quot; Episode';
    Meta='Educational / News  &#183;  5&#8211;15 minutes';
    Critic='Pulitzer / duPont-Columbia / Peabody standards  &#183;  SPJ ethics';
    CriticSub='Poynter post-mortem; Columbia Journalism Review critique';
    Steps=@(
      @('Topic pitch + angle','Deep research +','interview list','Script + visual plan'),
      @('Interviews + B-roll','Archive footage /','stills licensing','Motion gfx + data viz'),
      @('Edit + narration','record','Color, mix'),
      @('Fact-check every','claim','Legal review','Editorial standards'),
      @('YouTube release','Podcast clip','Newsletter feature'),
      @('CTR, AVD,','retention curve','Pinned corrections','Next-ep learnings')
    );
    Crews=@(
      @('Showrunner','Researcher','Fact-Checker','Scriptwriter'),
      @('Director','DoP','Archive Producer','Motion Designer'),
      @('Editor','Narrator','Colorist','Re-recording Mixer'),
      @('Fact-Checker','Legal Reviewer','Editor-in-Chief'),
      @('Channel Manager','Social Strategist','SEO'),
      @('Channel Analyst','Standards Editor')
    )
  },
  @{
    Id='J'; File='J-feature-film'; Title='Feature-Length AI Film';
    Meta='Long-form Cinematic  &#183;  60&#8211;120 minutes';
    Critic='Sundance / Cannes / Venice juries  &#183;  AMPAS  &#183;  Runway AIFF';
    CriticSub='Target Metacritic &#8805;85; festival selection; profitable distribution';
    Steps=@(
      @('Screenplay','Financing + IP','Visual dev + bible','Storyboard / animatic','Voice + likeness cast'),
      @('Scene-by-scene AI','generation','Consistency QC','Voice + lip-sync','Original score'),
      @('Editorial -&gt; picture','lock','VFX, 4K upscale,','color grade','Atmos sound mix'),
      @('Test screenings','Director&#39;s cut','MPA rating','Legal QC, C2PA'),
      @('Festival premiere','Sales agent -&gt;','streamer/theatrical','Trailer + press tour'),
      @('Box office /','streaming metrics','Reviews + awards','Sequel / IP plan')
    );
    Crews=@(
      @('Screenwriter','Producer / EP','Director','Concept Artists','Casting Director'),
      @('AI Generator Ops','AI QA Team','Voice Cast','Lip-Sync Specialists','Composer'),
      @('Editor','VFX Compositor','Colorist','Re-recording Mixer'),
      @('Director','Editor','Legal Reviewer','MPA'),
      @('Sales Agent','Distributor','Marketing Lead','Trailer House'),
      @('Distributor','Awards Strategist','Producer')
    )
  }
)

foreach ($w in $workflows) {
  $sb = New-Object System.Text.StringBuilder
  [void]$sb.Append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 740" font-family="Segoe UI, Arial, sans-serif">')
  [void]$sb.Append('<rect width="1400" height="740" fill="#FAFAFA"/>')
  [void]$sb.AppendFormat('<text x="30" y="38" font-size="22" font-weight="700" fill="#0F172A">Workflow {0} &#8212; {1}</text>', $w.Id, $w.Title)
  [void]$sb.AppendFormat('<text x="30" y="60" font-size="13" fill="#64748B">{0}</text>', $w.Meta)

  for ($i=0; $i -lt 6; $i++) {
    $x = 25 + $i*228
    $p = $phases[$i]
    $steps = $w.Steps[$i]
    $crew  = $w.Crews[$i]

    # Card background
    [void]$sb.AppendFormat('<rect x="{0}" y="80" width="218" height="555" rx="12" fill="#fff" stroke="#E2E8F0"/>', $x)
    # Colored header band with rounded top
    $hx = $x; $hx12 = $x+12; $hr = $x+206
    [void]$sb.AppendFormat('<path d="M{0} 80 H{1} a12 12 0 0 1 12 12 V134 H{2} V92 a12 12 0 0 1 12 -12 Z" fill="{3}"/>', $hx12, $hr, $hx, $p.Color)
    [void]$sb.AppendFormat('<text x="{0}" y="103" font-size="10" fill="#fff" opacity="0.85" letter-spacing="1">PHASE {1}</text>', $x+15, $i+1)
    [void]$sb.AppendFormat('<text x="{0}" y="123" font-size="15" font-weight="700" fill="#fff">{1}</text>', $x+15, $p.Name)

    # Steps label
    [void]$sb.AppendFormat('<text x="{0}" y="160" font-size="10" font-weight="700" fill="#475569" letter-spacing="1">KEY STEPS</text>', $x+15)

    # Step lines (first line gets bullet, continuation lines no bullet)
    $sy = 182
    $newStep = $true
    foreach ($s in $steps) {
      if ($newStep) {
        $line = '&#8226; ' + $s
      } else {
        $line = '   ' + $s
      }
      [void]$sb.AppendFormat('<text x="{0}" y="{1}" font-size="12" fill="#0F172A">{2}</text>', $x+15, $sy, $line)
      $sy += 18
      # If next entry begins a new bullet: heuristic – treat each entry as a new bullet by default.
      $newStep = $true
    }

    # Crew box
    [void]$sb.AppendFormat('<rect x="{0}" y="445" width="198" height="180" rx="8" fill="#F1F5F9"/>', $x+10)
    [void]$sb.AppendFormat('<text x="{0}" y="465" font-size="10" font-weight="700" fill="#475569" letter-spacing="1">CREW</text>', $x+22)
    $cy = 487
    foreach ($c in $crew) {
      [void]$sb.AppendFormat('<text x="{0}" y="{1}" font-size="11" fill="#0F172A">&#8226; {2}</text>', $x+22, $cy, $c)
      $cy += 18
    }

    # Arrow to next phase
    if ($i -lt 5) {
      $ax = $x + 222
      [void]$sb.AppendFormat('<polygon points="{0},355 {1},349 {1},361" fill="#94A3B8"/>', $ax, $ax+7)
    }
  }

  # Footer (critic loop)
  [void]$sb.Append('<rect x="25" y="660" width="1350" height="60" rx="8" fill="#FFF7ED" stroke="#FED7AA"/>')
  [void]$sb.Append('<text x="40" y="682" font-size="11" font-weight="700" fill="#9A3412" letter-spacing="1">CRITIC LOOP</text>')
  [void]$sb.AppendFormat('<text x="135" y="682" font-size="12" fill="#7C2D12">{0}</text>', $w.Critic)
  [void]$sb.AppendFormat('<text x="135" y="702" font-size="11" fill="#9A3412">{0}</text>', $w.CriticSub)

  [void]$sb.Append('</svg>')

  $path = Join-Path $out "$($w.File).svg"
  [System.IO.File]::WriteAllText($path, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))
  Write-Host "Wrote $path"
}
