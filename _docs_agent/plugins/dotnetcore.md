---
layout: page
title: Monitoring and collecting data from .NET Core
description: Information on the metrics collected by the CoScale .NET Core plugin.
---

> .NET Core is an open-source and cross-platform framework to build applications for all operating system including Windows, Mac, and Linux. .NET Core is a fork of the NET Framework, a modular implementation that can be used in a wide variety of verticals, scaling from the data center to touch based devices.

More information on: [https://www.microsoft.com/net](https://www.microsoft.com/net)

## How it works

This plugin analyzes the performance of your .NET Core application.

**The minimal supported version of .NET Core is 1.1.x.**

## Installation

{% include_relative _installation.md orchestrator="false" service=".NET Core" %}

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


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/netcore.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
