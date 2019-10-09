require 'nokogiri'
require 'open-uri'

doc= Nokogiri::HTML(open('https://www.google.com/search?q=Linux','User-Agent'=>'Nooby'))

doc.xpath('//div/a/div[text()]').each do |link|
    puts link.content
end
   
