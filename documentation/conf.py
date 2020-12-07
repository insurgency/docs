import sys

from datetime import datetime

# Main Settings

author = 'insurgency.gg'
autodoc_member_order = 'bysource'
# noinspection PyShadowingBuiltins
copyright = f'{datetime.now().year}, {author}'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    # See: https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
    # See: https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.linkcode',
]
html_static_path = ['_static']
html_theme = 'alabaster'
nitpicky = True
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']

# Extension Settings

intersphinx_mapping = {
    'py': ('https://docs.python.org/{0.major}.{0.minor}'.format(sys.version_info), None),
}
extlinks = {
    # GitHub
    'github-branch':    ('https://github.com/insurgency/aioa2squery/tree/branches/%s',  'name'),
    'issue':            ('https://github.com/insurgency/aioa2squery/issues/%s',         'gh-'),

    # Steam
    'steam-app':        ('https://store.steampowered.com/app/%s',                       'app-id'),
    'steam-support':    ('https://support.steampowered.com/kb_article.php?ref=%s',      'ref'),

    # Wikis
    'valve-wiki':       ('https://developer.valvesoftware.com/wiki/%s',                 'page'),
    'insurgency-wiki':  ('https://insurgency.fandom.com/wiki/%s',                       'page'),
}
# Wikis
extlinks.update(dict.fromkeys(['wiki', 'wikipedia'], ('https://wikipedia.org/wiki/%s', 'page')))

# Conditional Settings

try:
    # noinspection PyPackageRequirements
    import django
except ImportError:
    pass
else:
    extensions.append('djangodocs')

    value = ('https://docs.djangoproject.com/en/stable/', 'https://docs.djangoproject.com/en/stable/_objects/')
    # noinspection PyTypeChecker
    intersphinx_mapping.update(dict.fromkeys(['dj', 'django'], value))

try:
    # noinspection PyPackageRequirements
    import redis
except ImportError:
    pass
else:
    value = ('https://redis-py.readthedocs.io/en/stable/', None)
    intersphinx_mapping.update(dict.fromkeys(['redis', 'redis-py'], value))

try:
    import sphinxcontrib.programoutput
except ImportError:
    pass
else:
    extensions.append('sphinxcontrib.programoutput')

try:
    import sphinx_autodoc_typehints
except ImportError:
    pass
else:
    # See: https://github.com/agronholm/sphinx-autodoc-typehints#installation-and-setup
    extensions.append('sphinx_autodoc_typehints')

try:
    # noinspection PyPackageRequirements
    import yarl
except ImportError:
    pass
else:
    intersphinx_mapping['yarl'] = ('https://yarl.rtfd.io/en/stable/', None)

try:
    # noinspection PyPackageRequirements
    import aiohttp
except ImportError:
    pass
else:
    intersphinx_mapping['aiohttp'] = ('https://docs.aiohttp.org/en/stable/', None)
