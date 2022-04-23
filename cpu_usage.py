#!/usr/bin/env python
import psutil

# gives a single float value
cpu = psutil.cpu_percent(1)

# gives an object with many fields
ram = psutil.virtual_memory()

print(f"CPU: {cpu}, RAM: {ram}")
