{% extends "base.html" %}
{% block title %}Contact{% endblock %}
{% block head %}
   {{ super() }}
   <style>
   </style>
{% endblock %}

{% block toprowcontent %}
  <!-- Main jumbotron for a primary marketing message or call to action -->
  <article class="jumbotron">
    <section id="name-email-form">
      <p>
        To join the email list for
          <a href="http://www.seeourminds.com" title="SeeOurMinds.com home page">
            SeeOurMinds.com</a>
          and
          <a href="http://www.groja.com" title="Groja.com home page">
            Groja.com</a>,
          enter your name and email address in the form below.
      </p>
      <form action="" method="post" role="form">
        {{ form.hidden_tag() }}
        <div class="form-group">
          <label for="name">{{ form.name.label }}</label>
          {{ form.name( class="form-control", value=form.name.data ) }}
          <label for="email">{{ form.email.label }}</label>
          {{ form.email( class="form-control", value=form.email.data ) }}
        </div>
        <button type="submit" class="btn btn-success">Sign Up</button>
      </form>
    </section><!-- #name-email-form -->
  </article><!-- .jumbotron -->
  <article class="thanks">
    <div class="row">
      <div class="col-md-8">
        <section id="thanks">
          <h3>Thanks!</h3>
        </section><!-- #thanks -->
      </div><!-- .col-md-8 -->
    </div><!-- .row -->
  </article><!-- .thanks -->
{% endblock %}
{% block toprowsidebox %}
  <section id="process">
    <div class="sidebox">
      <h3>What to Expect</h3>
      <ul start="0">
        <li>
          We will send you updates every once in awhile.</li>
        <li>
          Keep an eye out for the Spiritual Portrait of
			   one of your favorite characters!</li>
      </ul>
      <p>Thanks!</p>
    </div><!-- .sidebox -->
    {{ super() }}
  </section><!-- #process -->
{% endblock %}
