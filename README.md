# 妖zon.com
妖怪ウォッチに出てくる[**妖zon.com**](妖zon.com)のオマージュ  
アニメの内容を完全に忘れているので完全な再現はできてないかもしれない
## なぜPHPじゃなくてPythonなのか
こっちのほうが書きやすいし、WebSocketも使えるから
## How to Build
Require: Python >= 3.10
```
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 80
```
(Linuxの人はuvicornコマンドを別途インストールしてください)
