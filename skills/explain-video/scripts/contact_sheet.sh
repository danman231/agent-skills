#!/usr/bin/env bash
# Contact sheet from a rendered MP4: one frame at each given time, or N evenly spaced
# midpoints, in a 3-column grid with the timestamp on each frame.
# Usage: contact_sheet.sh VIDEO.mp4 OUT.png [TIME_SECONDS ...]
#        N=12 contact_sheet.sh VIDEO.mp4 OUT.png      (default N=9)
set -euo pipefail
in="$1"; out="$2"; shift 2
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
if [ $# -eq 0 ]; then
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$in")
  n=${N:-9}
  set -- $(python3 -c "d=$dur;n=$n;print(' '.join(f'{d*(i+0.5)/n:.2f}' for i in range(n)))")
fi
i=0
for t in "$@"; do
  i=$((i+1))
  ffmpeg -v error -y -ss "$t" -i "$in" -frames:v 1 \
    -vf "scale=640:-2,drawtext=text='${t}s':x=10:y=10:fontsize=24:fontcolor=white:box=1:boxcolor=black@0.7" \
    "$tmp/$(printf %03d $i).png"
done
rows=$(( (i + 2) / 3 ))
ffmpeg -v error -y -pattern_type glob -i "$tmp/*.png" -vf "tile=3x$rows:color=white" -frames:v 1 "$out"
echo "contact sheet: $out ($i frames at: $*)"
