# Nuke Duplicate Frame QC Check
#### An in-house Quality Control Check for VFX Shots to Detect Duplicate Frames
---
We often work on VFX shots that require retimes.  It's important to double check to make sure that there are no duplicate frames back to back when delivering your shot.  This script runs on our render farm when a shot is submitted for review and will notify the VFX Coordinator if it fails QC.

This script uses Foundry's Nuke (our VFX compositing package) as a Python module.

For more information about Nuke: check out the [Foundry website](https://www.foundry.com/products/nuke).

For more information about using Python with Nuke : check out the [Nuke Python Dev Guide](https://learn.foundry.com/nuke/developers/112/pythondevguide/index.html) and [Nuke Python API](https://learn.foundry.com/nuke/developers/112/pythonreference/)

For more information about Nuke as a Python Module: check out the [Nuke Python docs](https://learn.foundry.com/nuke/developers/112/pythondevguide/nuke_as_python_module.html).
