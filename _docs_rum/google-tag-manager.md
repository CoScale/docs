---
layout: page
title: Google Tag Manager
description: Information on how to install the CoScale real user monitoring component using Google tag manager.
---

This manual will guide you through the process of adding the CoScale Real user monitoring component to Google Tags and publishing the changes to your website.

## Requirements

* The CoScale RUM snippet

    You can find it by going to <a href="#" db-href="/datasources/rum/" class="js-dashboard-link">`Datasources > Real user monitoring`</a> in our dashboard.
    
## Adding it to Google Tag Manager

Click the `New Tag` button.
<img class="img-responsive" alt="Create new tag" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/create_new_tag.png" />

Choose the 'Custom HTML Tag' product.
<img class="img-responsive" alt="Choose custom HTML tag" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/choose_product.png" />

Insert the CoScale RUM snippet.
<img class="img-responsive" alt="Insert Javascript snippet" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/add_javascript_snippet.png" />

Click the `All Pages` button, so the CoScale snippet will be added to all the pages on your website.
<img class="img-responsive" alt="Select all pages" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/select_all_pages.png" />

After click the `Create Tag` button on the bottom of the page. It will ask you for a tag name, fill in `CoScale RUM` or choose your own. Click `save` to go to your Tags list.
<img class="img-responsive" alt="Create meaningful tagname" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/tag_name.png" />

Click the `Publish` button to start to push the changes to your website.
<img class="img-responsive" alt="Publish changes" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/publish.png" />

Click the `Publish Now` button.
<img class="img-responsive" alt="Publish new tag" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/publish_now.png" />

That's it, the CoScale RUM component is now installed on your website and we will start gathering data.
<img class="img-responsive" alt="New tag has been published" src="{{ site.baseurl }}/gfx/installation/rum/google-tag-manager/published.png" />
