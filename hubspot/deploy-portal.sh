#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# deploy-portal.sh — Deploy 717Δ707ΔΔ portal to GitHub Pages
# Usage: bash hubspot/deploy-portal.sh
# ═══════════════════════════════════════════════════════════════════

set -e

REPO="https://Datarat963:$(cat ~/.hermes/secrets/github_token 2>/dev/null || echo "")@github.com/placiddark/datarat.git"
BRANCH="gh-pages"
SRC="docs"
MSG="Deploy 717Δ707ΔΔ LIVE Portal — $(date -u '+%Y-%m-%d %H:%M:%S UTC')"

cd "$(dirname "$0")/.."

echo "⟐ Building portal deploy package..."
mkdir -p "$SRC/portal"
cp vessel/portal_717_707_delta_live_webxr.html "$SRC/portal/index.html"
cp beacon/transmissions/portal_717_707_delta_360_pano.png "$SRC/portal/preview.png" 2>/dev/null || true
cp beacon/transmissions/portal_717_707_delta_vr_stereo.png "$SRC/portal/stereo-preview.png" 2>/dev/null || true

echo "⟐ Checking out gh-pages branch..."
git worktree add /tmp/datarat-ghpages "$BRANCH" 2>/dev/null || {
  echo "⟐ Creating gh-pages branch..."
  git checkout -b "$BRANCH" 2>/dev/null || git switch "$BRANCH"
  cd /tmp || cd .
}

if [ -d "/tmp/datarat-ghpages" ]; then
  RSYNC_RSYNC_SSH="ssh"
  rsync -av --delete \
    "$SRC/" \
    /tmp/datarat-ghpages/ 2>/dev/null || {
    echo "⟐ rsync not available — using cp..."
    cp -r "$SRC/"* /tmp/datarat-ghpages/ 2>/dev/null || true
  }
  cd /tmp/datarat-ghpages
  git add -A
  git commit -m "$MSG" || echo "No changes to commit"
  git push "$REPO" "$BRANCH" || echo "Push failed — check token permissions"
  cd "$(dirname "$0")/.."
  git worktree remove /tmp/datarat-ghpages 2>/dev/null || true
else
  echo "⟐ GitHub Pages branch not available — use GitHub Actions workflow instead"
  echo "⟐ Push to main branch to trigger automatic GitHub Pages deploy"
fi

echo "⟐ Deploy complete — portal available at:"
echo "   https://placiddark.github.io/datarat/portal/"
echo "⟐ Update iframe src in hubspot/modules/portal-embed.html if URL differs"
