---
layout: page
title: Widgets
description: Overview of CoScale dashboard widgets
---

Widgets are your main visualization tool. In CoScale, we support different types of widgets and allow many customization options. To add widgets and see the array of possibilities, follow the steps below.

## Add widget

Click the 'Add widget' button on the top right of any dashboard.

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/add_widget.png" alt=" screenshot" class="img-responsive" />

## Select the datasource

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/select_datasource.png" alt=" screenshot" class="img-responsive" />

## Select metrics and events

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/select_metrics.png" alt=" screenshot" class="img-responsive" />

Your selection will also be visible in the right side.

You can search for a metric, using just a keyword / part of the full metric name.

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/search_metric.png" alt=" screenshot" class="img-responsive" />


## Choose widget type

Based on your previous selection, only the applicable widget types are available at this step. There are also configuration options below the graph area, for more customization.

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/widget_gauge.png" alt=" screenshot" class="img-responsive" />

Click on Finish and the widget will be diplayed on the dashboard.

## Settings

You can edit the widget's name by clicking on that title, or you can click on the hamburger icon for more options.

<img src="{{ site.baseurl }}/gfx/dashboard/widgets/widget_settings.png" alt=" screenshot" class="img-responsive" />

<ul>
  <li><b>Widget settings</b>: Contains the settings (metrics, events, widget type, widget options)</li>
  <li><b>Enable time lock</b>: Every widget on the page follows the time selector by default. With the time lock you can lock a widget on a certain time range.</li>
  <li><b>Mode</b>: Average, First, Last, Minimum, Maximum, Diff, Sum</li>
  <li><b>Export data</b>: Exports the information from the selected metrics, in the given time interval.</li>
  <li><b>Copy widget</b>: Copies the widget.</li>
  <li><b>Delete this widget</b>: Removes the widget from the dashboard.</li>
</ul>

## Types
<ul class="list-inline">
    <li><i class="fa fa-line-chart fa-fw"></i> Chart</li>
    <li><i class="fa fa-table fa-fw"></i> Table</li>
    <li><i class="fa fa-bug fa-fw"></i> Errors</li>
    <li><i class="fa fa-square-o fa-fw"></i> Tile</li>
    <li><i class="fa fa-th fa-fw"></i> Heatmap</li>
    <li><i class="fa fa-pie-chart fa-fw"></i> Pie chart</li>
    <li><i class="fa fa-tachometer fa-fw"></i> Gauge</li>
    <li><i class="fa fa-list fa-fw"></i> Event overview</li>
    <li><i class="fa fa-list-alt fa-fw"></i> Anomaly timeline</li>
</ul>

<div class="row">
    <div class="col-sm-12">
        <h3>Chart</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/chart.png" alt="Chart screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-12">
        <h3>Table</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/table.png" alt="Table screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-6">
        <h3>Heatmap</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/heatmap.png" alt="Heatmap screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-6">
        <h3>Pie chart</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/pie-chart.png" alt="Pie chart screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-6">
        <h3>Gauge</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/gauge.png" alt="Gauge screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-6">
        <h3>Tile</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/tile.png" alt="Tile screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-12">
        <h3>Event overview</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/event-overview.png" alt="Event overview screenshot" class="img-responsive" />
    </div>

    <div class="col-sm-12">
        <h3>Anomaly timeline</h3>
        <img src="{{ site.baseurl }}/gfx/dashboard/widgets/anomaly-timeline.png" alt="Anomaly timeline screenshot" class="img-responsive" />
    </div>
</div>
