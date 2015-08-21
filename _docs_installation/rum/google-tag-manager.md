---
layout: page
title: Google Tag Manager
---

This manual will guide you through the process of adding the CoScale Real user monitoring component to Google Tags and publishing the changes to your website.

## Requirements

* The CoScale RUM snippet
    You can find it by going to your dashboard, selecting `Metrics` and then `Real user monitoring` in the sidebar. The instructions for adding RUM are in the top part of the page, you can find the snippet by clicking the `here` link.

## Adding it to Google Tag Manager

Click the `New Tag` button.

![Create new tag]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/create_new_tag.png)

Choose the 'Custom HTML Tag' product.

![Choose custom HTML tag]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/choose_product.png)

Insert the CoScale RUM snippet.

![Insert Javascript snippet]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/add_javascript_snippet.png)

Click the `All Pages` button, so the CoScale snippet will be added to all the pages on your website.

![Select all pages]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/select_all_pages.png)

After click the `Create Tag` button on the bottom of the page. It will ask you for a tag name, fill in `CoScale RUM` or choose your own. Click `save` to go to your Tags list.

![Create meaningfull tagname]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/tag_name.png)

Click the `Publish` button to start to push the changes to your website.

![Publish changes]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/publish.png)

Click the `Publish Now` button.

![Publish new tag]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/publish_now.png)

That's it, the CoScale RUM component is now installed on your website and we will start gathering data.

![New tag has been published]({{ site.baseurl }}/gfx/installation/rum/google-tag-manager/published.png)
