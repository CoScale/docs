---
layout: page
title: .NET Core plugin
description: Information on the metrics collected by the CoScale .NET Core plugin.
---

> .NET Core is an open-source and cross-platform framework to build applications for all operating system including Windows, Mac, and Linux. .NET Core is a fork of the NET Framework, a modular implementation that can be used in a wide variety of verticals, scaling from the data center to touch based devices.

More information on: [https://www.microsoft.com/net](https://www.microsoft.com/net)

## How it works

This plugin analyzes the performance of your .NET Core application.

**The minimal supported version of .NET Core is 1.1.x.**


## Configuration

For gathering global statistics, the AppMetric library is used alongside with the CoScale extension. You can download the extension from [https://github.com/CoScale/ResourceMetrics/releases](https://github.com/CoScale/ResourceMetrics/releases).

Add the AppMetrics library and the CoScale extension to the project: `<project-dir>WebApplication1.csproj`:

{% highlight xml %}
<ItemGroup>
    <PackageReference Include="App.Metrics.AspNetCore.Mvc" Version="2.0.0-alpha" />
    <PackageReference Include="App.Metrics.AspNetCore.Tracking" Version="2.0.0-alpha" />
    <Reference Include="ResourceMetrics">
        <HintPath>[path-to-file]\ResourceMetrics.dll</HintPath>
    </Reference>
</ItemGroup>
{% endhighlight %}

Change the `Program.cs` file to enable AppMetrics:

{% highlight cscharp %}
public static class Program
{
    public static IWebHost BuildWebHost(string[] args)
    {
        return WebHost.CreateDefaultBuilder(args)
                .UseMetrics()
                .UseMetricsWebTracking()
                .UseResourceMetrics()
                .UseStartup<Startup>()
                .Build();
    }

    public static void Main(string[] args) { BuildWebHost(args).Run(); }
}
{% endhighlight %}

Change the `Startup.cs` file in order to allow App Metrics to inspect MVC routes:

{% highlight cscharp %}
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseMvc();
    }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddMvc(options => options.AddMetricsResourceFilter());
    }
}
{% endhighlight %}

**Build the application to apply these changes.**

Provide the status URL, as you configured it on your server.
E.g.: `http://localhost/metrics`

## Active checks

This plugin can be configured to perform a HTTP GET on your .NET Core application. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page`) should be provided.

## Metrics

| Metric name                                               | Metric unit |
|-----------------------------------------------------------|-------------|
| .NET Core active check latency                            | s           |
| .NET Core active check uptime                             | %           |
| .NET Core Active Requests                                 | #           |
| .NET Core Application Performance Index                   |             |
| .NET Core Application Performance Index score             |             |
| .NET Core Average POST Size                               | b           |
| .NET Core Average PUT Size                                | b           |
| .NET Core GC last GC time                                 | s           |
| .NET Core GC total collection count                       | #           |
| .NET Core GC total memory                                 | b           |
| .NET Core One Minute Error Percentage Rate                | req         |
| .NET Core Process maximum physical memory set             | b           |
| .NET Core Process nonpaged system memory size             | b           |
| .NET Core Process paged memory size                       | b           |
| .NET Core Process peak paged memory size                  | b           |
| .NET Core Process peak working set                        | b           |
| .NET Core Process threads count                           | #           |
| .NET Core Process total processor time                    | %           |
| .NET Core Process user processor time                     | %           |
| .NET Core Process virtual memory size                     | b           |
| .NET Core Process working set                             | b           |
| .NET Core Request Error count                             | #           |
| .NET Core Request Error Rate                              | req         |
| .NET Core Request Error Rate Per Endpoint                 | req         |
| .NET Core Request Error Rate Per Endpoint And Status Code | req         |
| .NET Core Total Transactions                              | req         |
| .NET Core Total Transactions duration                     | s           |
| .NET Core Transactions Per Endpoint                       | req         |
| .NET Core Transactions Per Endpoint duration              | s           |
