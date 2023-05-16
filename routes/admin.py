admin_route = [
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
            },
            {
                "name": 'dashboard_workbench',
                "path": '/dashboard/workbench',
                "component": 'self',
                "meta": {
                    "title": '工作台',
                    "requiresAuth": True,
                    "icon": 'icon-park-outline:workbench'
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
        "name": 'document',
        "path": '/document',
        "component": 'basic',
        "children": [
            {
                "name": 'document_vue',
                "path": '/document/vue',
                "component": 'self',
                "meta": {
                    "title": 'vue文档',
                    "requiresAuth": True,
                    "icon": 'logos:vue'
                }
            },
            {
                "name": 'document_vite',
                "path": '/document/vite',
                "component": 'self',
                "meta": {
                    "title": 'vite文档',
                    "requiresAuth": True,
                    "icon": 'logos:vitejs'
                }
            },
            {
                "name": 'document_naive',
                "path": '/document/naive',
                "component": 'self',
                "meta": {
                    "title": 'naive文档',
                    "requiresAuth": True,
                    "icon": 'logos:naiveui'
                }
            },
            {
                "name": 'document_project',
                "path": '/document/project',
                "component": 'self',
                "meta": {
                    "title": '项目文档',
                    "requiresAuth": True,
                    "localIcon": 'logo'
                }
            },
            {
                "name": 'document_project-link',
                "path": '/document/project-link',
                "meta": {
                    "title": '项目文档(外链)',
                    "requiresAuth": True,
                    "localIcon": 'logo',
                    "href": 'https://docs.soybean.pro/'
                }
            }
        ],
        "meta": {
            "title": '文档',
            "icon": 'mdi:file-document-multiple-outline',
            "order": 2
        }
    },
    {
        "name": 'component',
        "path": '/component',
        "component": 'basic',
        "children": [
            {
                "name": 'component_button',
                "path": '/"component"/button',
                "component": 'self',
                "meta": {
                    "title": '按钮',
                    "requiresAuth": True,
                    "icon": 'mdi:button-cursor'
                }
            },
            {
                "name": 'component_card',
                "path": '/"component"/card',
                "component": 'self',
                "meta": {
                    "title": '卡片',
                    "requiresAuth": True,
                    "icon": 'mdi:card-outline'
                }
            },
            {
                "name": 'component_table',
                "path": '/"component"/table',
                "component": 'self',
                "meta": {
                    "title": '表格',
                    "requiresAuth": True,
                    "icon": 'mdi:table-large'
                }
            }
        ],
        "meta": {
            "title": '组件示例',
            "icon": 'cib:app-store',
            "order": 3
        }
    },
    {
        "name": 'plugin',
        "path": '/plugin',
        "component": 'basic',
        "children": [
            {
                "name": 'plugin_charts',
                "path": '/plugin/charts',
                "component": 'multi',
                "children": [
                    {
                        "name": 'plugin_charts_echarts',
                        "path": '/plugin/charts/echarts',
                        "component": 'self',
                        "meta": {
                            "title": 'ECharts',
                            "requiresAuth": True,
                            "icon": 'simple-icons:apacheecharts'
                        }
                    },
                    {
                        "name": 'plugin_charts_antv',
                        "path": '/plugin/charts/antv',
                        "component": 'self',
                        "meta": {
                            "title": 'AntV',
                            "requiresAuth": True,
                            "icon": 'simple-icons:antdesign'
                        }
                    }
                ],
                "meta": {
                    "title": '图表',
                    "icon": 'mdi:chart-areaspline'
                }
            },
            {
                "name": 'plugin_map',
                "path": '/plugin/map',
                "component": 'self',
                "meta": {
                    "title": '地图',
                    "requiresAuth": True,
                    "icon": 'mdi:map'
                }
            },
            {
                "name": 'plugin_video',
                "path": '/plugin/video',
                "component": 'self',
                "meta": {
                    "title": '视频',
                    "requiresAuth": True,
                    "icon": 'mdi:video'
                }
            },
            {
                "name": 'plugin_editor',
                "path": '/plugin/editor',
                "component": 'multi',
                "children": [
                    {
                        "name": 'plugin_editor_quill',
                        "path": '/plugin/editor/quill',
                        "component": 'self',
                        "meta": {
                            "title": '富文本编辑器',
                            "requiresAuth": True,
                            "icon": 'mdi:file-document-edit-outline'
                        }
                    },
                    {
                        "name": 'plugin_editor_markdown',
                        "path": '/plugin/editor/markdown',
                        "component": 'self',
                        "meta": {
                            "title": 'markdown编辑器',
                            "requiresAuth": True,
                            "icon": 'ri:markdown-line'
                        }
                    }
                ],
                "meta": {
                    "title": '编辑器',
                    "icon": 'icon-park-outline:editor'
                }
            },
            {
                "name": 'plugin_swiper',
                "path": '/plugin/swiper',
                "component": 'self',
                "meta": {
                    "title": 'Swiper插件',
                    "requiresAuth": True,
                    "icon": 'simple-icons:swiper'
                }
            },
            {
                "name": 'plugin_copy',
                "path": '/plugin/copy',
                "component": 'self',
                "meta": {
                    "title": '剪贴板',
                    "requiresAuth": True,
                    "icon": 'mdi:clipboard-outline'
                }
            },
            {
                "name": 'plugin_icon',
                "path": '/plugin/icon',
                "component": 'self',
                "meta": {
                    "title": '图标',
                    "requiresAuth": True,
                    "localIcon": 'custom-icon'
                }
            },
            {
                "name": 'plugin_print',
                "path": '/plugin/print',
                "component": 'self',
                "meta": {
                    "title": '打印',
                    "requiresAuth": True,
                    "icon": 'mdi:printer'
                }
            }
        ],
        "meta": {
            "title": '插件示例',
            "icon": 'clarity:plugin-line',
            "order": 4
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
        "name": 'function',
        "path": '/function',
        "component": 'basic',
        "children": [
            {
                "name": 'function_tab',
                "path": '/function/tab',
                "component": 'self',
                "meta": {
                    "title": 'Tab',
                    "requiresAuth": True,
                    "icon": 'ic:round-tab'
                }
            },
            {
                "name": 'function_tab-detail',
                "path": '/function/tab-detail',
                "component": 'self',
                "meta": {
                    "title": 'Tab Detail',
                    "requiresAuth": True,
                    "hide": True,
                    "activeMenu": 'function_tab',
                    "icon": 'ic:round-tab'
                }
            },
            {
                "name": 'function_tab-multi-detail',
                "path": '/function/tab-multi-detail',
                "component": 'self',
                "meta": {
                    "title": 'Tab Multi Detail',
                    "requiresAuth": True,
                    "hide": True,
                    "multiTab": True,
                    "activeMenu": 'function_tab',
                    "icon": 'ic:round-tab'
                }
            }
        ],
        "meta": {
            "title": '功能',
            "icon": 'icon-park-outline:all-application',
            "order": 6
        }
    },
    {
        "name": 'exception',
        "path": '/exception',
        "component": 'basic',
        "children": [
            {
                "name": 'exception_403',
                "path": '/exception/403',
                "component": 'self',
                "meta": {
                    "title": '异常页403',
                    "requiresAuth": True,
                    "icon": 'ic:baseline-block'
                }
            },
            {
                "name": 'exception_404',
                "path": '/exception/404',
                "component": 'self',
                "meta": {
                    "title": '异常页404',
                    "requiresAuth": True,
                    "icon": 'ic:baseline-web-asset-off'
                }
            },
            {
                "name": 'exception_500',
                "path": '/exception/500',
                "component": 'self',
                "meta": {
                    "title": '异常页500',
                    "requiresAuth": True,
                    "icon": 'ic:baseline-wifi-off'
                }
            }
        ],
        "meta": {
            "title": '异常页',
            "icon": 'ant-design:exception-outlined',
            "order": 7
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
            "order": 8
        }
    },
    {
        "name": 'management',
        "path": '/management',
        "component": 'basic',
        "children": [
            {
                "name": 'management_auth',
                "path": '/management/auth',
                "component": 'self',
                "meta": {
                    "title": '权限管理',
                    "requiresAuth": True,
                    "icon": 'ic:baseline-security'
                }
            },
            {
                "name": 'management_role',
                "path": '/management/role',
                "component": 'self',
                "meta": {
                    "title": '角色管理',
                    "requiresAuth": True,
                    "icon": 'carbon:user-role'
                }
            },
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
            {
                "name": 'management_route',
                "path": '/management/route',
                "component": 'self',
                "meta": {
                    "title": '路由管理',
                    "requiresAuth": True,
                    "icon": 'material-symbols:route'
                }
            }
        ],
        "meta": {
            "title": '系统管理',
            "icon": 'carbon:cloud-service-management',
            "order": 9
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
            "singleLayout": 'basic'
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
            "order": 10
        }
    }
]
