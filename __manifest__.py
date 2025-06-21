{
    'name': 'Theme Tutorial',
    'description': 'Theme Tutorial Desc',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/snippets/property_agents.xml',
        'views/snippets/dynamic_products.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_tutorial/static/src/css/styles.css',
            'theme_tutorial/static/src/js/dynamic_snippets.js',
        ]
    },
    'license': 'LGPL-3',
}
