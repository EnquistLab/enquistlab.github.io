require "jekyll"
require "jekyll-scholar"
require "yaml"
require "nokogiri"

root = File.expand_path("..", __dir__)
site = Jekyll::Site.new(Jekyll.configuration("source" => root, "config" => [], "safe" => true, "quiet" => true, "disable_disk_cache" => true))
Liquid::Template.register_filter(Jekyll::Filters)
source = File.read(File.join(root, "_pages/people.md"))
template = Liquid::Template.parse(source.split(/^---\s*$/, 3).last)
people = YAML.unsafe_load_file(File.join(root, "_data/people.yml"))
groups = {
  "postdocs" => "postdoctoral-researchers",
  "grad_students" => "graduate-students",
  "visiting_students" => "visiting-graduate-students",
  "staff" => "lab-team-technical-staff",
  "alumni" => "alumni"
}
fixtures = [people, {}, groups.transform_values { [] }, groups.transform_values { [{ "name" => "Test Member", "degree" => "Postdoc", "start_year" => 2020 }] }]
fixtures.each do |data|
  output = template.render!({ "site" => { "data" => { "people" => data } } }, registers: { site: site })
  document = Nokogiri::HTML.fragment(output)
  groups.each do |group, anchor|
    expected = Array(data[group]).any?
    raise "#{group}: incorrect nav visibility" unless !document.at_css("nav a[href='##{anchor}']").nil? == expected
    raise "#{group}: incorrect section visibility" unless !document.at_css("[id='#{anchor}']").nil? == expected
  end
end
puts "PASS: people links and sections agree for real, missing, empty and populated group data."

pages = Dir[File.join(root, "_pages/*")].map do |path|
  text = File.read(path)
  YAML.unsafe_load(text.split(/^---\s*$/, 3)[1]) if text.start_with?("---")
end.compact
nav = pages.select { |page| page["nav"] }.sort_by { |page| page["nav_order"] }
raise "primary navigation" unless nav.map { |page| page["title"] } == ["research", "people", "publications", "tools & data", "join us", "More"]
raise "secondary navigation" unless nav.last["children"].map { |child| child["permalink"] } == %w[/about/ /field-sites/ /news/ /teaching/ /community/ /conservation-impacts/ /contact/]

layout = Liquid::Template.parse(File.read(File.join(root, "_layouts/page.liquid")).split(/^---\s*$/, 3).last)
[{ "permalink" => "/" }, { "permalink" => "/people/", "section_nav" => false }, { "permalink" => "/research/" }].each do |page|
  output = layout.render!({ "page" => page, "site" => {} }, registers: { site: site })
  document = Nokogiri::HTML.fragment(output)
  raise "home heading" unless document.css("h1").length == (page["permalink"] == "/" ? 0 : 1)
  raise "duplicate summary navigation" unless document.css("nav").length == (page["permalink"] == "/research/" ? 1 : 0)
end
puts "PASS: navigation order and secondary URLs; home heading suppression; scoped summary navigation."

home = File.read(File.join(root, "_pages/home.md")).split(/^---\s*$/, 3).last
output = Liquid::Template.parse(home).render!({ "site" => {} }, registers: { site: site })
document = Nokogiri::HTML.fragment(output)
raise "home identity" unless document.css("h1").length == 1 && document.at_css("h1").text == "Macroecology Lab"
raise "duplicate home blocks" if document.at_css(".home-pillars, .home-process-grid")
raise "home card count" unless document.css(".home-card").length == 6
raise "recruitment and tools" unless document.at_css(".home-recruitment-status .status-chip") && document.at_css("a[href='/resources/']")
images = document.css("img")
raise "home image count" unless images.length == 7
images.each do |image|
  raise "missing image dimensions" unless image["width"].to_i > 0 && image["height"].to_i > 0
  raise "missing sizes" if image["sizes"].to_s.empty?
  image["srcset"].split(",").each do |candidate|
    path, width = candidate.split
    raise "missing derivative #{path}" unless File.file?(File.join(root, path.delete_prefix("/")))
    raise "incorrect width descriptor" unless path.end_with?("-#{width.delete_suffix('w')}.jpg")
  end
end
raise "hero loading" unless images.first["loading"] == "eager" && images.first["fetchpriority"] == "high" && images.first["sizes"] == "100vw"
raise "card loading" unless images.drop(1).all? { |image| image["loading"] == "lazy" }
puts "PASS: rendered home identity, six cards, recruitment/tools and all seven responsive image sources."