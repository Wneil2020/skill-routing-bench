---
name: anthropic-slack-gif-creator
description: "Use when Create animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for: covers anthropic, slack, gif, GIF, 슬랙 GIF"
metadata:
  holon-triggers: |
    make me a GIF of X doing Y for Slack.
    users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."
---

---
name: anthropic-slack-gif-creator
description: >-
  Create animated GIFs optimized for Slack. Provides constraints, validation
  tools, and animation concepts. Use when users request animated GIFs for Slack
  like "make me a GIF of X doing Y for Slack." Do NOT use for static image
  creation (use anthropic-canvas-design) or general Slack messaging (use
  kwp-slack-slack-messaging). Korean triggers: "GIF", "슬랙 GIF", "애니메이션".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Complete terms in LICENSE.txt"
  category: "document"
---
# Slack GIF Creator

A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack.

## Slack Requirements

**Dimensions:**
- Emoji GIFs: 128x128 (recommended)
- Message GIFs: 480x480

**Parameters:**
- FPS: 10-30 (lower is smaller file size)
- Colors: 48-128 (fewer = smaller file size)
- Duration: Keep under 3 seconds for emoji GIFs

## Core Workflow

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)

    # Draw your animation using PIL primitives
    # (circles, polygons, lines, etc.)

    builder.add_frame(frame)

# 3. Save with optimization
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Drawing Graphics

### Working with User-Uploaded Images
If a user uploads an image, consider whether they want to:
- **Use it directly** (e.g., "animate this", "split this into frames")
- **Use it as inspiration** (e.g., "make something like this")

Load and work with images using PIL:
```python
from PIL import Image

uploaded = Image.open('file.png')
# Use directly, or just as reference for colors/style
```

### Drawing from Scratch
When drawing graphics from scratch, use PIL ImageDraw primitives:

```python
from PIL import ImageDraw

draw = Imag
