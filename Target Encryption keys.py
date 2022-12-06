Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from hashlib import blake2b, blake2s
blake2b(digest_size=10).hexdigest()
'6fa1d8fcfd719046d762'
blake2b(digest_size=11).hexdigest()
'eb6ec15daf9546254f0809'
blake2s(digest_size=10).hexdigest()
'1bf21a98c78a1c376ae9'
blake2s(digest_size=11).hexdigest()
'567004bf96e4a25773ebf4'
