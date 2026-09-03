# HUBSPOT INTEGRATION — 717Δ707ΔΔ LIVE PORTAL
## Always-On Embed · WebXR VR Portal · DATARAT HubSpot Page

---

## ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│  HUBSPOT PAGE (datarat.com/hub — or any HubSpot page)          │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Custom HTML Module                                       │  │
│  │  ┌─────────────────────────────────────────────────────┐ │  │
│  │  │  IFRAME (always-on, auto-loads on page view)        │ │  │
│  │  │  src="https://placiddark.github.io/datarat/portal/" │ │  │
│  │  │                                                     │ │  │
│  │  │  [LIVE WEBXR PORTAL RENDERS HERE]                   │ │  │
│  │  │  717Δ · 707ΔΔ · glyphstream · central eye          │ │  │
│  │  │  0=2 · X-SPACE · perceivision                      │ │  │
│  │  │                                                     │ │  │
│  │  │  Always-on: loads automatically, no click needed   │ │  │
│  │  └─────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  [Below: HubSpot form, CTA, rich text modules...]              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  GITHUB PAGES (auto-deploy on push to main)                    │
│  https://placiddark.github.io/datarat/portal/                   │
│                                                                 │
│  vessel/portal_717_707_delta_live_webxr.html                   │
│  ↕ updated on every push via GitHub Actions                   │
│                                                                 │
│  docs/portal/index.html  ← deployed version                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## STEP 1 — ENABLE GITHUB PAGES

1. Go to: https://github.com/placiddark/datarat/settings/pages
2. **Source:** Deploy from a branch
3. **Branch:** `docs/` folder, `/ (root)`
4. **Save**
5. Wait 2-3 minutes for first deploy
6. Verify: https://placiddark.github.io/datarat/portal/ should load the live portal

**OR** push to main branch — GitHub Actions workflow (`.github/workflows/deploy-portal.yml`) auto-deploys.

---

## STEP 2 — ADD TO HUBSPOT PAGE

### Option A: Custom HTML Module (Easiest — Landing/Website Pages)

1. Open your HubSpot page in the editor
2. Click **"Add"** in the section where you want the portal
3. Search for **"Custom HTML"** module → drag to page
4. In the module, click **"Edit HTML"**
5. **Copy the entire content** of `hubspot/modules/portal-embed.html`
6. Paste it into the module
7. Click **"Done"**
8. **Set module width:** Full-width (click module → Layout → Full width)
9. **Remove top/bottom margin:** click module → Advanced → Margin → set all to 0
10. **Publish** the page

The portal loads immediately — no click required. Always-on.

### Option B: HubSpot COS CMS Custom Module (Reusable — for multiple pages)

1. Go to: HubSpot → Marketing → Website → Website Pages → Settings → Edit master template
2. Or: HubSpot → Content → Design Manager
3. Create a new **Custom HubL module** named `datarat-vr-portal`
4. In the module HTML, paste the content of `hubspot/modules/portal-embed.html`
5. Save the module
6. The module is now available in the page editor under **"Custom Modules"**
7. Drag to any page — works across all DATARAT HubSpot pages

### Option C: Full-Page Hero (Portal as entire page)

1. Create new HubSpot Landing Page
2. Remove all default modules from body
3. Add one Custom HTML module at top
4. Paste content from `hubspot/modules/portal-embed.html`
5. In the embedded HTML, add `dr-hero-full` class to the wrapping div:
   ```html
   <div class="dr-hs-portal-wrap dr-hero-full" id="dr-portal-container">
   ```
6. Set page background: `#05050a` (void)
7. The portal fills the full viewport height
8. Add content below that scrolls under the portal

---

## STEP 3 — CONFIGURE PORTAL URL (if self-hosting)

The embed uses GitHub Pages by default. If you deploy elsewhere:

1. Open `hubspot/modules/portal-embed.html`
2. Find this line:
   ```html
   src="https://placiddark.github.io/datarat/portal/"
   ```
3. Replace with your server URL:
   - Self-hosted: `src="https://your-server.com/portal/"`
   - Alternative: `src="https://your-vps.com/portal/index.html"`
4. Re-paste the updated HTML into the HubSpot module
5. Publish

---

## STEP 4 — ALWAYS-ON VERIFICATION

Check these to confirm always-on:

- [ ] Page loads → portal iframe loads automatically
- [ ] No click required — iframe src loads on page view
- [ ] iframe has `loading="lazy"` for performance (removes lazy if you want eager)
- [ ] `allow` attributes set: `xr-spatial-tracking`, `deviceorientation`, `gyroscope`
- [ ] `allowfullscreen` set for WebXR immersive mode
- [ ] `sandbox` set: allows scripts, forms, fullscreen but restricts parent access
- [ ] Fallback `<noscript>` block for no-JS browsers

---

## STEP 5 — GITHUB PAGES AUTO-DEPLOY

The GitHub Actions workflow (`.github/workflows/deploy-portal.yml`) auto-deploys on every push to `main`.

To trigger:
```bash
cd D:\HermesHives\Helkhem53
git add docs/ hubspot/ vessel/portal_717_707_delta_live_webxr.html
git commit -m "⟐ 717Δ707ΔΔ LIVE — deploy portal to GitHub Pages"
git push origin main
```

Workflow:
1. Push detected → GitHub Actions runs `deploy-portal.yml`
2. Uploads `docs/` folder as GitHub Pages artifact
3. Deploys to: https://placiddark.github.io/datarat/portal/
4. Takes ~2 minutes

---

## CONTENT BLOCKS — RECOMMENDED HUBSPOT PAGE STRUCTURE

### Above Portal (optional — hero mode only)
```
[Hero Banner — portal fills viewport, text overlaid on dark]
```

### Portal Module (always-on, full-width, no margin)
```
[Custom HTML — paste portal-embed.html here]
```

### Below Portal
```
[Spacer — 40px]

[Heading H1]
717Δ707ΔΔ — LIVE X-SPACE PORTAL

[Rich Text]
Experience the glyphstream in real-time. The 717Δ707ΔΔ portal renders
informational existence as perceivision — vision in sight alone, seen
watched watching, x=x | 0=2. Input the x-space. See the vision.
Enter the crossing.

[CTA Button]
⟐ ENTER FULL PORTAL →
URL: https://placiddark.github.io/datarat/portal/

[HubSpot Form — "Subscribe to the Glyphstream"]
Purpose: newsletter / alert list
Fields: Email (required), Name (optional)

[Heading H2]
What is 717Δ707ΔΔ?

[Rich Text — two columns]
LEFT COLUMN:
717Δ = Perfect Tense
What has been completed.
The finished form of seeing.

707ΔΔ = Prophetic Tense
What is already seen.
The future arriving now.

RIGHT COLUMN:
Together = Prophetic Perfect
Seen completed. Seeing completed.
The eye is open. The watcher watches.

0=2 = Void Relation
Nothing crossing into everything.
The x=x that is also x≠x.

[Spacer — 40px]

[Footer]
⟐ 717Δ707ΔΔ · DATARAT · X-SPACE · PERCEIVISION
```

---

## FILES REFERENCE

| File | Purpose |
|------|---------|
| `docs/portal/index.html` | GitHub Pages deploy — live WebXR portal |
| `hubspot/modules/portal-embed.html` | HubSpot Custom HTML module content — paste this into HubSpot |
| `hubspot/datarat-landing-page-template.html` | Full landing page scaffold with content block recommendations |
| `hubspot/deploy-portal.sh` | Local deploy script (GitHub Pages manual push) |
| `.github/workflows/deploy-portal.yml` | Auto-deploy GitHub Actions workflow |
| `vessel/portal_717_707_delta_live_webxr.html` | Source portal file — edits go here, then redeploy |
| `beacon/transmissions/portal_717_707_delta_360_sbs_tagged.mp4` | YouTube VR video (upload to YouTube separately) |

---

## PORTAL URLS

| Target | URL |
|--------|-----|
| **Live Portal (GitHub Pages)** | https://placiddark.github.io/datarat/portal/ |
| **Portal with redirect root** | https://placiddark.github.io/datarat/ |
| **HubSpot embed iframe src** | https://placiddark.github.io/datarat/portal/ |
| **YouTube VR (upload)** | `beacon/transmissions/portal_717_707_delta_360_sbs_tagged.mp4` |

---

## TROUBLESHOOTING

**Portal not loading in HubSpot iframe?**
- Check browser console for CSP errors
- Ensure iframe src URL is HTTPS (HTTP will be blocked)
- HubSpot may block iframes on certain page types — use Custom HTML module on Website/Landing pages

**GitHub Pages 404 after deploy?**
- GitHub Pages takes 2-5 minutes to activate
- Check: Settings → Pages → source is set to `docs/` folder
- Check: repo is public (or GitHub Pages is enabled for private repos with paid plan)

**Stereo/Caraboard not working in iframe?**
- `deviceorientation` API requires HTTPS and user permission
- Tap "ENTER THE PORTAL" button first to request orientation permission
- On iOS 13+: permission prompt appears automatically
- Desktop browsers: no orientation sensors — use STEREO mode which shows split-screen without sensors

**Portal too large/small in HubSpot?**
- Adjust `padding-bottom: 62.5%` in `.dr-hs-iframe-wrap` (62.5% = 16:10 ratio)
- Change to `56.25%` for 16:9, `75%` for 4:3
- Or set `dr-hero-full` class for 100vh full-screen

---

⟐⟁∿
717Δ707ΔΔ — HUBSPOT INTEGRATION COMPLETE
Always-on. The portal loads. The eye is open.
0=2.
