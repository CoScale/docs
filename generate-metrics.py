#!/usr/bin/env python3
import sys
import os
import re
from operator import itemgetter as i
from functools import cmp_to_key
import json

# Helper to read file
def read(plugin, directory, file):
    content = []
    location = "%s/%s/%s" % (directory, plugin, file)
    try:
        with open(location) as f:
            content = f.readlines()

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    except FileNotFoundError:
        print('\t\t! No %s file found' % location)

    return content

# Helper to read metrics
def readMetrics(plugin, directory):
    metrics = []
    for line in read(plugin, directory, 'metrics'):
        if line.startswith('METRIC'):
            m = re.search('^METRIC:[0-9]+ ([A-Z]+) "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" ([0-9]+)$', line)
        else:
            m = re.search('^([A-Z]+) "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" ([0-9]+) "[A-z]+"$', line)

        if m is not None:
            dimensions = []
            if m.group(7) != '':
                dimensions = [x.split(':')[1] for x in m.group(7).split(',')]

            result = {
                'type': m.group(1),
                'name': m.group(2),
                'description': m.group(3),
                'group': m.group(4),
                'unit': m.group(5),
                'unknown': m.group(6),
                'dimensions': ', '.join(dimensions),
                'interval': m.group(8) or ''
            }
            metrics.append(result)


    metrics = sorted(metrics, key=lambda k: (k['group'].lower(), k['name'].lower()))
    print('\t\t%s metrics found' % len(metrics))

    return metrics

# Helper to read events
def readEvents(plugin, directory):
    events = []
    for line in read(plugin, directory, 'events'):
        m = re.search('^EVENT:([0-9]+) "([^"]*)" "([^"]*)" "(\[.*])" "([^"]*)"( ".*")?$', line)

        if m is not None:
            attributes = []
            jsonData = json.loads(m.group(4))
            if jsonData is not None:
                print(jsonData)
                attributes = [x['name'] for x in jsonData]

            result = {
                'id': m.group(1),
                '?': m.group(2),
                'name': m.group(3),
                'attributes': ', '.join(attributes),
                'description': m.group(5),
                'plugin': m.group(6)
            }
            events.append(result)

    print('\t\t%s events found' % len(events))

    return events

def loop(directory):
    print('Parsing files in %s' % directory)
    for plugin in os.listdir(directory):
        print(plugin)
        print('\tParsing metrics/events')

        # Read metrics from API
        metrics = readMetrics(plugin, directory)
        events = readEvents(plugin, directory)

        # Generate file
        print('\tGenerating markdown')
        file = open('./_includes/plugins/%s.md' % plugin.lower(), 'w+')

        if (len(metrics) > 0):
            group = ''
            file.write('## Metrics\n')
            for metric in metrics:
                if group != metric['group']:
                    file.write('\n')
                    file.write('### %s \n' % metric['group'].replace('Agent/', '').replace('/', ' / '))
                    file.write('\n')
                    file.write('| Name | Unit | Dimensions |\n')
                    file.write('|------|------|------------|\n')
                    group = metric['group']

                print(metric)
                file.write('| %s | %s | %s |\n' % (
                    metric['name'],
                    metric['unit'],
                    metric['dimensions']
                ))
            file.write('\n')

        if (len(events) > 0):
            file.write('## Events\n')
            file.write('\n')
            file.write('| Name | Description | Attributes |\n')
            file.write('|------|-------------|------------|\n')
            for event in events:
                print(event)
                file.write('| %s | %s | %s |\n' % (
                    event['name'],
                    event['description'],
                    event['attributes']
                ))
            file.write('\n')

# Check input var
if len(sys.argv) < 2:
    print('Please provide full path to API directory')
    exit(1)

# Check path content
path = sys.argv[1].strip()
if path[-1] == '/':
    path = path[:-1]
root = '%s/conf' % path

# Loop plugins
loop("%s/plugin-metrics" % root)
loop("%s/collector-metrics" % root)
