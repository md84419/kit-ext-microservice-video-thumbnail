# Omniverse kit-ext-service-video-thumbnail [robotica.service.video.thumbnail]

An example microservice to produce video thumbnails from videos

# Introduction
We follow a multi-step process to produce a thumbnail video:
1. Extract 256 equally spaced frames from the source video.  If the source isn't at least 256 frames long, some frames will be duplicated.
2. Resize the extracted frames to a maximum of 256x256.  We letterbox or pillarbox to preserve the aspect ratio.

# Getting Started
## Requirements
- NVIDIA Omniverse Launcher
- An Omniverse App (Create, Code, etc)
- Kit 104.1 or later
- Tested with Code 2022.3.3

```
> .\link_app.bat
> .\runbuild.bat
```

# TODO
- [ ]  Eliminate the use of temporary files (this is a limitation of moviepy - it can't currenlty directly read IOBuffers)

# Contributing
The source code for this repository is provided as-is. We only accept outside contributions from individuals who have signed an Individual Contributor License Agreement.
