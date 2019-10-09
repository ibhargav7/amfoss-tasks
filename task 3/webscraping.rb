require 'nokogiri'
require 'open-uri'

puts "what are you looking for ..  "
search = gets 
doc= Nokogiri::HTML(open('https://www.google.com/search?q='+search,'User-Agent'=>'Nooby'))

doc.xpath('//div/a/div[text()]').each do |link|
    puts link.content
end
   
