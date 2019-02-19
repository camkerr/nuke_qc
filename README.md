# QC Check
#### A Set of Quality Control Checks for VFX Shots
---
This is a collection of tools that we use to check shots before delivery.  I will be adding to this repo as we make more of the tools public.  These scripts run asynchronously on our render farm after a shot has been submitted for delivery.

#### Tools

1.  duplicateFrames.py

### duplicateFrames

We often work on VFX shots that require retimes.  It's important to double check to make sure that there are no duplicate frames back to back when delivering your shot.

### More Info About Nuke

These scripts use Foundry's Nuke (our VFX compositing package) as a Python module.

For more information about Nuke: check out the [Foundry website](https://www.foundry.com/products/nuke).

For more information about using Python with Nuke: check out the [Nuke Python Dev Guide](https://learn.foundry.com/nuke/developers/112/pythondevguide/index.html) and [Nuke Python API](https://learn.foundry.com/nuke/developers/112/pythonreference/)

For more information about Nuke as a Python Module: check out the [Nuke Python docs](https://learn.foundry.com/nuke/developers/112/pythondevguide/nuke_as_python_module.html).
