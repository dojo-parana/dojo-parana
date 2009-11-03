require "fileutils"

class Dojo
  attr_accessor :class_name, :language
  
  def initialize(class_name, language)
    self.class_name = class_name
    self.language = language
  end
  
  def create
    if self.language == :ruby || self.language == :python
      # Create the Directory
      begin
        FileUtils.mkdir(self.directory)
      rescue Errno::EEXIST
        return $stderr.puts("Already exists.")
      end
    
      open(class_file, "w+") do |fd|
        class_template = open("tools/templates/#{self.language}/class#{self.extension}").read
        class_template.gsub!("#Class#", self.class_name)
      
        fd.write(class_template)
      end
    
      open(test_class_file, "w+") do |fd|
        test_class_template = open("tools/templates/#{self.language}/class_test#{self.extension}").read
        test_class_template.gsub!("#class#", self.class_name.downcase)
        test_class_template.gsub!("#TestClass#", self.test_class_name)
        test_class_template.gsub!("#Class#", self.class_name)
      
        fd.write(test_class_template)
      end
    else
      return $stderr.puts("Invalid Language.")
    end     
  end
  
  def extension
    case self.language
    when :ruby
      return ".rb"
    when :python
      return ".py"
    else
      raise "Invalid Language"
    end
  end
  
  def test_class_name
    return self.class_name + "Test"
  end
  
  def directory
    return self.class_name.downcase
  end
  
  def class_file
    return self.directory + "/" + self.class_name.downcase + self.extension
  end
  
  def test_class_file
    return self.directory + "/" + self.class_name.downcase + "_test" + self.extension
  end
end

if ARGV.length != 2
  $stderr.puts "USE: ruby tools/create_dojo.rb class_name language"
else
  d = Dojo.new(ARGV[0], ARGV[1].to_sym)
  d.create
end