---
layout: index
---

{% assign postCount = site.posts | size %}
{% if postCount == 0 %}
<header class="entry-header">
    <h1 class="entry-content">henüz bir şey yazmadım</h1>
</header>
{% endif %}

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2951689275458403"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="fluid"
     data-ad-layout-key="-gw-3+1f-3d+2z"
     data-ad-client="ca-pub-2951689275458403"
     data-ad-slot="9781640845"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
{% for post in site.posts %}
<article class="post">
    <header class="entry-header">
        <div>
            <h1 class="entry-title">
                <a href="{{ post.url }}" data="{{ post.language }}">{{ post.title }}</a>
            </h1>
            <div class="entry-meta">
                <span class="post-date"><time class="entry-date"
                            datetime="{{ page.date | date_to_xmlschema }}">{{ post.date | date_to_long_string}}</time></span>
                {% for category in post.category %}<span class="post-category"><a>{{category}}</a></span>{% endfor %}
            </div>
        </div>
    </header>
    <div class="entry-content clearfix">
        <p>{{ post.content | strip_html | truncatewords:23, " ..." }}</p>
        <!-- <div class="read-more">
            <a href="{{ post.url }}" class="more-link">Continue reading <span class="meta-nav">→</span></a>
        </div> -->
    </div>
</article>
{% endfor %}
