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
        'views/snippets/blogs.xml',
        'views/snippets/testimonial.xml',
        'views/snippets/snippets.xml',
    ],
    'images': [
        'static/description/cobalt_screenshot.jpg',
    ],
    'assets': {
        'web.assets_frontend': [
            # ==============   For Main Css   ===============
            'theme_tutorial/static/src/css/styles.css',
            'theme_tutorial/static/src/css/common.css',

            # ==============   For All Snippets Css File  ===============
            'theme_tutorial/static/src/css/snippet_css/testimonial.css',

            # ==============   For Snippets Css Files   ===============


            # ==============   For Js   ===============
            'theme_tutorial/static/src/js/dynamic_snippets.js',
        ]
    },
    'license': 'LGPL-3',
}
