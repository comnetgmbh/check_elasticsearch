#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Fabian Binder - comNET GmbH - 2018-03-29

register_check_parameters(
    subgroup_applications,
    "elasticsearch_active_shards_percent",
    _("Elasticsearch active Shards (percent)"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of active shards in percent"),
                    elements = [
                     Float(title = _("Warning at less than"),  unit = _("shards"), default_value = 100.0),
                     Float(title = _("Critical at less than"), unit = _("shards"), default_value = 50.0),
                    ]
                )
            ),
        ],
    ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_cluster",
    _("Elasticsearch cluster"),
    Transform(
        Dictionary(
            elements = [
                ("docs_count_delta",
                    Tuple (
                        title = _("Document count delta"),
                        help = _("If this parameter is set, the document count delta of the last minute will be compared to the delta of the average X minutes. You can set WARN or CRIT levels to check if the last minute's delta is X percent higher than the average delta."),
                        elements = [
                            Float( title = _("Warning at"), unit = _("percent higher than average")),
                            Float( title = _("Critical at"), unit = _("percent higher than average")),
                            Integer( title = _("Averaging"), unit = _("minutes"), minvalue = 1, default_value = 30),
                        ]
                    )
                ),
                ("size_delta",
                    Tuple (
                        title = _("Size delta"),
                        help = _("If this parameter is set, the size delta of the last minute will be compared to the delta of the average X minutes. You can set WARN or CRIT levels to check if the last minute's delta is X percent higher than the average delta."),
                        elements = [
                            Float( title = _("Warning at"), unit = _("percent higher than average")),
                            Float( title = _("Critical at"), unit = _("percent higher than average")),
                            Integer( title = _("Averaging"), unit = _("minutes"), minvalue = 1, default_value = 30),
                        ]
                    )
                )
            ]
        ),
    ),
    None,
    match_type = "first",
)

register_check_parameters(
    subgroup_os,
    "elasticsearch_cpu_usage",
    _("Elasticsearch CPU usage"),
    Dictionary(
        elements =  [
            ( 'levels',
                Tuple(
                    title = _("Alert on too high CPU utilization"),
                    elements = [
                        Percentage(title = _("Warning at a utilization of"), default_value=90.0),
                        Percentage(title = _("Critical at a utilization of"), default_value=95.0)
                    ],
                ),
            ),
        ]
    ),
    TextAscii(
        title = _("Node"),
        allow_empty = True
    ),
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_data_nodes",
    _("Elasticsearch Data Nodes"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of Data Nodes"),
                    elements = [
                        Integer(title = _("Warning at less than"),  unit = _("nodes"), default_value = 3),
                        Integer(title = _("Critical at less than"), unit = _("nodes"), default_value = 2),
                    ],
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_delayed_unassigned_shards",
    _("Elasticsearch delayed unsassigned Shards"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of delayed unassigned shards"),
                    elements = [
                        Integer(title = _("Warning at more than"),  unit = _("shards"), default_value = 0),
                        Integer(title = _("Critical at more than"), unit = _("shards"), default_value = 10),
                    ],
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_storage,
    "elasticsearch_indices",
    _("Elasticsearch Indices"),
    Dictionary(
        elements = [
            ("docs_count_delta",
                Tuple (
                    title = _("Document count delta"),
                    help = _("If this parameter is set, the document count delta of the last minute will be compared to the delta of the average X minutes. You can set WARN or CRIT levels to check if the last minute's delta is X percent higher than the average delta."),
                    elements = [
                        Float( title = _("Warning at"), unit = _("percent higher than average")),
                        Float( title = _("Critical at"), unit = _("percent higher than average")),
                        Integer( title = _("Averaging"), unit = _("minutes"), minvalue = 1, default_value = 30),
                    ]
                )
            ),
            ("size_delta",
                Tuple (
                    title = _("Size delta"),
                    help = _("If this parameter is set, the size delta of the last minute will be compared to the delta of the average X minutes. You can set WARN or CRIT levels to check if the last minute's delta is X percent higher than the average delta."),
                    elements = [
                        Float( title = _("Warning at"), unit = _("percent higher than average")),
                        Float( title = _("Critical at"), unit = _("percent higher than average")),
                        Integer( title = _("Averaging"), unit = _("minutes"), minvalue = 1, default_value = 30),
                    ]
                )
            )
        ]
      ),
    TextAscii(
        title = _("Index Name"),
        help = _("The name of the index"),
    ),
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_initializing_shards",
    _("Elasticsearch initializing Shards"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of initializing shards"),
                    elements = [
                        Integer(title = _("Warning at more than"),  unit = _("shards"), default_value = 0),
                        Integer(title = _("Critical at more than"), unit = _("shards"), default_value = 10),
                    ],
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_number_of_nodes",
    _("Elasticsearch Node count"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of Nodes"),
                    elements = [
                        Integer(title = _("Warning at less than"),  unit = _("nodes"), default_value = 3),
                        Integer(title = _("Critical at less than"), unit = _("nodes"), default_value = 2),
                    ]
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_pending_tasks",
    _("Elasticsearch pending Tasks"),
    Transform(
        Dictionary(
            elements = [
                ( 'tasks_delta',
                    Tuple (
                        title = _("Pending Tasks delta"),
                        help = _("If this parameter is set, the pending Task count delta of the last minute will be compared to the delta of the average X minutes. You can set WARN or CRIT levels to check if the last minute's delta is X percent higher than the average delta."),
                        elements = [
                            Float( title = _("Warning at"), unit = _("percent higher than average")),
                            Float( title = _("Critical at"), unit = _("percent higher than average")),
                            Integer( title = _("Averaging"), unit = _("minutes"), minvalue = 1, default_value = 30),
                        ]
                    )
                )
            ]
        ),
    ),
    None,
    match_type = "first",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_relocating_shards",
    _("Elasticsearch relocating Shards"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of relocating shards"),
                    elements = [
                        Integer(title = _("Warning at more than"),  unit = _("shards"), default_value = 0),
                        Integer(title = _("Critical at more than"), unit = _("shards"), default_value = 3),
                    ],
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_shards",
    _("Elasticsearch shards"),
    Transform(
        Dictionary(
            elements = [
                ("failed",
                    Alternative(
                        title = _("Failed shards"),
                        help = _("Setting levels on the failed shards is optional."),
                        elements = [
                            Tuple(
                                title = _("Percentual levels in relation to total shards"),
                                elements = [
                                    Percentage(title = _("Warning at"), unit = _("% of total shards failed")),
                                    Percentage(title = _("Critical at"), unit = _("% of total shards failed")),
                                ]
                            ),
                            Tuple(
                                title = _("Absolute levels of failed shards"),
                                elements = [
                                    Integer(title = _("Warning at"), unit = _("failed shards")),
                                    Integer(title = _("Critical at"), unit = _("failed shards")),
                                ]
                            )
                    ])
                )
            ]
        ),
    ),
    None,
    match_type = "first",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_task_max_waiting_in_queue",
    _("Elasticsearch Task max waiting time in queue"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("The maximum wait time of all tasks in the queue"),
                    elements = [
                        Integer(title = _("Warning at more than"),  unit = _("ms"), default_value = 1000),
                        Integer(title = _("Critical at more than"), unit = _("ms"), default_value = 5000),
                    ]
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)

register_check_parameters(
    subgroup_applications,
    "elasticsearch_unassigned_shards",
    _("Elasticsearch unassigned Shards"),
    Dictionary(
        elements = [
            ( 'levels',
                Tuple(
                    title = _("Number of unassigned shards"),
                    elements = [
                        Integer(title = _("Warning at more than"),  unit = _("shards"), default_value = 0),
                        Integer(title = _("Critical at more than"), unit = _("shards"), default_value = 3),
                    ],
                )
            ),
        ],
     ),
    None,
    match_type = "dict",
)
