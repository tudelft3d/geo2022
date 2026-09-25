# Exposes when the thesis data was last updated to Liquid as
# site.data['theses_updated'], with keys 'archive' (_data/geotheses.yml)
# and 'current' (_data/ongoing_theses.yml).
#
# The dates come from git history rather than site.time, so they only
# move when the data itself changes — via the maintenance scripts or by
# hand — and not on unrelated pushes that happen to rebuild the site.
# Falls back to the file's modification time and then to the build time
# when git history is unavailable. CI must check out with
# fetch-depth: 0, or every build there would silently take a fallback.
require 'shellwords'

module ThesesUpdated
  DATA_FILES = {
    'archive' => '_data/geotheses.yml',
    'current' => '_data/ongoing_theses.yml'
  }.freeze

  class Generator < Jekyll::Generator
    def generate(site)
      site.data['theses_updated'] =
        DATA_FILES.transform_values { |path| ThesesUpdated.last_updated(site, path) }
    end
  end

  def self.last_updated(site, path)
    out = %x(git -C #{Shellwords.escape(site.source)} log -1 --format=%cs -- #{path} 2>/dev/null).strip
    return out if out =~ /\A\d{4}-\d{2}-\d{2}\z/
    full = File.join(site.source, path)
    return File.mtime(full).strftime('%F') if File.exist?(full)
    site.time.strftime('%F')
  end
end
