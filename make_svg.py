import base64, urllib.request

URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP4MtA-NQihxf7xkBu2iJ2Gqnptq5dc1kZ5Op7mH-F3A&s=10"
W, H = 250, 250  # display size; change to match your image's proportions

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
data = base64.b64encode(urllib.request.urlopen(req).read()).decode()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <image href="data:image/jpeg;base64,{data}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none">
    <animate attributeName="x"
             values="0;0;{W};0;0;0"
             keyTimes="0;0.25;0.5;0.5;0.75;1"
             dur="4s" repeatCount="indefinite"/>
    <animate attributeName="width"
             values="0;{W};0;0;{W};0"
             keyTimes="0;0.25;0.5;0.5;0.75;1"
             dur="4s" repeatCount="indefinite"/>
  </image>
</svg>'''

open("jotchua.svg", "w").write(svg)
print("Wrote jotchua.svg")
