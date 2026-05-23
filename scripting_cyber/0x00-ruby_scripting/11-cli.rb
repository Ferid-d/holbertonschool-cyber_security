elsif options[:list]
  puts "Tasks:"
  load_tasks.each_with_index { |t, i| puts "#{i + 1}. #{t}" }
