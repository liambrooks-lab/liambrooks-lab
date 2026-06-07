import urllib.request
def fetch(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {dest}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

fetch('https://capsule-render.vercel.app/api?type=rect&color=0:050816,50:0b132b,100:123c69&height=220&section=header&text=Rudranarayan%20Jena&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=Founder%20%40%20Voxion%20Labs%20%7C%20Aspiring%20Data%20Scientist%20%26%20AI%20Engineer%20%7C%20System%20Builder&descAlignY=64&descSize=18', 'e:/Projects/liambrooks-lab/assets/header_banner.svg')
fetch('https://github-readme-stats.vercel.app/api?username=liambrooks-lab&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true', 'e:/Projects/liambrooks-lab/assets/github-stats.svg')
fetch('https://github-readme-stats.vercel.app/api/top-langs/?username=liambrooks-lab&layout=compact&theme=tokyonight&hide_border=true&langs_count=8', 'e:/Projects/liambrooks-lab/assets/top-langs.svg')
fetch('https://github-readme-activity-graph.vercel.app/graph?username=liambrooks-lab&bg_color=0d1117&color=58a6ff&line=1f6feb&point=58a6ff&area=true&hide_border=true', 'e:/Projects/liambrooks-lab/assets/activity-graph.svg')
