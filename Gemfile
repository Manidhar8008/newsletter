source "https://rubygems.org"

# Build the static artifact directly. The github-pages meta-gem pins older
# transitive dependencies (including vulnerable rubyzip 2.x) that are not
# needed when deploying with actions/deploy-pages.
gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sitemap", "~> 1.4"
end
