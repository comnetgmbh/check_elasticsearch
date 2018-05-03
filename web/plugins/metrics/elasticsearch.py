#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Copyright (C) 2017 comNET GmbH
#
# This file is part of check_elasticsearch.
# 
# check_elasticsearch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with check_elasticsearch.  If not, see <http://www.gnu.org/licenses/>.

# Changelog:
# 2017-05-29, comNET GmbH, Fabian Binder

metric_info["elasticsearch_size_avg"] = {
        "title" : _("Average size growth"),
        "unit"  : "bytes",
        "color" : "33/a",
}

metric_info["elasticsearch_size_rate"] = {
        "title" : _("Size growth per minute"),
        "unit"  : "bytes",
        "color" : "31/a",
}

metric_info["elasticsearch_size"] = {
        "title" : _("Total size"),
        "unit"  : "bytes",
        "color" : "31/b",
}

metric_info["elasticsearch_count_avg"] = {
        "title" : _("Average document count growth"),
        "unit"  : "count",
        "color" : "45/a",
}

metric_info["elasticsearch_count_rate"] = {
        "title" : _("Document count growth per minute"),
        "unit"  : "count",
        "color" : "43/a",
}

metric_info["elasticsearch_count"] = {
        "title" : _("Total documents"),
        "unit"  : "count",
        "color" : "43/b",
}

perfometer_info.append(("stacked", [
    {
        "type"          : "logarithmic",
        "metric"        : "elasticsearch_size_rate",
        "half_value"    : 5000,
        "exponent"      : 2,
    },
    {
        "type"          : "logarithmic",
        "metric"        : "elasticsearch_count_rate",
        "half_value"    : 10,
        "exponent"      : 2,
    }
]))

metric_info["active_primary_shards"] = {
        "title" : _("Active primary shards"),
        "unit"  : "count",
        "color" : "21/b",
}

metric_info["active_shards"] = {
        "title" : _("Active shards"),
        "unit"  : "count",
        "color" : "21/a",
}

graph_info["active_shards"] = {
    "title"   : _("Active shards"),
    "metrics" : [
        ( "active_shards", "area" ),
        ( "active_primary_shards", "area" ),
    ],
}

perfometer_info.append(("dual", [
    {
    "type"       : "linear",
    "segments"  : [ "active_primary_shards"],
    "total"     : "active_shards",
    },
    {
    "type"       : "linear",
    "segments"  : [ "active_shards"],
    "total"     : "active_shards",
    }
]))

metric_info["active_shards_percent_as_number"] = {
        "title" : _("Active shards in percent"),
        "unit"  : "%",
        "color" : "22/a",
}

perfometer_info.append({
    "type"     : "linear",
    "segments" : [ "active_shards_percent_as_number" ],
    "total"    : 100.0,
})

metric_info["number_of_data_nodes"] = {
        "title" : _("Data nodes"),
        "unit"  : "count",
        "color" : "41/a",
}

metric_info["delayed_unassigned_shards"] = {
        "title" : _("Delayed unassigned shards"),
        "unit"  : "count",
        "color" : "42/a",
}

metric_info["initializing_shards"] = {
        "title" : _("Initializing shards"),
        "unit"  : "count",
        "color" : "52/a",
}

metric_info["number_of_nodes"] = {
        "title" : _("Nodes"),
        "unit"  : "count",
        "color" : "43/a",
}

metric_info["number_of_pending_tasks"] = {
        "title" : _("Pending tasks"),
        "unit"  : "count",
        "color" : "53/a",
}

metric_info["number_of_pending_tasks_rate"] = {
        "title" : _("Pending tasks delta"),
        "unit"  : "count",
        "color" : "14/b",
}

metric_info["number_of_pending_tasks_avg"] = {
        "title" : _("Average pending tasks delta"),
        "unit"  : "count",
        "color" : "26/a",
}

perfometer_info.append({
        "type"          : "logarithmic",
        "metric"        : "number_of_pending_tasks_rate",
        "half_value"    : 10,
        "exponent"      : 2,
        "unit"          : "count",
})

metric_info["relocating_shards"] = {
        "title" : _("Relocating shards"),
        "unit"  : "count",
        "color" : "16/b",
}

metric_info["task_max_waiting_in_queue_millis"] = {
        "title" : _("Maximum wait time of all tasks in queue"),
        "unit"  : "count",
        "color" : "11/a",
}

metric_info["unassigned_shards"] = {
        "title" : _("Unassigned shards"),
        "unit"  : "count",
        "color" : "14/a",
}
