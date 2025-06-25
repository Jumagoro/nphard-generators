"""Simple sandbox. Can be overwritten any time"""


def test(**kwargs):
    comments = kwargs.get("comments") or []
    for b in comments:
        print("T")

test()
