require 'open-uri'
require 'uri'
require 'fileutils'

if ARGV.length < 2
  puts "Usage: 9-download_file.rb URL LOCAL_FILE_PATH"
else
  url, path = ARGV
  puts "Downloading file from #{url}..."
  URI.open(url) do |file|
    FileUtils.cp(file.path, path)
  end
  puts "File downloaded and saved to #{path}."
end
