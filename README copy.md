# Website

## First steps

This site is generated with [Hugo](https://gohugo.io/). Read the [Docs](https://gohugo.io/documentation/).

### Serve locally

git clone https://github.com/binaridigital/binaridigital.github.io
hugo serve

### Deploy to Production

hugo --environment production

## Structure

Pages are componentized in sections and code, style and data are decoupled.

Code is found at `layouts/`, style at `assets/scss/`, data at `data/` _(component-level)_ and `content/` _(page-level)_.
