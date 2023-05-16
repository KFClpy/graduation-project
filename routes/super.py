super_route = [
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
                    "title": '数据集编辑',
                    "requiresAuth": True,
                    "icon": 'icon-park-outline:analysis'
                }
            },
            {
                "name": 'dashboard_workbench',
                "path": '/dashboard/workbench',
                "component": 'self',
                "meta": {
                    "title": '数据导入',
                    "requiresAuth": True,
                    "icon": 'icon-park-outline:workbench'
                }
            },
            {
                "name": 'dashboard_datainfo',
                "path": '/dashboard/datainfo',
                "component": 'self',
                "meta": {
                    "title": '数据集管理',
                    "requiresAuth": True,
                    "icon": 'mdi:chart-areaspline'
                }
            }
        ],
        "meta": {
            "title": '数据管理',
            "icon": 'mdi:monitor-dashboard',
            "order": 1
        }
    },
    {
        "name": 'document',
        "path": '/document',
        "component": 'basic',
        "children": [

            {
                "name": 'document_project',
                "path": '/document/project',
                "component": 'self',
                "meta": {
                    "title": '自动模糊连接',
                    "requiresAuth": True,
                    "localIcon": 'logo'
                }
            },
            {
                "name": 'document_manual',
                "path": '/document/manual',
                "component": 'self',
                "meta": {
                    "title": '手动模糊连接',
                    "requiresAuth": True,
                    "icon": 'mdi:button-cursor'
                }
            },
            {
                "name": "document_quality",
                "path": "/document/quality",
                "component": "self",
                "meta": {
                    "title": '连接质量评测',
                    "requiresAuth": True,
                    "icon": 'mdi:calculator'
                }
            }
        ],
        "meta": {
            "title": '模糊连接',
            "icon": 'mdi:file-document-multiple-outline',
            "order": 2
        }
    },
{
        "name": 'management',
        "path": '/management',
        "component": 'basic',
        "children": [
            {
                "name": 'management_user',
                "path": '/management/user',
                "component": 'self',
                "meta": {
                    "title": '用户管理',
                    "requiresAuth": True,
                    "icon": 'ic:round-manage-accounts'
                }
            },
        ],
        "meta": {
            "title": '系统管理',
            "icon": 'carbon:cloud-service-management',
            "order": 9
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
    },
    {
        "name": 'userinfo',
        "path": '/userinfo',
        "component": 'self',
        "meta": {
            "title": '用户信息',
            "requiresAuth": True,
            "icon": 'carbon:user',
            "hide": True,
            "singleLayout": 'basic'
        }
    },
]
