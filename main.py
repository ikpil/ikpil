"""
Very much inspired by the README of the author of rich:
    https://github.com/willmcgugan/willmcgugan
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=150)

tree = Tree("😄 [link=https://github.com/ikpil]Ikpil", guide_style="bold cyan")
packages_tree = tree.add("🐍 Packages")
packages_tree.add("[link=https://github.com/ikpil/DotRecast]DotRecast")
packages_tree.add("[link=https://github.com/ikpil/UniRecast]UniRecast")
packages_tree.add("[link=https://github.com/ikpil/DotFastLZ]DotFastLZ")
packages_tree.add("[link=https://github.com/ikpil/DotCompressorBenchmark]DotCompressorBenchmark")
articles_tree = tree.add("📘 Popular Articles")
articles_tree.add("[link=https://www.ikpil.com/1348]Deadlock Detector")

about = """\
[한국어]
저는 대한민국에서 게임 프로그래머로 활동하고 있는 최익필입니다. 게임 개발시 필요한 필수 요소를 주로 만들고 있어요. 같이 재미있게 만들어요!

[English]
I'm Ikpil, working as a game programmer in South Korea. I mainly focus on creating essential elements required for game development. Let's make games together and have fun!

Follow me on [bold link=https://twitter.com/ikpil]Twitter[/].
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi 👋 I'm Ikpil", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)