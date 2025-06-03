from django.shortcuts import render

def second(request):
    # 예: 상품 데이터 (DB에서 가져온다고 가정)
    products = [
        {
            'category': 'PEN',
            'name': 'FX ZETA C3',
            'image': 'https://dfrkkcv2hg1jc.cloudfront.net/data/main/file1_1699945409grwui60w6u.jpg',
            'link': 'http://www.monami.com/product/product_view.php?ccode=005002&idx=188'
        },
        {
            'category': 'NOTE',
            'name': '지퀀스',
            'image': 'https://dfrkkcv2hg1jc.cloudfront.net/data/main/file1_169994521784nzg4whv7.jpg',
            'link': 'http://www.monami.com/product/product_view.php?ccode=001005&idx=186'
        },
        # 추가 상품들...
    ]
    return render(request, 'second.html', {'products': products})


def test(request):
    return render(request, 'test.html', {
        'monami_title': 'Monami',
        'sns_links': [
            {'link': 'https://www.facebook.com/monami1960', 'img': '/images/sns_facebook.gif'},
            {'link': 'https://www.instagram.com/monami_official/', 'img': '/images/sns_insta.gif'},
            {'link': 'https://www.youtube.com/channel/UC7lJDw-5bYXnAGNHh1uUG3A', 'img': '/images/sns_youtube.gif'},
        ]
    })
