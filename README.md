# DemonZ: Echoes of the Forgotten - Prototype (GitHub repo)

This repository contains a Ren'Py visual novel prototype prepared for DemonZ Development,
optimized assets, and a GitHub Actions workflow to build Android artifacts on push.

## Contents
- `game/` - Ren'Py project files (images, audio, script.rpy)
- `.github/workflows/renpy-android.yml` - CI workflow to build Android package on Ubuntu runners.

## Quick start (on Android or desktop)
1. Clone this repo locally: `git clone https://github.com/<yourname>/demonz-proto.git`
2. Edit the `game/` assets or scripts as needed.
3. Push to GitHub.
4. GitHub Actions will run on push to `main` and create build artifacts.

## GitHub Secrets (for signed builds)
To produce signed APK/AABs, add these repository secrets:
- `RENPY_KEYSTORE_BASE64` — base64 of your release keystore (optional; blank builds unsigned).
- `RENPY_KEYSTORE_PASSWORD`
- `RENPY_KEY_ALIAS`
- `RENPY_KEY_PASSWORD`

To create the base64 keystore value locally:
```
base64 -w 0 my-release-key.jks
```
Paste the output into the `RENPY_KEYSTORE_BASE64` secret.

## Notes
- The workflow installs Ren'Py, Android SDK/NDK and attempts to build an Android package.
- If you only want assets, remove the workflow.
- For fast iteration on Android devices, edit files in the `game/` folder and push changes.

Enjoy — DemonZ Development
