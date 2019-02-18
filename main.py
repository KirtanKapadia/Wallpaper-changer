import UnsplashWallpaper, DesktopWallpaper




api_key = '5dfe97f1d0fac9b501aaf462244cff5d8b993581c28337e8382ac158dc77c939'
client_id = '5dfe97f1d0fac9b501aaf462244cff5d8b993581c28337e8382ac158dc77c939'
client_secret = '1f4c6dbecc92dc0ef493f80413e1fb6a513aeee29962310e14789af8ee35b19e'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
code = '404daa4c075643d17d0532374ad512baff309f5f1bd29780b38897e8c41331ed'
path = ''

wall = UnsplashWallpaper.UnsplashWallpaper(api_key, client_id, client_secret, redirect_uri, code,path)
wall.get_link()
