---
---
var docs =
[
    {% for post in site.docs_advanced %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_agent %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_custom_metrics %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_events %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_other %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_rum %}
        {% include post.json %}
    {% endfor %}
    {% for post in site.docs_tools %}
        {% include post.json %}
    {% endfor %}
];

// init lunr
var idx = lunr(function () {
    this.field('title', 10);
    this.field('content');
});

// add each document to be index
for(var index in docs) {
    idx.add(docs[index]);
}
