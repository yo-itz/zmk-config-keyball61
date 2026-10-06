"""Static design checks only; not a Devicetree or firmware compiler."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "examples/mac-win.keymap").read_text()
layers = dict(re.findall(r"(\w+)_layer\s*\{.*?bindings\s*=\s*<(.*?)>;", text, re.S))
assert list(layers) == ["mac", "windows", "fn", "symbols", "mouse", "scroll", "snipe"]
parsed = {}
for name, body in layers.items():
    rows = [re.findall(r"&\w+(?:\s+[^&\n]+)?", row) for row in body.strip().splitlines()]
    rows = [[binding.strip() for binding in row] for row in rows]
    assert [len(row) for row in rows] == [12, 12, 12, 14, 11], name
    parsed[name] = rows
for name in ("mac", "windows"):
    assert parsed[name][0][1:11] == [f"&kp N{i % 10}" for i in range(1, 11)]
    assert parsed[name][4][8] == "&mo FN"
assert parsed["mac"][4][2] == "&kp LGUI"
assert parsed["windows"][4][2] == "&kp LCTRL"
assert parsed["fn"][0] == [f"&kp F{i}" for i in range(1, 13)]
assert parsed["fn"][3][8:10] == ["&select_windows", "&select_mac"]
for profile, layer in ((0, "MAC"), (1, "WINDOWS")):
    assert f"&bt BT_SEL {profile} &out OUT_BLE &to {layer}" in text
assert not re.search(r"\bBT_CLR(?:_ALL)?\b|&(?:reset|bootloader)\b", text)
assert not list(root.glob("build.yaml")), "Hardware target must be explicitly reviewed first"
print("PASS: 7 x 61 bindings, number/F-key rows, shortcut positions, OS/profile macros, no reset bindings")
print("NOT VERIFIED: compilation, matrix mapping, hardware, trackball, runtime switching")
