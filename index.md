---
layout: index
---

{% assign postCount = site.posts | size %}
{% if postCount == 0 %}
<header class="entry-header">
    <h1 class="entry-content">henüz bir şey yazmadım</h1>
</header>
{% endif %}

{% for post in site.posts %}
<article class="post">
    <header class="entry-header">
        <h1 class="entry-title">
            <a href="{{ post.url }}" data="{{ post.language }}">{{ post.title }}</a>
        </h1>
        <div class="entry-meta">
            <span class="post-date"><a><time class="entry-date" datetime="{{ page.date | date_to_xmlschema }}">{{ post.date | date_to_long_string}}</time></a></span>
            <span class="post-category"><a href="#">Web Design</a></span>
            <!-- <span class="post-author"><a href="#">Albert Einstein</a></span> -->
            <!-- <span class="comments-link"><a href="#">4 Comments</a></span> -->
        </div>
    </header>
    <div class="entry-content clearfix">
        <p>{{ post.content }}</p>
        <!-- <div class="read-more">
            <a href="{{ post.url }}" class="more-link">Continue reading <span class="meta-nav">→</span></a>
        </div> -->
    </div>
</article>
{% endfor %}