user_route=[
    {
      "name": 'dashboard',
      "path": '/dashboard',
      "component": 'basic',
      "children": [
        {
          "name": 'dashboard_analysis',
          "path": '/dashboard/analysis',
          "component": 'self',
          "meta": {
            "title": '分析页',
            "requiresAuth": True,
            "icon": 'icon-park-outline:analysis'
          }
        }
      ],
      "meta": {
        "title": '仪表盘',
        "icon": 'mdi:monitor-dashboard',
        "order": 1
      }
    },
    {
      "name": 'auth-demo',
      "path": '/auth-demo',
      "component": 'basic',
      "children": [
        {
          "name": 'auth-demo_permission',
          "path": '/auth-demo/permission',
          "component": 'self',
          "meta": {
            "title": '权限切换',
            "requiresAuth": True,
            "icon": 'ic:round-construction'
          }
        }
      ],
      "meta": {
        "title": '权限示例',
        "icon": 'ic:baseline-security',
        "order": 5
      }
    },
    {
      "name": 'multi-menu',
      "path": '/multi-menu',
      "component": 'basic',
      "children": [
        {
          "name": 'multi-menu_first',
          "path": '/multi-menu/first',
          "component": 'multi',
          "children": [
            {
              "name": 'multi-menu_first_second',
              "path": '/multi-menu/first/second',
              "component": 'self',
              "meta": {
                "title": '二级菜单',
                "requiresAuth": True,
                "icon": 'mdi:menu'
              }
            },
            {
              "name": 'multi-menu_first_second-new',
              "path": '/multi-menu/first/second-new',
              "component": 'multi',
              "children": [
                {
                  "name": 'multi-menu_first_second-new_third',
                  "path": '/multi-menu/first/second-new/third',
                  "component": 'self',
                  "meta": {
                    "title": '三级菜单',
                    "requiresAuth": True,
                    "icon": 'mdi:menu'
                  }
                }
              ],
              "meta": {
                "title": '二级菜单(有子菜单)',
                "icon": 'mdi:menu'
              }
            }
          ],
          "meta": {
            "title": '一级菜单',
            "icon": 'mdi:menu'
          }
        }
      ],
      "meta": {
        "title": '多级菜单',
        "icon": 'carbon:menu',
        "order": 7
      }
    },
    {
      "name": 'about',
      "path": '/about',
      "component": 'self',
      "meta": {
        "title": '关于',
        "requiresAuth": True,
        "singleLayout": 'basic',
        "icon": 'fluent:book-information-24-regular',
        "order": 8
      }
    }
  ]