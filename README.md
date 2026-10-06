# Keyball61 — Mac / Windows 配列設計

**実機構成確認待ちの設計リポジトリです。書き込み可能な完成ファームウェアではありません。**

無線 ZMK Keyball61 を Mac 優先で使い、Windows にも同じ指使いで切り替えるための独自配列案です。別機体の Microball 設定は使用していません。

## 配列案

`examples/mac-win.keymap` は US 配列を仮定した候補です。実機の matrix transform と一致すると確認するまで `config/` に移さないでください。各層は 61 キー、行ごとの並びは 12 / 12 / 12 / 14 / 11 です。最後の行には親指以外の下段キーも含みます。

| 操作 | 設計 |
| --- | --- |
| 通常入力 | QWERTY、通常数字段、Mac を起動時の配列にする |
| ショートカット | 下段左から3番目を Mac Command / Windows Ctrl にする。左端は Mac Ctrl / Windows GUI |
| Fn | 下段左から9番目を押している間。最上段は左から F1–F12 |
| メディア | Fn + Q/W/E = 前曲/再生停止/次曲、Fn + A/S/D = 消音/音量下/音量上 |
| Mac 選択 | Fn + M：BT profile 0 + BLE 出力 + Mac 配列 |
| Windows 選択 | Fn + N：BT profile 1 + BLE 出力 + Windows 配列 |
| USB 出力 | Fn + U：配列を保ったまま USB 出力。Mac/Win 選択は再び BLE を選ぶ |
| 記号 | 下段左から4番目を押している間。US 記号・括弧 |
| ナビゲーション | Fn + H/J/K/L = 左/下/上/右 |

OS 選択は明示的なマクロです。OS 自動検出ではありません。切替時は入力・修飾キーを離し、Fn と選択キーだけで操作してください。再起動後は Mac 配列に戻りますが、ZMK の BT profile 選択は保存されるため、**再起動後にも利用する OS の選択キーを押してください**。接続先側の準備ができていなくても配列は変わり、接続成功を保証するトランザクションではありません。profile 0/1 は提案であり、既存ペアリングとの対応確認が必要です。

## トラックボールは統合待ち

候補内の層4/5/6は MOUSE / SCROLL / SNIPE 用に予約しています。MOUSE 層にマウスボタンの例はありますが、センサー、配線、ドライバー、スクロール/低速化/自動マウス層は未設定です。SCROLL と SNIPE は現在透明なプレースホルダーであり、球の動作は変えません。

実機対応元を確定したら、そのドライバー、ピン、回転、CPI、スクロール、低速化、画面設定を維持し、層番号との参照を照合します。**現在の実機操作を維持できることはまだ検証できていません。** ペアリング消去・リセット・ブートローダー呼出しは候補配列に配置していません。

## 確認してほしい情報

無線化キット名または購入/設定元 URL を教えてください。そこから MCU、基板/配線、センサー、球の左右、画面、central 側を確認します。併せて Mac と Windows で US / JIS のどちらを使うか確認が必要です。

## 参考候補・出典

| 公開元 | 確認した構成 | 状態 |
| --- | --- | --- |
| [tangbonze/zmk-config-Keyball61](https://github.com/tangbonze/zmk-config-Keyball61) | main: nice_nano_v2、keyball61_left/right、ZMK v0.3、PMW3610。OLED と nice!view 等に分岐 | 実機適合未確認 |
| [mochukeeb/zmk-config-keyball61](https://github.com/mochukeeb/zmk-config-keyball61) | niceview: nice_nano_v2、nice_view、PMW3610。oled は別分岐 | 実機適合未確認 |
| [superxc3/zmk-config-Keyball61](https://github.com/superxc3/zmk-config-Keyball61) | 調査候補 | 未採用 |

調査時の参照コミット: tangbonze/main `57306efff1642fc6a6f4e3312a19e832bb232543`、mochukeeb/niceview `c493cbaa014e9763ba898f29e2e24f32e8452e49`。

上記2候補の GitHub licenseInfo は未指定、確認したツリーに LICENSE はありませんでした。上流の利用条件を推定してコードを取り込まず、このリポジトリは独立作成しています。fork 元・採用済みハードウェア設定はありません。将来取り込む場合は出典、原著者の帰属、適用ライセンスを保持します。

ZMK 公式資料: [macros](https://zmk.dev/docs/keymaps/behaviors/macros)、[layers](https://zmk.dev/docs/keymaps/behaviors/layers)、[Bluetooth](https://zmk.dev/docs/keymaps/behaviors/bluetooth)、[output](https://zmk.dev/docs/keymaps/behaviors/outputs)。

## 検証と今後

`python3 scripts/check_layout.py` でキー数、主要キー、切替マクロ、危険操作の不在を静的確認できます。CI は GitHub 標準 `ubuntu-latest` runner の静的確認のみで、インストール処理はありません。

ZMK/Zephyr コンパイル、実機入力、トラックボール、BLE/USB 切替は未検証です。board/shield/west.yml/build.yaml は実機特定後に追加します。候補ファイルだけでファームウェアをビルドすることはできません。
