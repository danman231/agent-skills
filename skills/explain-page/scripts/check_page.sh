#!/usr/bin/env bash
# Render an explainer page with headless Chrome. No other tool is necessary.
# Usage: check_page.sh PAGE.html [OUT_DIR]
# Writes full-height desktop (1280 px), mobile (390 px), and dark-mode screenshots,
# prints each console error, and writes the page text to OUT_DIR/<name>-text.md for ste_check.py.
# Exit code 1 when the page logs an uncaught error.
set -euo pipefail
page="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
out="${2:-$(dirname "$page")/_check}"
mkdir -p "$out"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$chrome" ] || { echo "Google Chrome not found at $chrome" >&2; exit 2; }
name="$(basename "$page" .html)"
here="$(cd "$(dirname "$0")" && pwd)"
flags=(--headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --virtual-time-budget=4000)

# Headless Chrome has a minimum window width of 500 px, so the page goes in an iframe of the
# target width. The wrapper measures the page height so the screenshot shows the whole page.
wrap() { # $1 = iframe width
  local w="$out/.wrap-$1.html"
  cat > "$w" <<HTML
<!doctype html><html><head><style>html,body{margin:0;background:#888}iframe{border:0;display:block;width:$1px;height:2000px}</style></head>
<body><iframe id=f src="file://$page"></iframe><script>
f.onload=()=>{const d=f.contentDocument.documentElement;f.style.height=d.scrollHeight+'px';
document.body.dataset.h=d.scrollHeight;document.body.dataset.sw=d.scrollWidth;};
</script></body></html>
HTML
  echo "$w"
}
measure() { # $1 = wrapper, prints "height scrollWidth"
  "$chrome" "${flags[@]}" --window-size=1280,2000 --dump-dom "file://$1" 2>/dev/null \
    | sed -nE 's/.*data-h="([0-9]+)" data-sw="([0-9]+)".*/\1 \2/p' | head -1
}
shot() { # $1 = iframe width, $2 = label, $3 = optional extra flag
  local w; w=$(wrap "$1")
  read -r h sw <<<"$(measure "$w")"
  h=${h:-2400}; [ "$h" -gt 16000 ] && h=16000
  local win=$(( $1 < 500 ? 500 : $1 ))
  "$chrome" "${flags[@]}" --window-size="$win,$h" ${3:+"$3"} --screenshot="$out/$name-$2.png" "file://$w" >/dev/null 2>&1
  echo "$2: ${1}px wide, page height ${h}px, scrollWidth ${sw:-?}px$([ "${sw:-0}" -gt "$1" ] && echo '  <-- HORIZONTAL OVERFLOW')"
}
shot 1280 desktop
shot 390 mobile
shot 1280 dark --blink-settings=preferredColorScheme=0
rm -f "$out"/.wrap-*.html

"$chrome" --headless=new --disable-gpu --enable-logging=stderr --v=0 --virtual-time-budget=4000 \
  --dump-dom "file://$page" 2>"$out/console.txt" >"$out/.dom.html" || true
python3 "$here/extract_text.py" "$out/.dom.html" "$page" > "$out/$name-text.md"
rm -f "$out/.dom.html"
echo "screenshots: $out/$name-{desktop,mobile,dark}.png"
echo "page text:   $out/$name-text.md  (run ste_check.py on it with --type description)"
errs=$(grep -E 'CONSOLE.*(Uncaught|Error)' "$out/console.txt" | sed -E 's/^.*CONSOLE[^]]*\] //' || true)
if [ -n "$errs" ]; then echo "CONSOLE ERRORS:"; echo "$errs"; exit 1; fi
echo "console: no errors"
