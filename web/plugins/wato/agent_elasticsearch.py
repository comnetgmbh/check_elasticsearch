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
# 2017-05-23, comNET GmbH, Fabian Binder

group = "datasource_programs"

register_rule(group,
    "special_agents:elasticsearch",
    Dictionary(
        title = _("Request Elasticsearch data via REST API"),
        help = _("Requests data about elasticsearch clusters and indices"),
        elements = [
            ( "hosts",
              ListOfStrings(
                  title = _("Hostnames to query"),
                  help = _("Use this option to set which host should be checked by the special agent. If the "
                           "connection to the first server fails, the next server will be queried (fallback)."
                           "The check will only output data from the first host that sends a response."),
                  size = 40,
                  allow_empty = True,
              )
            ),
            ( "port",
              Integer(
                  title = _("Port"),
                  help = _("Use this option to query a port which is different from standard port 9200"),
                  default_value = 9200,
                  allow_empty = True,
              )
            ),
            ( "infos",
              Transform(
                  ListChoice(
                     choices = [
                         ( "health",          _("Cluster health") ),
                         ( "nodestats",       _("Node statistics") ),
                         ( "stats",           _("Cluster, Indices and Shard statistics") ),
                     ],
                     default_value = [ "health", "nodestats", "stats" ],
                     allow_empty = False,
                   ),
                   title = _("Retrieve information about..."),
                )
             ),
            ( "piggyback",
              TextAscii(
                  title = _("Display data on other host (piggyback)"),
                  help = _("Use this option to display the retrieved data on another host in Check_MK"),
                  allow_empty = True,
              )
            ),
        ],
        optional_keys = ["hostname", "piggyback"],
    ),
    title = _("Check Elasticsearch REST API"),
    match = 'first'
)

group = "agents/" + _("Agent Plugins")

register_rule(group,
    "agent_config:elasticsearch",
    CascadingDropdown(
        title = _("Elasticsearch plugin (Linux)"),
        help = _("If you activate this option, then the agent plugin <tt>elasticsearch</tt> will be deployed. "
                 "This plugin retrieves the same data as the special agent for elasticsearch."),
        style = "dropdown",
        choices = [
            ( "static", _("Deploy elasticsearch plugin"),
                Dictionary(
                    elements = [
                        ( "host", TextAscii(
                            title = _("Hostname"),
                            default_value = "localhost",
                        )),
                        ( "port", Integer(
                            title = _("TCP Port Number"),
                            minvalue = 1,
                            maxvalue = 65535,
                            default_value = 9200,
                        )),
                        ( "infos", Transform(
                            ListChoice(
                               choices = [
                                   ( "health",          _("Cluster health") ),
                                   ( "nodestats",       _("Node statistics") ),
                                   ( "stats",           _("Cluster, Indices and Shard statistics") ),
                               ],
                               default_value = [ "health", "nodestats", "stats" ],
                               allow_empty = False,
                             ),
                             title = _("Retrieve information about..."),
                        )),
                    ],
                    optional_keys = [ "page" ],
                ),
            ),
            ( None, _("Do not deploy the elasticsearch plugin") ),
        ]
    ),
)
