import math
import os
import sys
import time

# Rotation angles for the torus
A = 0.0
B = 0.0

# Clear screen once at the beginning
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('\x1b[2J')

try:
    while True:
        # Initialize z-buffer (depth buffer) and output buffer (frame buffer)
        z = [0.0] * 1760
        b = [' '] * 1760

        # j goes from 0 to 2pi (theta - circle around the tube)
        j = 0.0
        while j < 6.28:
            # i goes from 0 to 2pi (phi - circle around the spin axis)
            i = 0.0
            while i < 6.28:
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                
                # Depth calculation
                D = 1.0 / (c * h * e + f * g + 5.0)
                
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e

                # 2D projection coordinates mapped to 80x22 terminal layout
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)

                # Luminance calculation (shading index)
                N = int(
                    8
                    * (
                        (f * e - c * d * g) * m
                        - c * d * e
                        - f * g
                        - l * d * n
                    )
                )

                # Check boundaries and depth buffer
                if 0 <= o < 1760:
                    if D > z[o]:
                        z[o] = D
                        # Choose ASCII character based on luminance
                        b[o] = '.,-~:;=!*#$@'[N if N > 0 else 0]

                i += 0.02
            j += 0.07

        # Render frame
        sys.stdout.write('\x1b[H')
        output = []
        for k in range(1761):
            if k % 80:
                output.append(b[k - 1])
            else:
                output.append('\n')

        sys.stdout.write(''.join(output))
        sys.stdout.flush()

        # Increment rotation angles
        A += 0.04
        B += 0.02

        # Control frame rate (~30fps)
        time.sleep(0.03)

except KeyboardInterrupt:
    sys.exit()
