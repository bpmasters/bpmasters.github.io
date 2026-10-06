import random
import math

svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 2000" preserveAspectRatio="xMinYMid slice">']
svg.append('<defs><linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#57068c" stop-opacity="0.06"/><stop offset="100%" stop-color="#57068c" stop-opacity="0.0"/></linearGradient>')
svg.append('<linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#57068c" stop-opacity="0.03"/><stop offset="100%" stop-color="#57068c" stop-opacity="0.0"/></linearGradient></defs>')

# Smooth continuous waveform (like a heartbeat / oscilloscope)
path1 = ["M 0,0"]
path2 = ["M 0,0"]
path3 = ["M 0,0"]

for y in range(0, 2001, 20):
    env = math.sin(math.pi * (y / 2000))
    # Layer 1
    w1 = 50 + env * 150 + math.sin(y * 0.01) * 30 + random.random() * 20
    path1.append(f"L {w1},{y}")
    # Layer 2
    w2 = 20 + env * 100 + math.sin(y * 0.015 + 1) * 40 + random.random() * 10
    path2.append(f"L {w2},{y}")
    # Layer 3
    w3 = 10 + env * 250 + math.sin(y * 0.005 + 2) * 50 + random.random() * 15
    path3.append(f"L {w3},{y}")

path1.append("L 0,2000 Z")
path2.append("L 0,2000 Z")
path3.append("L 0,2000 Z")

svg.append(f'<path d="{" ".join(path3)}" fill="url(#grad2)" />')
svg.append(f'<path d="{" ".join(path1)}" fill="url(#grad1)" />')
svg.append(f'<path d="{" ".join(path2)}" fill="url(#grad1)" />')

svg.append('</svg>')

with open('assets/images/bg-waves.svg', 'w') as f:
    f.write("\n".join(svg))
