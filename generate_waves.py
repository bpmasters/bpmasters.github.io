import math

svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 1000" preserveAspectRatio="none">']

# Draw several overlapping, wavy lines to look like an oscilloscope or sound wave
colors = ["#57068c", "#57068c", "#57068c", "#57068c"]
opacities = ["0.08", "0.06", "0.05", "0.04"]

for i in range(4):
    path = []
    for y in range(0, 1001, 10):
        # Base sine wave + some higher frequency harmonics
        freq1 = 0.005 + i * 0.001
        freq2 = 0.02 + i * 0.005
        
        # Swell in the middle
        envelope = math.sin(math.pi * (y / 1000))
        
        # X position oscillates around a center line
        center = 30 + i * 15
        amplitude = 20 + i * 10
        
        x = center + envelope * amplitude * (math.sin(y * freq1) + 0.5 * math.sin(y * freq2))
        
        if y == 0:
            path.append(f"M {x},{y}")
        else:
            path.append(f"L {x},{y}")
            
    svg.append(f'<path d="{" ".join(path)}" fill="none" stroke="{colors[i]}" stroke-width="{1.5 + i*0.5}" stroke-opacity="{opacities[i]}" />')

svg.append('</svg>')

with open('assets/images/bg-waves.svg', 'w') as f:
    f.write("\n".join(svg))
