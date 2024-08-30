def menus():
    return [
        {
            'name': 'Dashboard',
            'icon': 'bx-home-circle',
            'prefix': '/dashboard/',
            'url': '/dashboard/',
            'type': 0
        },
        {
            'name': 'Category',
            'icon': 'bx-category',
            'prefix': '/category/',
            'url': '/category/',
            'type': 0
        },
        {
            'name': 'Members',
            'icon': 'bx-male',
            'prefix': '/members/',
            'url': '/members/',
            'type': 0
        },
        # {
        #     'name': 'Users',
        #     'icon': 'bx-user',
        #     'type': 1,
        #     'sub_menus': [
        #         {
        #             'name': 'All Users',
        #             'url': 'users.all_users',
        #         }, {
        #             'name': 'Add User',
        #             'url': 'users.add_user',
        #         }
        #     ]

        # }

    ]
