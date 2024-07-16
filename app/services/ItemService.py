import random

from ..objects import Item, ItemTypes


class ItemService:
    items = [
        Item(
            id=0,
            name="妖怪ウォッチ",
            type=ItemTypes.WATCH,
            price=11000,
            summary="素晴らしい腕時計",
            description="メダルを読み込むと妖怪を呼び出すことができます。",
            image="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR4AvhuVcnuED5wBp3sojsOt68MKkTlFm-F1HMeecBomv1Qf3Qb-Y6k2DdwoexPCbaAYUF8n5LroX9KxEN64PMTu5iihEDv1J2qGTt59qk",
        ),
        Item(
            id=1,
            name="妖怪ウォッチドリーム",
            type=ItemTypes.WATCH,
            price=15000,
            summary="もっと素晴らしい腕時計",
            description="メダルを読み込むと妖怪を呼び出すことができます。読み込める妖怪の種類が増えています。",
            image="https://m.media-amazon.com/images/I/71eDkBtSWOL.__AC_SX300_SY300_QL70_ML2_.jpg",
        ),
        Item(
            id=2,
            name="ウィスパー",
            type=ItemTypes.MEDAL,
            price=0,
            summary="知ったかぶり",
            description="知ったかぶりの執事",
            image="https://www.youkai-watch.jp/yw/images/special/character.png",
        ),
        Item(
            id=3,
            name="ジバニャン",
            type=ItemTypes.MEDAL,
            price=5000,
            summary="妖怪ウォッチの顔",
            description="地縛霊",
            image="https://www.tv-tokyo.co.jp/anime/youkai-watch/sp/images/chara/sp06.jpg",
        ),
        Item(
            id=4,
            name="妖怪ウォッチ2",
            type=ItemTypes.SOFTWARE,
            price=20140710,
            summary="2014年7月10日(真打は12月13日)に販売された幻の神ゲー",
            description="伝説のゲームソフト",
            image="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS-75AJkHS_0QwWQ7aJj6ym6EG9w6FDLfdXYXP84j7NVN_rSFqa4NvRBNeeW3LQ56z2nqtgvgj3up0y7NgwuUCBfsCdptKVjzi7d3J2Fw",
        ),
        Item(
            id=5,
            name="妖怪パッド",
            type=ItemTypes.ITEM,
            price=5000,
            summary="知ったかぶりが使ってそうな板",
            description="RAM: 64MB ストレージ: 1GB",
            image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYzigQQXA9nqeZ0FQ8qWDMPNP9feHf7oWRa_gzVXkpCnpy7yItc-K6QcW2&s=10",
        ),
    ]

    @classmethod
    def getItems(cls, length):
        random.shuffle(cls.items)
        return cls.items[:length]
