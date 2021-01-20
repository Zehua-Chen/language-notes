# Overview

Platform detections can be done at compile-time using macros

- Apple Platforms: `__APPLE__`
- Windows:
  - `_WIN32`: x86, x64, 32-bit ARM, 64-bit ARM
  - `_WIN64`: x64, 64-bit ARM
- Linux: `__linux__`
- Android: `__ANDROID__`
