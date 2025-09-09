from rich.console import Console
from time import sleep
console = Console()  

lines = [
    "Together in death, whoa, whoa",
    "Won't you die tonight for love? (Baby, join me in death)",
    "Won't you die? (Baby, join me in death)",  
    "Won't you die tonight for love? (Baby, join me in death)"
]

delays = [0.10, 0.25, 0.30, 0.60, 0.40]

def type_out_pink(text, delay_per_char=0.05):
    for char in text:
        console.print(char, end="", style="bold magenta")  
        sleep(delay_per_char)
    console.print("")  

for line, wait in zip(lines, delays):
    sleep(wait)
    type_out_pink(line, delay_per_char=0.15)